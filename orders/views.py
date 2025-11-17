from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
import requests
from django.conf import settings
from .models import Order
from .serializers import OrderSerializer

class CreateOrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        
        # Send Telegram notification to owner
        self.send_telegram_notification(order)
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def send_telegram_notification(self, order):
        """Send Telegram notification when a new order is created"""
        try:
            bot_token = getattr(settings, 'TELEGRAM_BOT_TOKEN', None)
            chat_id = getattr(settings, 'TELEGRAM_CHAT_ID', None)
            
            if bot_token and chat_id:
                message = f"""
🎉 *New Baby Care Order!*

📦 *Order ID:* #{order.id}
👤 *Customer:* {order.full_name}
📱 *Phone:* {order.phone_number}
📍 *City:* {order.city}
🔢 *Quantity:* {order.quantity}
💰 *Total:* {order.quantity * 2500} DZD
📅 *Date:* {order.created_at.strftime('%Y-%m-%d %H:%M:%S')}

Please contact the customer to confirm the order! 📞
"""
                
                url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
                payload = {
                    'chat_id': chat_id,
                    'text': message,
                    'parse_mode': 'Markdown'
                }
                
                requests.post(url, json=payload, timeout=5)
        except Exception as e:
            # Log the error but don't prevent order creation
            print(f"Failed to send Telegram notification: {str(e)}")

            print(f"Failed to send email notification: {str(e)}")

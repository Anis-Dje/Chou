from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
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
        
        # Send email notification to owner
        self.send_order_notification(order)
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def send_order_notification(self, order):
        """Send email notification when a new order is created"""
        try:
            subject = f'🎉 New Baby Care Order #{order.id}'
            message = f"""
New Order Received!

Order Details:
--------------
Order ID: #{order.id}
Customer: {order.full_name}
Phone: {order.phone_number}
City: {order.city}
Quantity: {order.quantity}
Date: {order.created_at.strftime('%Y-%m-%d %H:%M:%S')}

Total Amount: {order.quantity * 2500} DZD

Please contact the customer to confirm the order.

---
Baby Care Shop - Order Management System
"""
            
            # Get owner email from settings
            owner_email = getattr(settings, 'OWNER_EMAIL', None)
            
            if owner_email:
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[owner_email],
                    fail_silently=True,  # Don't raise exception if email fails
                )
        except Exception as e:
            # Log the error but don't prevent order creation
            print(f"Failed to send email notification: {str(e)}")

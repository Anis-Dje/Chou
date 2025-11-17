# 📱 Telegram Bot Setup Guide

Get instant notifications on your phone when new orders arrive!

## Quick Setup (5 minutes)

### Step 1: Create Your Telegram Bot

1. **Open Telegram** on your phone or computer
2. **Search for** `@BotFather` (the official bot creator)
3. **Start a chat** and send: `/newbot`
4. **Choose a name** for your bot (e.g., "Baby Care Orders Bot")
5. **Choose a username** (must end in 'bot', e.g., "babycare_orders_bot")
6. **Copy the token** - It looks like: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`

### Step 2: Get Your Chat ID

**Option A: Using @userinfobot (Easiest)**
1. Search for `@userinfobot` in Telegram
2. Start a chat with it
3. It will send you your chat ID (a number like `123456789`)

**Option B: Using your bot**
1. Search for your bot in Telegram (the username you created)
2. Click **START** or send any message to your bot
3. Open this URL in your browser (replace with your bot token):
   ```
   https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
   ```
4. Look for `"chat":{"id":123456789}` in the response
5. That number is your Chat ID

### Step 3: Configure on Render

1. Go to your **Render Dashboard**
2. Select your **backend service**
3. Click **Environment** tab
4. Add these variables:

```
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
TELEGRAM_CHAT_ID=123456789
```

5. Click **Save**
6. Render will automatically redeploy

### Step 4: Test It!

1. Wait for Render to finish deploying (1-2 minutes)
2. Go to **https://brikoula.vercel.app**
3. Submit a test order
4. You should receive an instant notification on Telegram! 🎉

## What You'll Receive

Every time someone places an order, you'll get:

```
🎉 New Baby Care Order!

📦 Order ID: #123
👤 Customer: John Doe
📱 Phone: 0555123456
📍 City: Algiers
🔢 Quantity: 2
💰 Total: 5000 DZD
📅 Date: 2025-11-17 20:30:45

Please contact the customer to confirm the order! 📞
```

## Advantages Over Email

✅ **Instant** - Get notifications in 1-2 seconds
✅ **Mobile-friendly** - Perfect for on-the-go
✅ **No spam folder** - Always see your orders
✅ **Free** - No email service costs
✅ **Reliable** - Telegram is always online
✅ **Easy setup** - No app passwords or SMTP config

## Testing Locally

Create a `.env` file in `chou` directory:

```env
TELEGRAM_BOT_TOKEN=your-token
TELEGRAM_CHAT_ID=your-chat-id
```

Run your Django server and test!

## Troubleshooting

### Not receiving notifications?

1. **Check bot token**: Make sure it's correct in Render environment variables
2. **Check chat ID**: Must be your personal chat ID (a number)
3. **Start the bot**: You MUST click START in Telegram before receiving messages
4. **Check logs**: Look at Render logs for any errors
5. **Test the bot**: Send a message to verify it's working

### How to verify bot token is correct:

Open this URL in browser (replace with your token):
```
https://api.telegram.org/bot<YOUR_TOKEN>/getMe
```

Should return your bot information.

### How to test notification manually:

```bash
curl -X POST https://api.telegram.org/bot<YOUR_TOKEN>/sendMessage \
  -H "Content-Type: application/json" \
  -d '{"chat_id":"<YOUR_CHAT_ID>","text":"Test notification!"}'
```

## Group Notifications (Optional)

Want to send notifications to a group?

1. Create a Telegram group
2. Add your bot to the group
3. Make the bot an admin (optional)
4. Get the group chat ID (negative number like `-987654321`)
5. Use the group chat ID in environment variables

## Security Notes

✅ Bot token is secret - never share it
✅ Chat ID is just your user ID - safe to use
✅ Notifications fail silently - orders still work if bot is down
✅ No customer data is stored in Telegram

---

Need help? Test your setup step by step and check the troubleshooting section!

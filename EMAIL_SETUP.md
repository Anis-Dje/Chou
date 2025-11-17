# Email Notification Setup Guide

## Overview
The system sends automatic email notifications to the owner whenever a new order is placed.

## Setup Instructions

### Option 1: Gmail (Recommended for Easy Setup)

1. **Enable 2-Factor Authentication on your Gmail account**
   - Go to https://myaccount.google.com/security
   - Enable 2-Step Verification

2. **Create an App Password**
   - Visit: https://myaccount.google.com/apppasswords
   - Select "Mail" and "Other (Custom name)"
   - Name it "Baby Care Shop"
   - Copy the 16-character password

3. **Set Environment Variables on Render**
   - Go to your Render dashboard
   - Select your backend service
   - Go to "Environment" tab
   - Add these environment variables:
     ```
     EMAIL_HOST_USER=your-email@gmail.com
     EMAIL_HOST_PASSWORD=your-16-char-app-password
     OWNER_EMAIL=owner-notification-email@gmail.com
     ```

### Option 2: Other Email Providers

#### SendGrid
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = 'your-sendgrid-api-key'
```

#### Mailgun
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-mailgun-username'
EMAIL_HOST_PASSWORD = 'your-mailgun-password'
```

## Testing Locally

1. **Create a `.env` file** in the `chou` directory:
   ```env
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-app-password
   OWNER_EMAIL=your-test-email@gmail.com
   ```

2. **Test the email**:
   ```bash
   python manage.py shell
   ```
   
   Then run:
   ```python
   from django.core.mail import send_mail
   from django.conf import settings
   
   send_mail(
       'Test Email',
       'This is a test email from Baby Care Shop',
       settings.DEFAULT_FROM_EMAIL,
       [settings.OWNER_EMAIL],
       fail_silently=False,
   )
   ```

## Email Notification Content

When a new order is placed, the owner receives:
- Order ID
- Customer name
- Phone number
- City/Wilaya
- Quantity ordered
- Total amount (DZD)
- Order date and time

## Troubleshooting

### Emails not being received?

1. **Check spam folder** - First emails might go to spam
2. **Verify environment variables** - Ensure all are set correctly on Render
3. **Check Gmail security** - Make sure 2FA and App Password are set up
4. **Review logs** - Check Render logs for email errors
5. **Test SMTP connection**:
   ```python
   from django.core.mail import send_mail
   send_mail('Test', 'Test message', 'from@example.com', ['to@example.com'])
   ```

### Common Issues

- **Authentication Error**: Wrong app password or username
- **SSL Error**: Check EMAIL_USE_TLS setting
- **Connection Timeout**: Firewall blocking port 587
- **Quota Exceeded**: Gmail has daily sending limits (500/day)

## Security Notes

- ✅ Never commit `.env` file to git
- ✅ Use App Passwords, not your actual Gmail password
- ✅ Email notifications fail silently to not break order creation
- ✅ All email credentials are stored in environment variables

## Alternative: Webhook Notifications

If email doesn't work, you can also set up:
- **Telegram Bot** - Instant notifications on your phone
- **Discord Webhook** - Notifications in Discord channel
- **Slack Integration** - Team notifications
- **SMS via Twilio** - Text message alerts

Let me know if you want to set up any of these alternatives!

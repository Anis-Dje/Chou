# Quick Deploy Checklist

## ✅ Backend Deployment (Render)

Your backend is now deploying with:
- ✅ Email notification system
- ✅ Fixed CORS configuration
- ✅ WhiteNoise middleware for static files

### Environment Variables to Set on Render:

Go to your Render dashboard → Your service → Environment tab

Add these variables:

```
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-gmail-app-password
OWNER_EMAIL=where-to-receive-notifications@gmail.com
```

**To get Gmail App Password:**
1. Enable 2FA: https://myaccount.google.com/security
2. Create App Password: https://myaccount.google.com/apppasswords
3. Select "Mail" and "Other (Custom name)"
4. Copy the 16-character password (no spaces)

### Monitor Deployment:

1. Go to Render dashboard
2. Watch the deploy logs
3. Should complete in 2-3 minutes
4. Check for "Build successful" message

### Test After Deployment:

1. Go to https://brikoula.vercel.app
2. Fill out the order form
3. Submit an order
4. Check:
   - ✅ No more CORS errors in browser console
   - ✅ Success message appears
   - ✅ Order saved in database
   - ✅ Email received (if env vars are set)

## 📧 Email Setup (Optional but Recommended)

If you skip email setup now:
- Orders will still work perfectly
- No email notifications will be sent
- You can add email later anytime

If you set up email:
- Get instant notification for every order
- Email includes all order details
- Professional automated system

## 🔍 Troubleshooting

**If CORS error persists:**
- Wait 2-3 minutes for Render to finish deploying
- Hard refresh the frontend (Ctrl+Shift+R)
- Check Render logs for deployment status

**If email doesn't work:**
- Check Render logs for email errors
- Verify environment variables are set correctly
- Make sure Gmail app password (not regular password)
- Check spam folder

**To view Render logs:**
- Dashboard → Your service → Logs tab
- Look for errors or email sending attempts

---

Need help? The system is configured and ready - just needs the deploy to finish!

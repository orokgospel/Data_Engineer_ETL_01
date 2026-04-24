# 1. Turn ON 2-Step Verification (Required)

Gmail App Passwords only work if 2FA is enabled.

Go to: https://myaccount.google.com/security

Under “Signing in to Google”

Click 2-Step Verification

Follow setup (SMS or Google Authenticator)

# 2. Generate App Password

After enabling 2FA:

- Go again to: https://myaccount.google.com/security
  
Click App passwords

>(You may need to search it if not visible)

Then:

Select app: Mail

Select device: Other (Custom name) → e.g. Python SMTP

Click Generate

You will get a 16-character password like:

abcd efgh ijkl mnop

👉 This is what you use in Python.

If you lost it → generate a new one

Just create a new one:

Steps:

Go to App Passwords page
Click Create new app password

Select:
> App: Mail
> 
Device: Custom (e.g. “Python Script”)

Click Generate

Copy it immediately

# 3. Revoke old password (recommended)

If you think it’s exposed:

Same App Password page
Click Delete / Revoke

This immediately disables it.

# Email Configuration
# Copy this file and rename it to email_config_local.py
# Then update the values with your actual email credentials

EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'sender_email': 'mohithbutta4002@gmail.com',  # Your Gmail address
    'sender_password': 'your_app_password_here',  # Your Gmail App Password
    'recipient_email': 'mohithbutta4002@gmail.com'  # Where to send messages
}

# Instructions:
# 1. Create a Gmail App Password:
#    - Go to your Google Account settings
#    - Enable 2-Factor Authentication if not already enabled
#    - Go to Security > App passwords
#    - Generate a new app password for "Mail"
#    - Copy the 16-character password
# 
# 2. Replace 'your_app_password_here' with your actual app password
# 
# 3. Update the email addresses if needed

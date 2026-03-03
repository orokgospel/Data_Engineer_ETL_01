import pandas as pd
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Example DataFrame
data = pd.DataFrame({
    "Full Name": ["gospel orok"]
})

# Split applicant names into First Name and Last Name
data[["First Name", "Last Name"]] = data["Full Name"].apply(
    lambda x: pd.Series([n.capitalize() for n in x.split(" ", 1)])
)

# Email sender credentials
sender_email = "orokgospel@gmail.com"
password = "ywuk xdzg citw dtgb"

# Email server setup
smtp_server = "smtp.gmail.com"
smtp_port = 465

# Loop through each applicant in the DataFrame
for index, row in data.iterrows():
    receiver_email = "orokgospel@gmail.com"  # Replace with actual receiver
    first_name = row["First Name"]

    # Create the email
    msg = MIMEMultipart("alternative")
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = "Welcome to the Data Engineering Program"

    # HTML content
    html_body = f"""
    <html>
      <body>
        <p>Hi {first_name},</p>
        <p>Welcome to the program! We're excited to have you onboard...</p>
      </body>
    </html>
    """

    msg.attach(MIMEText(html_body, "html"))

    # Send the email
    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print(f"Email sent to {first_name} ({receiver_email})")
        time.sleep(1)  # Optional delay between emails

    except Exception as e:
        print(f"Failed to send email to {first_name} ({receiver_email}): {e}")

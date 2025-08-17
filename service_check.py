import os
import smtplib
from email.mime.text import MIMEText

# List of services to check
services = ["nginx", "mysql"]
down = []

# Check service status
for service in services:
    status = os.system(f"systemctl is-active --quiet {service}")
    if status != 0:
        down.append(service)

# If any service is down, send email
if down:
    body = "ALERT: DOWN Services: " + ", ".join(down)
    msg = MIMEText(body, 'plain')
    msg['From'] = "from@example.com"
    msg['To'] = "to@example.com"
    msg['Subject'] = "Service Alert"

    # Mailtrap SMTP credentials
    smtp_host = "smtp.mailtrap.io"
    smtp_port = 2525
    smtp_user = "your_mailtrap_user"  # replace with your Mailtrap user
    smtp_pass = "your_mailtrap_pass"  # replace with your Mailtrap password

    # Send email
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()  # optional but recommended
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)

    print("Alert email sent successfully!")

import smtplib, psutil
from email.mime.text import MIMEText
from datetime import datetime

# SMTP configuration for Gmail
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_FROM = "surajlearnig@gmail.com"        # Your Gmail address
EMAIL_TO = "chauhansuraj29100@gmail.com"        # Recipient Gmail address
EMAIL_PASS = "Suraj@291"           # Use Gmail App Password

# Log file path
LOG_FILE = "/home/ubuntu/monitoring.log"

def log_message(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"{now} | {message}\n")
    print(message)  # optional: also print to console

def send_gmail_alert(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()                     # Secure connection
            server.login(EMAIL_FROM, EMAIL_PASS)
            server.sendmail(EMAIL_FROM, [EMAIL_TO], msg.as_string())
        print("Alert email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Check system usage
cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

log_message(f"CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%")

# Trigger alert if CPU > 90 AND Memory > 90 AND Disk > 90
if cpu > 5 and memory > 5 and disk > 90:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    subject = "⚠️ Server Alert"
    body = f"Alert at {now}\nCPU: {cpu}% | Memory: {memory}% | Disk: {disk}%"
    send_gmail_alert(subject, body)

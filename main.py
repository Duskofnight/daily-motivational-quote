import schedule, time, os, smtplib, random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

quotes = []

password = os.environ['mail_password']
username = os.environ['mail_username']


def sendMail():
  f = open("quotes.txt", "r")
  quotes = f.read().split("\n")
  f.close()
  quote = random.choice(quotes)
  email = quote
  server = "smtp.gmail.com"
  port = 587
  s = smtplib.SMTP(host = server, port=port)
  s.starttls()
  s.login(username, password)

  msg = MIMEMultipart()
  msg["To"] = username
  msg["From"] = username
  msg["Subject"] = "Motivational quote of the day"
  msg.attach(MIMEText(email, 'html'))
  
  s.send_message(msg)
  del msg


schedule.every(24).hours.do(sendMail)

while True:
  schedule.run_pending()
  time.sleep(1)
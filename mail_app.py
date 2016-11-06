import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
 
fromaddr = "archhacks0511@gmail.com"
toaddr = "venkatanarendra18@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Notification regarding patient"


body = "Pateint X has anomaly"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(fromaddr, "ufatarchhacks")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

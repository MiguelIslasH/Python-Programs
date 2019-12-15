from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from smtplib import SMTP
mensaje = MIMEMultipart("plain")
mensaje["From"]="yourMail"
mensaje["To"]= "targetMail"
mensaje["Subject"] ="Correo de prueba desde Python 3"
adjunto = MIMEBase("application","octect-stream")
adjunto.set_payload(open("yourDocument.txt","rb").read())
adjunto.add_header("content-Disposition",'attachment; filename="mensaje.txt"')
mensaje.attach(adjunto)
smtp = SMTP("smtp.live.com")
#smtp.gmail.com for google accounts
#smtp.yahoo.com for yahoo accounts
smtp.starttls()
smtp.login("yourMail","yourPassword")
smtp.sendmail("yourMail","targetMail",mensaje.as_string())
smtp.quit()

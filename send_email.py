from email.mime.text import MIMEText
import smtplib

def send_email(email,height,avg_height,count):
    from_email="aarushi1427@gmail.com"
    from_password="Abc@1234"
    to_email=email

    subject="Height data"
    message="Hey,your height is <strong>%s</strong>.<br> The average height is <strong>%s</strong> and that is calculated out of <strong>%s</strong> people.<br>Thanks!" %(height,avg_height,count)

    msg=MIMEText(message,"html")
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)

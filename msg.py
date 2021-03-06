import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
# from password import password_id, mail_id

fromaddr = "fortvkhush@gmail.com"
password = "fortvkhush.01"
def SendMail(ImgFileName):
    img_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'Mask not detected'
    msg['From'] = fromaddr
    msg['To'] = fromaddr

    text = MIMEText("Mask not detected.")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(fromaddr, password)
    s.sendmail(fromaddr, fromaddr, msg.as_string())
    print("Mail send successfully.")
    s.quit()
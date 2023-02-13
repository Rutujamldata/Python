"""
Created on Wed Feb  8 12:18:24 2023

@author: rutuja
"""
import json
from email.mime.multipart import MIMEMultipart
import os 

from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib, ssl
import shutil
import requests
        
########################################### Sendi mail ###############################
sender_email = "mailto:*********@gmail.com"
receiver_email = "mailto:*******@gmail.com"
# receiver_email = x.Email
password ="**********"
message = MIMEMultipart("alternative")
message["From"] = sender_email
message["To"] = receiver_email
part2 = MIMEText("hi hello")


context = ssl.create_default_context()
            
           
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    print(server)
    server.sendmail(sender_email, receiver_email, message.as_string())      



############################### sending mail with attachments #################
        
sender_email = "mailto:maskesagar1997@gmail.com"
receiver_email = "mailto:rutujanaik125@gmail.com"
# receiver_email = x.Email
password ="fkcmrjxhwbengeyv" ##App Password from gmail ->https://support.google.com/mail/answer/185833?hl=en


message = MIMEMultipart("alternative")
  
message["From"] = sender_email
message["To"] = receiver_email
       
part2 = MIMEText("hi hello")
path=r"C:\Users\user\Documents"
os.chdir(path)      
attachments = os.listdir(path)

if len(attachments) > 0: # are there attachments?
    for filename in attachments:
          f = path + '/' + 'Python developer.pdf'
          part = MIMEBase('application', "octet-stream")
          part.set_payload( open(f,"rb").read() )
          encoders.encode_base64(part)
          part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
          message.attach(part)
   
message.attach(part2)

            
context = ssl.create_default_context()
            
           
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    print(server)
    server.sendmail(sender_email, receiver_email, message.as_string())
  

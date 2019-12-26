'''
1) enable 2 step verification
2) go to enable app password
3) Generate the APP password
'''
import smtplib
import os
from email.message import EmailMessage
import imghdr

#setting the env. variables#
SENDER_EMAIL_ADDRESS = " "
EMAIL_PASSWORD = " "

msg = EmailMessage()
msg['Subject'] = ' '
msg['From'] = SENDER_EMAIL_ADDRESS
msg['To'] = ' '
msg.set_content('TERRORIST')

f = open("/Users/prituldave/Downloads/11.jpg",'rb')
data = f.read()
name = f.name
f.close()

msg.add_attachment(data,filename=name,maintype='image',subtype=imghdr.what(name))

#setting up the mail server and smtp port number#
with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
	
	#login to account#
	smtp.login(SENDER_EMAIL_ADDRESS,EMAIL_PASSWORD)

	#sending message sender id,receiver id#
	smtp.send_message(msg)

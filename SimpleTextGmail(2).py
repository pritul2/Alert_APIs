'''
1) enable 2 step verification
2) go to enable app password
3) Generate the APP password
'''
import smtplib
import os
from email.message import EmailMessage

#setting the env. variables#
SENDER_EMAIL_ADDRESS = " "
EMAIL_PASSWORD = " "

msg = EmailMessage()
msg['Subject'] = 'Terrorist detected'
msg['From'] = SENDER_EMAIL_ADDRESS
msg['To'] = SENDER_EMAIL_ADDRESS
msg.set_content('your msg')

#setting up the mail server and smtp port number#
with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
	
	#login to account#
	smtp.login(SENDER_EMAIL_ADDRESS,EMAIL_PASSWORD)

	#sending message sender id,receiver id#
	smtp.send_message(msg)

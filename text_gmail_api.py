'''
1) enable 2 step verification
2) go to enable app password
3) Generate the APP password
'''
import smtplib
import os

#setting the env. variables#
SENDER_EMAIL_ADDRESS = "sender address"
EMAIL_PASSWORD = "app password"
RECEIVER_EMAIL_ADDRESS= "receiver address"
#setting up the mail server and smtp port number#
with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:

	#login to account#
	smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

	#defining subject#
	subject = '---subject----'
	#defining body#
	body = '---body part -----'

	#wrapping up#
	msg=f'subject:{subject}\n\nbody:{body}'

	#sending message sender id,receiver id#
	smtp.sendmail(SENDER_EMAIL_ADDRESS,RECEIVER_EMAIL_ADDRESS,msg)

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
with smtplib.SMTP("smtp.gmail.com",587) as smtp:
	smtp.ehlo()#to allow smtp to run at background#
	smtp.starttls()#encrypting the msg#
	smtp.ehlo()

	#login to account#
	smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

	#defining subject#
	subject = 'Terrorist detected'
	#defining body#
	body = 'Terrorist detected at time xyz and number xyz'

	#wrapping up#
	msg=f'subject:{subject}\n\nbody:{body}'

	#sending message sender id,receiver id#
	smtp.sendmail(SENDER_EMAIL_ADDRESS,RECEIVER_EMAIL_ADDRESS,msg)

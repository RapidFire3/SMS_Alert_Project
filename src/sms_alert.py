import time								
import schedule
import os
from twilio.rest import Client

def sendMessage():
	'''
	This function is a job that is responsible for sending a sms message using
	the Twilio Cloud Communications Platform. Will need:
		-TWILIO_ACCOUNT_SID
		-TWILIO_AUTH_TOKEN
		-TWILIO_PHONE_NUMBER
		-RECIPENT(S)_PHONE_NUMBER
	'''

	#	Twilio account sid from environment variable.
	account_sid = os.environ['TWILIO_ACCOUNT_SID']
	
	#	Twilio authentication token from environment varible.
	auth_token	= os.environ['TWILIO_AUTH_TOKEN']
	
	#	Create the client object.
	client		= Client(account_sid, auth_token)

	#	Twilio phone number. Can be obtain from twilio account.
	twilio_number = 'TWILIO_PHONE_NUMBER'

	#	Recipient of the message. 
	recipient = 'RECIPENT(S)_PHONE_NUMBER' 

	#	Create and send the message out.
	message 	= client.messages.create(
					#	Message to send over the medium.
					body="Hello World. This is a Twilio test.",
					
					#	Twilio phone number.
					from_=twilio_number,

					#	Phone number of recipient.
					to=recipient
				)

	#	Status.
	print(message.sid)


#	Scheduled tasks.
schedule.every().day.at("13:00").do(sendMessage)

while True:
	#	Checks if there are any scheduled task.
	schedule.run_pending()
	time.sleep(1)

from twilio.rest import TwilioRestClient

accountid='your id here'
authtoken='token here'

twilioCli = TwilioRestClient(accountid, authtoken)
myTwilioNumber = 'your number here (please add the whole number)'

def bhejo(receiver,text):
	try:
		message = twilioCli.messages.create(body=text, from_=myTwilioNumber, to=receiver)
		info='Message successfully sent'
	except Exception, e:
		info='Error sending message'
	return info
from twilio.rest import Client

account_sid = '***********'
auth_token = '**********'
client = Client(account_sid, auth_token)

def send_message():
  message = client.messages.create(
  from_='whatsapp:+14155238886',
  body="INTRUDER ALERT",
  to='whatsapp:*********'
  )

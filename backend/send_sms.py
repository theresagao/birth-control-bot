from twilio.rest import TwilioRestClient

account_sid = "AC8d460c2afad3a32712fb62230c04107f" # Your Account SID from www.twilio.com/console    
auth_token  = "51f875c833e2054c89744b85e678e25c"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="What would you like?",
    to="+19255231279",    # Replace with your phone number
    #from_="+15005550006")
    from_="+19493972430") # Replace with your Twilio number

print(message.sid)

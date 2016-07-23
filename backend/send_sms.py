from twilio.rest import TwilioRestClient

account_sid = "ACd1a5bc0ab62b14c0f0429e5f2c224a65" # Your Account SID from www.twilio.com/console    
auth_token  = "a77d83bdf3b7b7b7277568c1b7ffd32a"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="What would you like?",
    to="+19492935943",    # Replace with your phone number
    #from_="+15005550006")
    from_="+19493972430") # Replace with your Twilio number

print(message.sid)

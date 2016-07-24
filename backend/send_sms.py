from twilio.rest import TwilioRestClient

account_sid = "{{your_account_sid}}" # Your Account SID from www.twilio.com/console    
auth_token  = "{{your_auth_token}}"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="What would you like?",
    to="+19492935943",    # Replace with your phone number
    #from_="+15005550006")
    from_="+19493972430") # Replace with your Twilio number

print(message.sid)

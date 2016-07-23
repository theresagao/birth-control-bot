from flask import Flask, request, redirect, session
import twilio.twiml

SECRET_KEY = 'NEW SESSION'
app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
  """Respond with the number of text messages sent between two parties."""

  counter = session.get('counter', 0)

  # Save the new counter value in the session
  session['counter'] = counter

  msg_body = request.values.get('Body')

  if msg_body != "Help":
    # increment the counter
    counter += 1
  
  if msg_body == "Help":
    send_help_text()    
  else if msg_body == "Reset":
    session.clear()
    message = "Your session has been reset."
    resp = twilio.twiml.Response()
    resp.sms(message)
    return str(resp)
  else:
    message = "".join(str(counter))
    resp = twilio.twiml.Response()
    resp.sms(message)

    return str(resp)

def init_text():

def send_help_text():



if __name__ == "__main__":
    app.run(debug=True)
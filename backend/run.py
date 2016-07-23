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
  elif msg_body == "Reset":
    reset_counter()
  elif counter == 1:
    init_text()
  elif counter == 2:
    quiz_question_1()
  elif counter == 3:
    quiz_question_2()
  elif counter == 4:
    quiz_question_3()
  elif counter == 5:
    quiz_question_4()
  elif counter == 6:
    quiz_question_5()
  elif counter == 7:
    give_recommendation_and_address()
  else:
    message = "".join(str(counter))
    resp = twilio.twiml.Response()
    resp.sms(message)
    return str(resp)
  #else:
  #  reset_counter()

def reset_counter():
  session.clear()
  message = "Your session has been reset."
  resp = twilio.twiml.Response()
  resp.sms(message)
  return str(resp)

def init_text():
  reset_counter()

def send_help_text():
  reset_counter()
  
if __name__ == "__main__":
    app.run(debug=True)
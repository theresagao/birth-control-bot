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
  msg_body = str(msg_body).lower()

  if msg_body != "help":
    # increment the counter
    counter += 1
  
  response = ""

  if msg_body == "help":
    response = send_help_text()    
  elif msg_body == "reset":
    response = reset_counter()
  elif counter == 1:
    response = init_text()
  elif counter == 2:
    response = quiz_question_1()
  elif counter == 3:
    response = quiz_question_2()
  elif counter == 4:
    response = quiz_question_3()
  elif counter == 5:
    response = quiz_question_4()
  elif counter == 6:
    response = quiz_question_5()
  elif counter == 7:
    response = ask_for_zipcode()
  else:
    response = give_recommendation_and_address()
  return response

def reset_counter():
  session.clear()
  message = "Your session has been reset."
  resp = twilio.twiml.Response()
  resp.sms(message)
  return str(resp)

def init_text():
  message = "Hello! Type 'Find A Location' To find the closest location. Type 'Continue' to determine the best form of birth control."
  resp = twilio.twiml.Response()
  resp.sms(message)
  return str(resp)

def send_help_text():
  message = "To use this bot, type your zip code to find the closest location. Type 'Continue' to determine the best form of birth control."
  resp = twilio.twiml.Response()
  resp.sms(message)
  return str(resp)

def quiz_question_1():
  message = "What blah blha blha."
  resp = twilio.twiml.Response()
  resp.sms(message)
  return str(resp)

def quiz_question_2():
  message = "Blah blah blha"
  resp = twilio.twiml.Response()
  resp.sms(message)
  return str(resp)

def quiz_question_3():
  message = "Blah blah blha"
  resp = twilio.twiml.Response()
  resp.sms(message)
  return str(resp)

def quiz_question_4():
  message = "Blah blah blha"
  resp = twilio.twiml.Response()
  resp.sms(message)
  return str(resp)

def quiz_question_5():
  message = "Blah blah blha"
  resp = twilio.twiml.Response()
  resp.sms(message)
  return str(resp)

def ask_for_zipcode():
  message = "Please type in your zipcode so we can find the closest location to obtain birth control."
  resp = twilio.twiml.Response()
  resp.sms(message)
  return str(resp)

def give_recommendation_and_address():
  message = "blah blha blah"
  resp = twilio.twiml.Response()
  resp.sms(message)
  return str(resp)  

if __name__ == "__main__":
    app.run(debug=True)
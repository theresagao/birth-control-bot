from flask import Flask, request, redirect, session
import twilio.twiml
import re
import requests

SECRET_KEY = 'NEW SESSION'
app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/", methods=['GET', 'POST'])

def hello_monkey():
  counter = session.get('counter', 0)
  options_arr = session.get('options', [
                                        "Birth Control Patch", 
                                        "Depro-Provera (Hormonal Injection)", 
                                        "Birth Control Ring", 
                                        "Condom", 
                                        "Copper IUD", 
                                        "Hormonal IUD",
                                        "Birth Control Pill",
                                        "Tubal Ligation",
                                        "Vasectomy"
                                      ])

  msg_body = request.values.get('Body')
  msg_body = str(msg_body).lower()

  if msg_body != "help me" and msg_body != "find a location" and not msg_body.isdigit():
    counter += 1

  print "Counter: " + str(counter)

  # Save the new counter value in the session
  session['counter'] = counter

  options_arr = eliminate_from_array(counter, options_arr, msg_body)

  session['options'] = options_arr

  response = ""

  if msg_body == "help me":
    response = send_help_text()
  elif msg_body == "reset":
    response = reset_counter()
  elif msg_body == "find a location":
    response = ask_for_zipcode()
  elif msg_body.isdigit():
    print "hi this is a zipcode"
    response = return_closest_center(msg_body)
    print "method finished"
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
    response = quiz_question_6()
  elif counter == 8:
    response = quiz_question_7()        
  elif counter == 9:
    response = quiz_question_8()  
  else:
    response = give_recommendation_and_address(options_arr)
  return response    

def reset_counter():
  session.clear()
  message = "Your session has been reset."
  resp = twilio.twiml.Response()
  resp.sms(message)
  return str(resp)

def init_text():
  message = "Hello! Type 'Find A Location' for the closest location. Type 'Continue' to determine the best form of birth control. Type 'Help me' to see this message again."
  resp = twilio.twiml.Response()
  resp.sms(message)
  return str(resp)

def send_help_text():
  message = "To use this bot, type your zip code to find the closest location. Type 'Continue' to determine the best form of birth control."
  resp = twilio.twiml.Response()
  resp.sms(message)
  return str(resp)

def quiz_question_1():
  message = "Are you male or female? (Ans: m/f)"
  resp = twilio.twiml.Response()
  resp.sms(message)
  return str(resp)

def quiz_question_2():
  message = "Are you ok with a permanent form of contraception? (y/n)"
  resp = twilio.twiml.Response()
  resp.sms(message)
  return str(resp)

def quiz_question_3():
  message = "Are you ok with a hormonal form of contraception? (y/n)"
  resp = twilio.twiml.Response()
  resp.sms(message)
  return str(resp)

def quiz_question_4():
  message = "Are you ok with interrupting sexual activity to use birth control? (y/n)"
  resp = twilio.twiml.Response()
  resp.sms(message)
  return str(resp)

def quiz_question_5():
  message = "Will you be able to remember to take birth control every day? (y/n)"
  resp = twilio.twiml.Response()
  resp.sms(message)
  return str(resp)

def quiz_question_6():
  message = "Will you be able to remember to take birth control every week/month? (y/n)"
  resp = twilio.twiml.Response()
  resp.sms(message)
  return str(resp)

def quiz_question_7():
  message = "Are you ok with receiving birth control in injection form? (y/n)"
  resp = twilio.twiml.Response()
  resp.sms(message)
  return str(resp)

def quiz_question_8():
  message = "Are you ok with birth control increasing your menstrual symptoms? (y/n)"
  resp = twilio.twiml.Response()
  resp.sms(message)
  return str(resp)

def ask_for_zipcode():
  message = "Please type in your zipcode so we can find the closest location to obtain birth control. (#####)"
  resp = twilio.twiml.Response()
  resp.sms(message)
  return str(resp)

def give_recommendation_and_address(options_arr):
  if len(options_arr) == 0:
    message = "Please consult with your doctors for options."
  else:
    message = "Possible forms of birth control are " + ", ".join(options_arr)
  resp = twilio.twiml.Response()
  resp.sms(message)
  session.clear()
  return str(resp)

def eliminate_from_array(counter, options_arr, msg_body):
  if msg_body == "y":
    return options_arr
  elif counter == 3:
    if msg_body == "m":
      options_arr.remove("Tubal Ligation")
      print options_arr
    elif msg_body == "f":
      options_arr.remove("Vasectomy")
      print options_arr  
    print counter  
  elif counter == 4:
    if msg_body == "n":
      if "Tubal Ligation" in options_arr:
        options_arr.remove("Tubal Ligation")
      if "Vasectomy" in options_arr:
        options_arr.remove("Vasectomy")
    print options_arr
    print counter
  elif counter == 5:
    if msg_body == "n":
      options_arr.remove("Depro-Provera (Hormonal Injection)")
      options_arr.remove("Hormonal IUD")      
      options_arr.remove("Birth Control Pill")  
    print options_arr 
    print counter   
  elif counter == 6:
    if msg_body == "n":
      options_arr.remove("Condom")
    print options_arr
    print counter
  elif counter == 7: 
    if msg_body == "n":
      if "Birth Control Pill" in options_arr:
        options_arr.remove("Birth Control Pill")
    print options_arr
    print counter
  elif counter == 8:  
    if msg_body == "n":
      options_arr.remove("Birth Control Patch")
      options_arr.remove("Birth Control Ring")
    print options_arr
    print counter
  elif counter == 9:  
    if msg_body == "n":
      if "Depro-Provera (Hormonal Injection)" in options_arr:
        options_arr.remove("Depro-Provera (Hormonal Injection)")
    print options_arr
    print counter
  elif counter == 10:
    if msg_body == "n":
      options_arr.remove("Copper IUD")
    print options_arr
    print counter

  return options_arr  

def return_closest_center(zipcode):
  r = requests.get("https://www.plannedparenthood.org/health-center/all/all/"+str(zipcode))
  #print(urllib2.urlopen("https://www.plannedparenthood.org/health-center/all/all/94582").read()) 
  center = ""
  #with r.content.split("\n") as i:
  for line in  r.content.split("\n"):
    addr_m = re.match(r'.*center_address">(.*)</.*', line)
    city_m = re.match(r'.*center_city">(.*)</.*', line)
    state_m = re.match(r'.*center_state_abbr">(.*)</.*', line)
    zip_m = re.match(r'.*center_zip">(.*)</.*', line)
    if addr_m:
      addr = addr_m.group(1)
      center = addr
    if city_m: 
      city = city_m.group(1)
      center += ", " + city
    if state_m:
      state = state_m.group(1)
      center += ", " + state
    if zip_m:
      zipcode = zip_m.group(1)
      center += ", " + zipcode + " is the closest Planned Parenthood location."
  
      resp = twilio.twiml.Response()
      resp.sms(center)
      return str(resp)
      break      

#LOL @ hackathon code :P
if __name__ == "__main__":
    app.run(debug=True)
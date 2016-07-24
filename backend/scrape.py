import re
import requests

user_zipcode = input("What's your zipcode?")


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
			print addr
		if city_m: 
			city = city_m.group(1)
			center += ", " + city
			print city
		if state_m:
			state = state_m.group(1)
			center += ", " + state
			print state
		if zip_m:
			zipcode = zip_m.group(1)
			center += ", " + zipcode 
			print zipcode
			return center
			break

return_closest_center(user_zipcode)
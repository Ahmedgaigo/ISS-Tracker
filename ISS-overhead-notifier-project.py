import requests
from datetime import datetime as dt
import smtplib
import time

MY_LAT = 40.343990
MY_LNG = -74.651451

EMAIL = "appbreweryinfo@gmail.com"
PASSWORD = "abcd1234()"
RECEIVER = "gaigoaan@gmail.com"

parameters = {
	'lat': MY_LAT,
	'lng': MY_LNG,
	'formatted': 0
}

sunset_api = 'https://api.sunrise-sunset.org/json'
iss_api = 'http://api.open-notify.org/iss-now.json'


def iss_is_close_to_my_location():
	iss_response = requests.get(url=iss_api)
	iss_response.raise_for_status()
	iss_data = iss_response.json()
	lng = float(iss_data['iss_position']['longitude'])
	lat = float(iss_data['iss_position']['latitude'])
	return lng - 5 >= MY_LNG <= lng + 5 and lat - 5 <= lat or MY_LAT <= lat + 5


def its_dark():
	response = requests.get(url=sunset_api, params=parameters)
	response.raise_for_status()
	data = response.json()

	sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
	sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

	# getting the hour
	time_now = dt.now().hour
	return sunset <= time_now <= sunrise


while True:
	time.sleep(60)
	if iss_is_close_to_my_location() and its_dark():
		with smtplib.SMTP("smtp.gmail.com") as connection:
			# to encrypt our email so that it can't be read by someone intercepting it
			connection.starttls()
			# login
			connection.login(EMAIL, PASSWORD)
			# send email
			connection.sendmail(EMAIL, RECEIVER, f"Subject:LOOK UP!\n\nThe ISS is moving over your location")

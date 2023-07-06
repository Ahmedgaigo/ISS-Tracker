# ISS-Overhead-Notification
ISS Tracker - Get Notified When the International Space Station Passes Over Your Location

The ISS Tracker is a Python script that allows you to receive an email notification whenever the International Space Station (ISS) is passing over your location during nighttime. By utilizing APIs and data on the ISS's location and sunrise/sunset times, the script continuously checks if the ISS is close to your coordinates and if it is currently dark outside.

Features:

1. Automatic Tracking: The script periodically checks the ISS's current location using the Open Notify API and compares it to your specified coordinates. It also retrieves the sunrise and sunset times for your location using the Sunrise-Sunset API.

2. Location-Based Alert: When the ISS is close to your location and it is nighttime, the script sends an email notification to your specified email address. The email subject is "LOOK UP!" to grab your attention, and the body of the email informs you that the ISS is moving over your location.

3. Email Authentication: To ensure secure communication, the script uses the SMTP library to establish a secure connection with Gmail's SMTP server. It encrypts the email communication using TLS (Transport Layer Security) and requires authentication with your Gmail account credentials.

4. Continuous Monitoring: The script runs indefinitely, continuously checking the ISS's location and the time of day. It pauses for 60 seconds between each check to avoid excessive API requests.

How to Use:

1. Set Your Location: Update the `MY_LAT` and `MY_LNG` variables with your latitude and longitude coordinates.

2. Email Configuration: Enter your Gmail email address, password, and the email address where you want to receive the notifications (as `EMAIL`, `PASSWORD`, and `RECEIVER`, respectively).

3. Run the Script: Execute the `main.py` script and keep it running in the background. You will receive an email notification whenever the ISS is passing over your location during nighttime.

Note: Make sure you have the required dependencies installed (`requests`, `datetime`, `smtplib`), and enable less secure apps access in your Gmail account settings to allow the script to send emails.

Experience the awe-inspiring presence of the ISS passing overhead with the ISS Tracker. Stay informed and never miss a chance to witness this incredible feat of human engineering and exploration!

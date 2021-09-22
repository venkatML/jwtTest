import datetime
import time
import jwt
import re


ssl_private_key_path = 'jwtTest_private.pem'
ssl_algorithm = 'RS256'
root_cert_filepath = 'jwtTest_cert.pem'
project_id = 'iot-registry'
gcp_location = 'us-west1'
registry_id = 'iot-registry'
device_id = 'rpi15'


time = datetime.datetime.now()

def create_jwt():
	token = {'iat': time,
		 'exp': time + datetime.timedelta(minutes=60),
		 'aud': project_id
	}

	with open(ssl_private_key_path, 'r') as f:
		private_key = f.read()
	return jwt.encode(token, private_key, ssl_algorithm)

print (create_jwt())

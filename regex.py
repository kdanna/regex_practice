import os, re, csv

# get current dir of script
dir = os.getcwd()  

# get current_files in dir
current_files = os.listdir(dir)
email_messages = [email for email in current_files if email.endswith('.msg')]


#regex
regex_to_email = re.compile(r'X-Original-To:\s([\w\d\.-]+@[\w\d\.-]+)')
regex_from_email = re.compile(r'From:\s*(\"\w*\s\w*\"\s)<([\w\d\.-]+@[\w\d\.-]+)')
regex_subject = re.compile('(?m)^Subject: (.+)$')

#loop through current file list & perform actions
for email in email_messages:
		open_file = open(email)
		email_data = open_file.read()
		open_file.close()

		to_email_addresses = re.search(regex_to_email, email_data)
		if to_email_addresses:
			print(to_email_addresses.group(1))
	

		from_email_addresses = re.search(regex_from_email, email_data)
		if from_email_addresses:
			print(from_email_addresses.group(2))

		subjects = re.findall(regex_subject, email_data)
		if subjects:
			print(subjects)
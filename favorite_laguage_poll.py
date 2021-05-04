# This program shows how to loop in dictionary using for-loop and check if there are any else without participating in polling.
users = ['ajay','basha','yuva','ravi','jyothi','anil','haritha']
language_polling = {'ajay':'python','anil':'java','jyothi':'c','yuva':'html','ravi':'java script'}
for user in users:
	if user in language_polling.keys():
		print(f"Thankyou {user.title()} for actively participaing in poll.\n")
	else:
		print(f"Hi {user.title()}, please participate in language polling.\n")

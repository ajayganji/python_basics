current_users = ['Yuva','Ravi','basha','Sahil','Lakshman']
new_users = ['sahil','ravi','aravind','pankaj','santosh']
existing_users = [value.lower() for value in current_users]
for new_user in new_users:
	if new_user.lower() in existing_users:
		print("user name had already taken, enter a new user name")
	else:
		print("user name available")

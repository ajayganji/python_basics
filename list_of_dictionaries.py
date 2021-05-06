# This program shows how to loop through list of dictionaries.

yuva = {'first':'yuva','last':'rajesh','age':26,'location':'kakinada'}
ravi = {'first':'ravi','last':'teja','age':27,'location':'kakinada'}
basha = {'first':'basha','last':'rabbani','age':28,'location':'pithapuram'}
users = [yuva,ravi,basha]
print("The details of the users logged in are: \n")
for user in users:
	full_name = f"{user['first']} {user['last']}"
	age = f"{user['age']}"
	location = f"{user['location']}"
	print( f"\tUser Full Name : {full_name.title()}\n"
		f"\tAge : {user['age']}\n"
		f"\tLocation : {user['location']}\n")
favorite_places = {
	'ajay':['nandi hills','leh','ooty'],
	'yuva':['araku','vizag','rampachodavaram'],
	'ravi':['house','msn chartece','beach'],
	}
for person,locations in favorite_places.items():
	print(f"The favorite places of {person.title()} are:")
	for location in locations:
		print(f"\t{location.title()}")
	print("")
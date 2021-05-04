major_rivers = {
	'nile':'africa',
	'amazon':'south america',
	'mississippi':'north america',
	'chang-jiang':'china'
	}
for river,origin in major_rivers.items():
	print(f"The {river.title()} river is in {origin.title()}.")

print("\nThe river names given in the list are :")
for river in major_rivers.keys():
	print(f"\t{river.title()}")

print("\nThe countries in which the rivers are in :")
for country in major_rivers.values():
	print(f"\t{country.title()}")
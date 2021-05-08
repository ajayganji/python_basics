cities = {
		'hyderabad':
			{
			'country':'india',
			'population':'68 lakhs',
			'fact':'the "kohinoor" originated here',
			},
		'new york':
			{
			'country':'USA',
			'population':'84 lakhs',
			'fact':'new york city has the largest gold storage in the world',
			}
		}	
for city,city_info in cities.items():
	
	country = city_info['country']
	population = city_info['population']
	fact = city_info['fact']

	print(f"The selected city is: {city.title()}")
	print (f"Country = {country}\n"
			f"Population = {population}\n"
			f"Fact: {fact}"
			)
	print()
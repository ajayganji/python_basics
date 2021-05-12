
def artist_info(artist_name,song_name,album_name=None,):
	if album_name:
		info = {'name':artist_name.title(),'song':song_name,'album':album_name.title(),}
	else:
		info = {'name':artist_name.title(),'song':song_name,}
	return info



while True:
	prompt = "This is a program to know details about your favorite music artist.\nYou can exit by typing 'q' at any point of this program."
	print(prompt)
	artist_name = input("Who is your favorite music artist?  ")
	if artist_name == 'q':
		print("YOU QUIT")
		break
	song_name = input(f"Enter your favorite song from {artist_name}: ")
	if song_name == 'q':
		print("YOU QUIT")
		break
	album_name = input(f"Which album does '{song_name}' song belongs to: ")
	if album_name == 'q':
		print("YOU QUIT")
		break
	music_artist_poll = artist_info(artist_name,song_name,album_name)
	print(music_artist_poll)
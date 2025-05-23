def make_album(artist, title, num_songs=None):
    album = {
        'artist': artist,
        'title': title
    }
    if num_songs is not None:
        album['songs'] = num_songs
    return album

while True:
    artist = input("Artist name: ")
    if artist == 'quit':
        break

    title = input("Album title: ")
    if title == 'quit':
        break

    if num_songs == 'quit':
        break
    elif num_songs == '':
        album = make_album(artist, title)
    else:
        album = make_album(artist, title, int(num_songs))

    print("Album created:", album)
    

def make_album(artist,title,num_songs=None):
    info = {
        'artist_name':artist, 
        'album_title' :title
        }
    if num_songs is not None:
     info['track_no']=num_songs
    return info

while True:
    artist = input("Enter artist's name: ")
    if artist == 'quit':
        break

    title = input("Enter title  name: ")
    if title == 'quit':
        break

    if num_songs == 'quit':
        break
    elif num_songs == '':
        info = make_album(artist, title)
    else:
        info = make_album(artist, title, int(num_songs))

    print(info)
    

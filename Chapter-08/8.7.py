def make_album(artist,title,num_songs=None):
    info = {
        'artist_name':artist, 
        'album_title' :title
        }
    if num_songs is not None:
     info['track_no']=num_songs
    return info

   
information1= make_album('Jin','Echo')
information2= make_album('Jungkook','Golden','8')
information3= make_album('V','Layover')
print(information1)
print(information2)
print(information3)
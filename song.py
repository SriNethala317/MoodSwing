
from typing import Any


class Song:
    def __init__(self, name, artist="test", image_url="test", extension="test") -> None:
        self.song_info ={"name" : name, "artist": artist, "image_url": image_url, "filename": name.replace(" ", "_") + "." + extension, "extension": extension, "played" : False, "length": 0}

    def __str__(self) -> str:
        return str(self.song_info)
    
    def __repr__(self) -> str:
        return str(self.song_info)
    
    def get_song_info(self):
        return self.song_info
    
    def get_name(self):
        return self.song_info['name']
    
    def get_artist(self):
        return self.song_info['artist']
    
    def get_length(self):
        return self.song_info['length']
    
    def get_extension(self):
        return self.song_info['extension']
    
    def get_image(self):
        print(self.song_info['image_url'])
        # return self.song_info['image_url']
    
    def get_filename(self):
        return self.song_info['filename']
    
    def set_extension(self, extension):
        self.song_info['extension'] = extension
    
    def set_length(self, length):
        self.song_info['length'] = length
    
    def set_filename(self, filename):
        self.song_info['filename'] = filename
    
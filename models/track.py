class Track:
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist
        print('a new song for', self.artist.name, 'has created')
    
    def play(self):
        print(self.name, 'Played')
        self.artist.counter += 1
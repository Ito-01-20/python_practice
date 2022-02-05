class Artist:
    def __init__(self, artist_name, track_number, debut_year):
        self.artist_name = artist_name
        self.track_number = track_number
        self.debut_year = debut_year


king_gun = Artist("King_Gnu", 10, 2018)
vaundy = Artist("Vaundy", 10, 2019)

print(vaundy.debut_year)
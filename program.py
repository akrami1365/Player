from models.artist import Artist
from models.track import Track

mohsenChavoshi = Artist("Mohsen Chavoshi")
mohammadIsfehani = Artist("Mohammad Isfehani")

track1 = Track('Amir bi ghazand', mohsenChavoshi)
track2 = Track('Dalghak', mohammadIsfehani)
track1.play()
track1.play()
track1.play()
track1.play()
track2.play()

print(mohsenChavoshi.name, 'Have',mohsenChavoshi.counter)
print(mohammadIsfehani.name, 'Have',mohammadIsfehani.counter)
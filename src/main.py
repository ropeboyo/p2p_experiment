import clientside as cs
import serverside as ss
import threading
import csv

serverside = threading.Thread(target=ss.ServerSide, args=("127.0.0.1", 6789))
clientside = threading.Thread(target=cs.ClientSide, args=("127.0.0.1", 6789))

dict = [
    {'title': 'Joker', 'year': 2019, 'rating': 5, 'comment': 'HONK HONK'},
    {'title': 'Captain Marvel', 'year': 2017, 'rating': 2, 'comment': 'The porn parody is better tbhngl'},
    {'title': 'Ghostbusters', 'year': 2016, 'rating': 1, 'comment': 'goo poo pee pee'}    
]

fields = ['title', 'year', 'rating', 'comment']

filename = "my_ratings.csv"

with open(filename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(dict)


serverside.start()
clientside.start()



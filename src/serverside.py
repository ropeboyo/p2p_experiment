import csv
import socket


class ServerSide:
    def __init__(self, address, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((address, port))
        self.server.listen(1)
        self.server.setblocking(1)
        print("[SERVER] - Server side is up")
        self.running(False)

    def running(self, end):
        while not end:
            cs, ca = self.server.accept()
            cs.setblocking(1)
            print("[SERVER] - Received connection from ", str(ca))
            
            query = cs.recv(256).decode("utf-8")
            if not query: continue

            result = self.search_ratings(query)
            cs.send(result.encode("utf-8"))
            cs.close()

        self.server.close()

    def search_ratings(self, query):
        with open("my_ratings.csv", 'rt', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            c1, c2, c3, c4 = reader.fieldnames
            result = ''

            for row in reader:
                if row[c1] == query:
                    result = row[c1] + " - " + row[c2] + " - " + row[c3] + " - " + row[c4]

        if result == '':
            result = 'TITLE_NOT_FOUND'
        
        return result

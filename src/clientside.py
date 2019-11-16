import socket


class ClientSide:
    def __init__(self, address, port):
        print("[CLIENT] - Client side is up")
        self.running(False, address, port)

    def running(self, end, address, port):
        while not end:
            self.query_network(address, port)

            opt = input("[CLIENT] - Another query?(Y/n)").lower()
            if opt == 'y' or opt == '':
                pass
            else:
                end = True
                print("[CLIENT] - Closing client side...")

        self.client.close()

    def query_network(self, address, port):
        query = input("[CLIENT] - Name a movie")
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(("HARD CODE IP FOR NOW", port))
        self.client.send(query.encode("utf-8"))
        result = self.client.recv(2048).decode("utf-8")
        print("[CLIENT] - ", result)

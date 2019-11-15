class ServerSide:
    def __init__(self, address, port):
        import socket

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
        result = "HIT BOYO"
        return result

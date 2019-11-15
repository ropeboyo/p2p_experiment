class ClientSide:
    def __init__(self, address, port):
        import socket

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((address, port))
        print("Client side is up")
        self.running(False)

    def running(self, end):
        while not end:
            greet = self.client.recv(64)
            greet = greet.decode("utf-8")

            print(greet)
            end = True
            print("ending client_side")

        self.client.close()

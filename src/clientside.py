class ClientSide:
    def __init__(self, address, port):
        import socket

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(("127.0.0.1", 6789))
        
        print("[CLIENT] - Client side is up")
        self.running(False)

    def running(self, end):
        while not end:
            self.query_network()

            opt = input("[CLIENT] - Another query?(Y/n)").lower()
            if opt == 'y' or opt == '': pass
            else:
                end = True
                print("[CLIENT] - Closing client side...")

        self.client.close()

    def query_network(self):
        query = input("[CLIENT] - Name a movie")
       
        # try:
        
        self.client.send(query.encode("utf-8"))
        result = self.client.recv(2048).decode("utf-8")
        print("[CLIENT] - ", result)   
        # except OSError:
        #     print("OSERROR")
        # except BrokenPipeError:
        #     print("Pipe's broken fam")
        # finally:
        #     self.client.close()
        

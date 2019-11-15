class ServerSide:
    def __init__(self, address, port):
        import socket
        import threading

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((address, port))
        self.server.listen(16)
        print("Server side is up")
        while True:
            cs, ca = self.server.accept()
            cthread = threading.Thread(target=self.running, args=(False, cs, ca))
            cthread.daemon = True
            cthread.start()

    def running(self, end, cs, ca):
        while not end:
            print("Received connection from ".format(ca))
            cs.send(bytes("HENLO" + str(cs), "utf-8"))

            print("ok")
            end = True
            print("ending...")

        self.server.close()

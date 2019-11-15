import clientside as cs
import serverside as ss
import threading


serverside = threading.Thread(target=ss.ServerSide, args=("127.0.0.1", 6789))
clientside = threading.Thread(target=cs.ClientSide, args=("127.0.0.1", 6789))


print("ddd")
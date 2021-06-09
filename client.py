#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://163.239.28.25:5000")

print(f"Sending request …")
socket.send_string("")

#  Get the reply.
while True:
    message = socket.recv()
    print(message)

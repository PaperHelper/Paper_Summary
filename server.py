#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq
from paper_summarization import main

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5000")

while True:
    #  Wait for next request from client
    message = socket.recv()
    print(f"Received request: {message}")

    #  Do some 'work'
    time.sleep(1)

    summary = main('Periapical Status Related to the Quality of Coronal.pdf')

    #  Send reply back to client
    socket.send_string(summary)
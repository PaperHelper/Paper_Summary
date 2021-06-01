import time
import zmq
from paper_summarization import main
from data_crawler import get_top_10_papers,get_
import os
import json

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5000")

while True:
    #  Wait for next request from client
    #  message format: 'field'\t'field'\t...
    message = socket.recv()
    print(f"Received request: {message}")

    fields = message.split('\t')

    if os.path.exists('./summary_data_ready.json'):
        with open('./summary_data_ready.json') as f:
            summary_data = json.load(f)

        for k in list(summary_data.keys())[:3]:
            data = summary_data[k]
            send_msg = f'{data['title']}\t{data['authors']}\t{data['publication']\t{data['year']}'
            socket.send_string(send_msg)
    else:
        wait_flag = True
        socket.send_string('Initializing... Please Wait.')

    papers = get_top_10_papers(fields)
    get_files(papers)
    main(papers)

    #  Do some 'work'
    time.sleep(1)

    summary = main('Conformer.pdf')

    #  Send reply back to client
    socket.send_string(summary)

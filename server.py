import time
import zmq
from paper_summarization import main
from data_crawling import get_top_10_papers,get_files,get_random_papers
import os
import json

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5000")

def send_summary(socket,fields):
    count = 0

    with open('./summary_data_ready.json') as f:
        summary_data = json.load(f)

    send_msg = ''

    with open('./served_papers_list.txt','a') as f:
        for k in list(summary_data.keys()):
            if count == 3:
                break
            if fields[0] != '':
                if len(set(summary_data[k][tags]) & set(fields)) == 0:
                    continue
            f.write(k+'\n')
            count += 1
            data = summary_data[k]
            #send_msg = f'{data["title"]} {", ".join(data["authors"])} {data["publication"]} {data["year"]}'
            send_msg += ' '+ data['title']
    
    socket.send_string(send_msg)


message = socket.recv()
print(f"Received request: {message}")

fields = message.decode('utf-8').split('\t')

if os.path.exists('./summary_data_ready.json'):
    send_summary(socket,fields)
else:
    wait_flag = True

if len(message) == 0:
    papers = get_random_papers()
else:
    papers = get_top_10_papers(fields)
    
# download papers for summarization
get_files(papers)

# summarize given(downloaded) papers
main(papers)

if wait_flag == True:
    send_summary(socket,fields)


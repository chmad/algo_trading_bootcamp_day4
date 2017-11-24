#
# Simple Tick Data Client with ZeroMQ
#
import zmq
import datetime

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://127.0.0.1:5555')

socket.setsockopt_string(zmq.SUBSCRIBE, 'AAPL')

while True:
    msg = socket.recv_string()
    t = datetime.datetime.now()
    print('%s | ' % str(t), msg)

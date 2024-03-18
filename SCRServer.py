import socket
import pyaudio
from art import tprint
tprint('SCR Server')
print('GitHub > https://github.com/ErkinKraft')

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

portint = int(input('Port> '))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', portint))
server.listen(5)

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK)

while True:
    client, addr = server.accept()
    print(f"Connection from {addr} has been established.")
    data = client.recv(1024)
    while data:
        stream.write(data)
        data = client.recv(1024)

    client.close()

stream.stop_stream()
stream.close()
p.terminate()

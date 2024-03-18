import socket
import pyaudio
from art import tprint
tprint('SCR Client')
print('GitHub > https://github.com/ErkinKraft')
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100


ipadres = input('IP> ')
portint = int(input('Port> '))
while True:
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ipadres, portint))
    except(ConnectionRefusedError):
        print('Error connection')
    else:
        print(f'Connected successfully CHA{CHANNELS}, CHU{CHUNK}, FOR{FORMAT}, IP{ipadres}, PORT{portint}')
        break

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

while True:
    data = stream.read(CHUNK)
    client.sendall(data)

stream.stop_stream()
stream.close()
p.terminate()
client.close()

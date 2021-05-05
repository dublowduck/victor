import time
import serial
from mycroft_bus_client import MessageBusClient, Message

#set up the 
ser = serial.Serial('/dev/ttyACM0', baudrate= 9600, timeout=1)

print('Setting up client to connect to a local mycroft instance')
client = MessageBusClient()

def print_utterance(message):
    victor_response = (format(message.data.get('utterance')))
    #print(format(message.data.get('utterance')))
    print (victor_response)
    ser.write(victor_response.encode())

print('Registering handler for speak message...')
client.on('speak', print_utterance)

client.run_forever()

##########

#while True:
    #user_input = input("Say something:")
    #time.sleep(1)
    #ser.write(victor_response.encode())

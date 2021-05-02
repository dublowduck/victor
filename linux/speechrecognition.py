# NOTE: this example requires PyAudio because it uses the Microphone class
from mycroft_bus_client import MessageBusClient, Message #import the mycroft message bus libary
import speech_recognition as sr #import the speech recognition libary for "hey victor"
import time

#establish comunication with mycroft
print('Setting up client to connect to a local mycroft instance')
client = MessageBusClient()
client.run_in_thread()

#set the speach to text variable to 0 and then print it
stt_state = 0
print(stt_state)

#forever loop
while True: 
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # listen for 1 second to calibrate the energy threshold for ambient noise levels
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
       
       #send text to google
        text = r.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + text)
        stt_state = 1
        print(stt_state)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        print(stt_state)
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))
        print(stt_state)

#if returned stt from google is any of the wakewords, send a listen command to mycroft.
    if stt_state == 1:
        if text == "Victor":
            print("Sending wake work comand")
            client.emit(Message('mycroft.mic.listen'))
        elif text == "victor":
            print("Sending wake work comand")
            client.emit(Message('mycroft.mic.listen'))
    
        elif text == "Hey Victor":
            print("Sending wake work comand")
            client.emit(Message('mycroft.mic.listen'))
        elif text == "hey Victor":
            print("Sending wake work comand")
            client.emit(Message('mycroft.mic.listen'))
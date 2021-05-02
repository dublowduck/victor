#Import the requirered modules
import os
import time

#Tell the user what you are doing
print("Imported modules")
time.sleep(0.5)
print("Running start-up script")
time.sleep(0.5)
print("Starting Speech Recognition")
#run the speech script for "hey victor"
os.system("python3 speechrecognition.py")
time.sleep(1)
print("Starting Mycroft...")
time.sleep(1)

#Clear the screen and start Mycroft
os.system("clear")
os.system("bash /home/rupert/mycroft-core/start-mycroft.sh debug")

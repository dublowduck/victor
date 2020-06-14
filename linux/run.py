#Import the requirered modules
import os
import time
import webbrowser

#Tell the user what you are doing
print("Imported modules")
time.sleep(0.5)
print("Running start-up script")
time.sleep(0.5)
print("Starting Mycroft...")
time.sleep(1)

#Clear the screen and start Mycroft
os.system("clear")
os.system("bash /home/rupert/mycroft-core/start-mycroft.sh debug")

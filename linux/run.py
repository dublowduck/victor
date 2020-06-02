#Import the requirered modules
import os
import time
import webbrowser

print("Imported modules")
time.sleep(0.5)
print("Running start-up script")
time.sleep(0.5)
print("Starting Mycroft...")
time.sleep(1)

os.system("clear")
os.system("bash /home/rupert/mycroft-core/start-mycroft.sh debug")

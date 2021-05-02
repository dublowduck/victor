#Import the requirered modules
import os
import time
import webbrowser

#Tell the user what you are doing
print("Imported modules")
time.sleep(0.5)
#ask the user to run sr.py
print("----------")
print("Run sr.py in a new terminal")
print("----------")
time.sleep(3)
input("Press Enter to continue...")
time.sleep(0.5)
print("Starting Mycroft...")
time.sleep(1)

#Clear the screen and start Mycroft
os.system("clear")
os.system("bash /home/rupert/mycroft-core/start-mycroft.sh debug")

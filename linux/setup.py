#Import the requirered modules
import os
import time
import webbrowser

#clear the screen
os.system("clear")

#Explain whats going on
print("Welcome to the Victor Project")
time.sleep(3)
print("This script will set up everything you need")
time.sleep(3)

#ask if they are using gnome
if input("Are you using Gnome?:") == "y":
    #Change some Gnome settings
    print("Gnome settings:")
    #ask if they want to disable the lock screen
    if input("Do you want to disable the lock screen?:") == "y":
        os.system("gsettings set org.gnome.desktop.screensaver lock-enabled false")

    #ask if they want Gnome dark mode
    if input("Do you want to use Gnome dark mode?:") == "y":
        os.system("gsettings set org.gnome.desktop.interface gtk-theme 'Yaru-dark'")

#Install recomended packeges
print("Installing recomended packeges:")
#Ask if they want to install net tools
if input("Do you want to install net tools? (Yes if unsure):") == "y":
    print("Installing net tools")
    os.system("sudo apt install net-tools")
    print("Done")

#Ask if they want to install openssh-server
if input("Do you want to install openssh-server?:") == "y":
    print("Installing openssh-server")
    os.system("sudo apt-get install openssh-server")
    print("Done")

time.sleep(3)
print("Installing programs")
time.sleep(3)
#Tell them to install Mycroft
print("Now you need to install Mycroft")
time.sleep(3)

#Clone the repo
path  = "/home/rupert/" 
clone = "git clone https://github.com/MycroftAI/mycroft-core.git" 
os.chdir(path) # Specifying the path where the cloned project needs to be copied
os.system(clone) # Cloning
os.system("bash /home/rupert/mycroft-core/dev_setup.sh") # Run the setup file

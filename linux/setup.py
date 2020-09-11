#Import the requirered modules
import os
import time
import webbrowser

#clear the screen
os.system("clear")

#Explain whats going on
print("=============================")
print("Welcome to the Victor Project")
print("=============================")
time.sleep(3)
print("This script will set up everything you need")
time.sleep(3)

#update the system first
print("The first thing you need to do is update and upgrade your system")
if input("Do you want to do this?:") == "y":
    os.system("sudo apt-get update")
    print("And the fun one")
    os.system("sudo apt-get upgrade")
    print("There, much better")
time.sleep(2)

#ask if they are using gnome
if input("Are you using Gnome?:") == "y":
    #Change some Gnome settings
    print("Gnome settings:")
    #ask if they want to disable the lock screen
    if input("Do you want to disable the lock screen?:") == "y":
        os.system("gsettings set org.gnome.desktop.screensaver lock-enabled false")

    #ask if they want Gnome dark mode
    if input("Do you want to use Gnome dark mode (Yaru-dark) ?:") == "y":
        os.system("gsettings set org.gnome.desktop.interface gtk-theme 'Yaru-dark'")

#Install recomended packeges
print("Installing recomended packeges:")
print("-------------------")
print("Recomended packeges")
print("-------------------")

print("If unsure, say yes")
#Ask if they want to install net tools
if input("Do you want to install net-tools?:") == "y":
    print("Installing net tools")
    os.system("sudo apt install net-tools")
    print("Done")

#Ask if they want to install openssh-server
if input("Do you want to install openssh-server?:") == "y":
    print("Installing openssh-server")
    os.system("sudo apt-get install openssh-server")
    print("Done")

#Ask if they want to install neofetch
if input("Do you want to install neofetch?:") == "y":
    print("Installing neofetch")
    os.system("sudo apt-get install neofetch")
    print("Done")

time.sleep(3)
print("\n")
print("Installing programs")
time.sleep(3)
#Tell them to install Mycroft
print("Now you need to install Mycroft")
a3 = input("Confirm installing Mycroft (if you don`t victor probably won`t work):")
if a3 == "y":
    #Clone the repo
    path  = "/home/rupert/" 
    clone = "git clone https://github.com/MycroftAI/mycroft-core.git" 
    os.chdir(path) # Specifying the path where the cloned project needs to be copied
    os.system(clone) # Cloning
    os.system("bash /home/rupert/mycroft-core/dev_setup.sh") # Run the setup file
    time.sleep(3)

#Customization
print("And relax")
time.sleep(3)
print("That was the hardest bit")
time.sleep(2)
print("Now for the customization:")
os.system("clear")

print("-------------")
print("Customization")
print("-------------")

os.system("neofetch")
time.sleep(1)
print("This is Victor's new home, and your computers specs")
print("Pay close attention to the Terminal")
print("You can run Mycroft, and by extension the victor run file, from theoretically any terminal. This will dictate the look and feel of Victor. You can use your system default terminal emulator or one of our recommendations like cool-retro-term for an old fashioned vintage feel, eDEX-UI for more of a sci-fi look or Konsole for a simple minimalist experience")
time.sleep(4)
print("\n")

#Ask what terminal they want and then install it
a1 = input("Which terminal emulator do you want to use?:\nR)ecomended\nS)ystem default:")
if a1 == "s":
    print("\n")
    print("Ok. Victor will keep using the system default terminal emulator")
elif a1 == "r":
    print("\n")
    a2 = input("Please pick a terminal to install:\nC)ool-retro-term\nE)dex-ui\nK)onsole:")
    if a2 == "c":
        print("\n")
        print("Installing cool-retro-term...")
        os.system("sudo add-apt-repository ppa:vantuz/cool-retro-term")
        os.system("sudo apt-get update")
        os.system("sudo apt-get install cool-retro-term")
        time.sleep(2)
        print("\n")
        print("Done")
        print("cool-retro-term installed")
    elif a2 == "e":
        print("\n")
        print("Installing eDEX-UI...")
        time.sleep(2)
        print("Ok, so you have to be a bit proactive with this one")
        time.sleep(3)
        print("Open this with AppImageLauncher and install it that way, I`ll wait for you")
        time.sleep(6)
        webbrowser.open_new_tab("https://github.com/GitSquared/edex-ui/releases/download/v2.2.2/eDEX-UI.Linux.x86_64.AppImage")
        
        if input("Press enter to continue...") == "hello there":
            print("General Kenobi")
        
        print("\n")
        print("Ok then")
        print("eDEX-UI installed")
    elif a2 == "k":
        print("\n")
        print("Installing Konsole...")
        os.system("sudo apt-get install konsole")
        time.sleep(2)
        print("\n")
        print("Done")
        print("Konsole installed")

#ending bit thing

print("\n")
print("-------")
print("The end")
print("-------")
time.sleep(3)

print("\n")
print("You have successfully installed Victor and all the packages and the components that make it work")
time.sleep(4)
print("\n")
print("Well done. To use Victor open the Terminal that you downloaded and cd to the folder that this script is in and run the run.py python file")
time.sleep(3)
print("Bye bye")
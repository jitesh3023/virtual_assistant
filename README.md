<<<<<<< HEAD
# Virtual assitant for shell command

## Description
This project is an virtual assistant for shell commands. Basic commands like change directory, list directory, moving and renaming folders can be run using speech like alexa. 

## Requirements

To use all of the functionality of the library, you should have:
- Python : The first software requirement is Python 2.6, 2.7, or Python 3.3+. This is required to use the library.
- PyAudio 0.2.11+ (required only if you need to use microphone input, Microphone)
- pyttsx3 module 
- speech_recognition module 
- touch module 
=======
# virtual assitant

## Description
This project is a virtual assistant for shell commands. Basic commands like change directory, list directory, moving and renaming folders can be run using speech like alexa. 

## Requirements

- python (3.6.7) on ubuntu (18.04)
- touch==2020.12.3
- datetime==4.3
- pyttsx3==2.90
- PyAudio==0.2.11
- SpeechRecognition==3.8.1

## Installation
Part 1

clone the repository
- git clone _todo_add_the_link
- cd virtual_assistant
- sudo chmod +x install.sh
- bash install.sh 

If all the commands run without any error , then proceed ahead else try to manually run all the commands inside install.sh and install the required packages

Part 2
- gedit ~/.bashrc

At the end of the file, add the line below
- alias OKLINUX="python3 ~/virtual_assistant/main.py"
- source ~/.bashrc

The installation is complete and the assistant can be tested by using the following command :  

- OKLINUX
>>>>>>> 6d834e3aab0e7434cd214916e81d306680655991

## Commands
### command - trigger word 

- **pwd** - print current directory  
- **ls -l** - list  
- **dir** - available directories   
- **cd 'directory name'**- change directory  
- **mkdir** - make directory  
- **touch** - create file   
- **rm** - remove file   
- **rmdir** - remove directory   
- **cp** - copy   
- **mv** - move 
- **sudo apt update** - update   
- **cd** - go to home directory 

## Testing 
<<<<<<< HEAD


=======
>>>>>>> 6d834e3aab0e7434cd214916e81d306680655991

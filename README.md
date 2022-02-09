# virtual assistant

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
- **executable** - makes file executable
- **locate** - gives the location of a file
- **open google** - opens google


 



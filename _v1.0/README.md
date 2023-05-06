# v1.0

First attempt to develop my personal assistant. It consists of one python file with various packages and function calls. Google Speech Recognition and Microsoft Speech APIs are used for its STT (speech_recognition) & TTS (sapi5).

A **virtual audio cable** is used to allow multiple I/O from a local operating system.

# Abilities

Greet/Farewell according to time of the day [morning, afternoon and night]

Control Lifx light bulbs [power on/off, change color]

Open computer applications [google chrome, webcam]

Carry out windows CMD functions [schedule shutdown, clear screen]

Get events on any day from Google Calendar


# Block Diagrams
 ![IRIS (Personal Project)](https://user-images.githubusercontent.com/63937643/168951282-16bae320-a967-4152-97ed-e52e81e49b8b.jpg)
![IRIS (Personal Project) (1)](https://user-images.githubusercontent.com/63937643/168951340-0144c2f2-eb76-4948-8d71-8a7a0afc197e.jpg)

# Updates

### 08/19/2021
Error Handling:

    Except network error

    Except lightbulb error
    
    Handle Error No.11001
    
Functionlities:
    
    Schedule shutdown 
    
    Clear console screen
    
    Call IRIS only when user wants to perform personal task (calendar, to-do...etc)

### 08/24/2021
Functionalities:

    Sleep IRIS

### 09/09/2021
Functionalities:

    Time sensitive lighting 

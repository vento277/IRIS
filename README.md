# Introduction
Iris is my personal assistant that helps automate daily tasks such as lighting controls and playing music. The code is meant to be used on my local computer, but it is simple enough such that with small changes, one can make good use of it. 

# Revisions

 ### 1.0
 - A simple one-file program

 ### 1.1
 - A bit more advanced programming with a library of responses to assist the keyword-based conversation.
 - Multiple levels of function calls.

 ### 2.0 (in progress)
 - Implementing OOP for a flexible addition of assistant abilities in the future
 - Contextual-based conversation 
 - Its abilities are carefully chosen from my experience over the past two years and are customized to maximize its productivity. 

# v2.0 

## STT & TTS
STT -> Vosk (local)

TTS -> Google 

## Abilities
- Greeting
Recognizes the time and greets appropriately. It can also get the weather information and offer you advise as to what to wear.
- Weather
OpenWeatherMap API - JSON
- Lighting Control
Take control of the locally available Lifx lightbulb and adjust its brightness and colour according to the time, weather, and user input.
- Timer
Make use of the Pomodoro Technique to set up a customized (35~45min Work/Study & a 5~10 min break ) work/study session for desired amount of hours.
- Search
Allow search function for various websites such as Google, Wikipedia, Youtube, Research Gate...etc
- Budget
Perform personal budgeting by taking daily spending from the user, and summing up the data weekly.
- Music
Play the right music at the right time.

## Block Diagram
<img src="https://docs.google.com/drawings/d/e/2PACX-1vTSLKY5qjm8dchPXGebag4KHNb58EpLL8VrGKnNNZ5f4CTxq4HempfUZDybn4H1dhvQjZlMiRYSR0T4/pub?w=1874&amp;h=880"> 

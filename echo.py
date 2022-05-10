import sys
import pyjokes
import pyttsx3
import pyttsx3 as p
import speech_recognition as sr
import pywhatkit
import pyaudio
import datetime
import wikipedia
import requests,json

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
    
#talk("Hello, How may I help you")

def take_command():
    with sr.Microphone() as source:
        print('listening...')
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
        try:
            command = listener.recognize_google(voice)
            command = command. lower()
            if 'echo' in command:
                command = command.replace('echo', '')
                print(command)
        except LookupError:
            print("Could not understand")
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M%p')
        talk('Current time is' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        date = datetime.datetime.today().strftime('%H:%M')
        talk('Current date is' + date)
    elif 'are you single' in command:
        talk('sorry, I am in relationship with wifi')
    elif 'jokes' in command:
        talk(pyjokes.get_jokes())
    elif 'weather' in command:
        api_key = "***creat_own_api_key_here***"
        base_url = " http://api.openweathermap.org/data/2.5/weather?"
        city_name = "Bengaluru"
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]-273.15
            print("Temperature in Bangalore = " + str(current_temperature))
            talk(current_temperature)
        else:
            print("City not Found")

    else:
        talk('Sorry, I could not understand your command')

while True:
    run_alexa()

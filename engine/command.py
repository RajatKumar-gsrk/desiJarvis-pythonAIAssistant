import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text = "Hello I am D.J! nice to meet you"):
    engine = pyttsx3.init('sapi5')

    voices = engine.getProperty('voices')       #getting details of current voice
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 175)

    eel.displayMessage(text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

@eel.expose # accessible through js file
def takeCommand():
    r = sr.Recognizer()

    try:
        mic = sr.Microphone(device_index=1) # Try with one of the microphone indices
        with mic as source:
            print("Listening...")
            eel.displayMessage("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, phrase_time_limit=5)
    except Exception as e:
        print(f"Error initializing microphone: {e}")
        eel.displayMessage("Error initializing microphone")
        return "None"

    try:
        print("Recognizing...")
        eel.displayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        time.sleep(2)
        
        print(f"User said : {query}")
        eel.displayMessage(query)
    except Exception as e:
        print(e)
        eel.displayMessage("Error! please repeat again")
        return "Error! please repeat again"
    

    eel.userText("user said "+query)
    return query.lower()

# takeCommand()

@eel.expose
def takeAllCommand(query = ""):
    if query == "":
        query = takeCommand()
    else:
        print(f"User query : {query}")
        eel.displayMessage(f"{query}")

    eel.userText(query)

    if "message" in query:
        from engine.features import messageContact
        messageContact(query)
    
    elif "call" in query:
        from engine.features import callContact
        callContact(query)

    elif "open" in query:
        from engine.features import openCommand
        openCommand(query)
        
    elif "youtube" in query:
        from engine.features import openYoutube
        openYoutube(query)

    else:
        from engine.gemini_api import generateAiResponse
        response = generateAiResponse(query)
        response=response.replace("*", "")
        eel.assistantText(response)
        eel.displayMessage(response)
        speak(response)


    time.sleep(3)
    eel.displayMessageReset()
    eel.displayOval()

    print("the end")
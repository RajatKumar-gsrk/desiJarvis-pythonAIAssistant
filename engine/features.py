import re
import webbrowser
from playsound import playsound
import eel
from engine.config import *
from engine.command import *
import os
import pywhatkit
import sqlite3

connection = sqlite3.connect("desijarvis.db")
cursor = sqlite3.Cursor(connection)

@eel.expose # accessible through js file
def soundAssistant():
    music_dir = "www\\assets\\audio\\boot.mp3"
    playsound(music_dir)


def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace('open', '')

    app_name = query.strip().lower()

    if app_name != "":
        try:
            cursor.execute(
                "SELECT path from sys_commands WHERE name IN (?)",(app_name,)
            )
            result = cursor.fetchall()

            if len(result) != 0:
                speak("opening "+query)
                os.startfile(result[0][0])
                return
            elif len(result) == 0:
                cursor.execute(
                    "SELECT path from web_commands WHERE name IN (?)",(app_name,)
                )
                result = cursor.fetchall()
                if len(result) != 0:
                    speak("opening "+query)
                    webbrowser.open(result[0][0])
                    return
                else:
                    if query != "":
                        speak("opening "+query)
                        os.system("start "+query)
                    else:
                        print("Error command not found")
                        eel.displayMessage("Error command not found")
                        raise NotFoundError("Something is wrong with command")
        except:
            speak("Something went wrong")

    


def openYoutube(query):
    query = extractKeyword(query)
    if query != "":
        speak('playing '+query+' on youtube')
        pywhatkit.playonyt(query)
    else:
        speak("Error please repeat")

def extractKeyword(query):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, query)

    if match != None:
        return match.group(1)
    else:
        return ""
    
class NotFoundError(Exception):
    """Custom exception class"""
    def __init__(self, message="Not Found"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"CustomError: {self.message}"


import speech_recognition as sr
import sys
import pyttsx3
import os
from web import youtube  # ✅ import youtube.py
from web import chrome   # ✅ import chrome.py
from web import wikipedia  # ✅ new import

r = sr.Recognizer()

def say(text):
    os.system(f"say {text}")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def take():
    with sr.Microphone() as source:
        # say("Say something!")
        try:
            audio = r.listen(source)
            aw = r.recognize_google(audio, language="en-in")
            print(aw)
            return aw
        except:
            return "sorry try again"


if __name__ == "__main__":
    say("program is on")
    while True:

        text = take()
        say(text)

        # ---------- YOUTUBE ----------
        if "open youtube" in text.lower():
            msg = youtube.open_youtube()
            say(msg)

        elif "search" in text.lower() and "youtube" in text.lower():
            query = text.lower().replace("search", "").replace("on youtube", "").replace("youtube", "").strip()
            if query:
                msg = youtube.search_youtube(query)
                say(msg)
            else:
                say("Please tell me what to search on YouTube")

        elif "play" in text.lower() and "video" in text.lower():
            for word, num in youtube.number_map.items():
                if word in text.lower():
                    msg = youtube.play_nth_video(num)
                    say(msg)
                    break

        elif any(cmd in text.lower() for cmd in ["play", "pause", "mute", "unmute", "fullscreen", "minimise",
                                                 "forward", "back", "rewind", "volume up", "volume down",
                                                 "next video", "previous video"]):
            msg = youtube.control_video(text.lower())
            say(msg)

        elif "close youtube" in text.lower():
            msg = youtube.close_youtube()
            say(msg)

        # ---------- CHROME ----------
        elif "open chrome" in text.lower():
            msg = chrome.open_chrome()
            say(msg)

        elif "search" in text.lower() and "chrome" in text.lower():
            query = text.lower().replace("search", "").replace("on chrome", "").replace("chrome", "").strip()
            if query:
                msg = chrome.search_chrome(query)
                say(msg)
            else:
                say("Please tell me what to search on Chrome")

        elif "click" in text.lower() and "website" in text.lower():
            for word, num in youtube.number_map.items():
                if word in text.lower():
                    msg = chrome.play_nth_website(num)
                    say(msg)
                    break

        elif "close chrome" in text.lower():
            msg = chrome.close_chrome()
            say(msg)

        # ---------- WIKIPEDIA ----------
        elif "open wikipedia" in text.lower():
            msg = wikipedia.open_wiki()
            say(msg)

        elif "search" in text.lower() and "wikipedia" in text.lower():
            query = text.lower().replace("search", "").replace("on wikipedia", "").replace("wikipedia", "").strip()
            if query:
                msg = wikipedia.search_wiki(query)
                say(msg)
            else:
                say("Please tell me what to search on Wikipedia")

        elif "open" in text.lower() and "result" in text.lower():
            for word, num in wikipedia.number_map.items():
                if word in text.lower():
                    msg = wikipedia.open_nth_result(num)
                    say(msg)
                    break

        elif "close wikipedia" in text.lower():
            msg = wikipedia.close_wiki()
            say(msg)

        # ---------- EXIT ----------
        elif "exit" in text.lower() or "goodbye" in text.lower():
            say("i am closing the program, goodbye osama sir")
            youtube.close_youtube()
            chrome.close_chrome()
            wikipedia.close_wiki()
            sys.exit()
        elif "hello" in text.lower() or "z" in text.lower():
            say("Hello osama sir, how can i help you")

        # else:
        #     say("i am closing the program sir")

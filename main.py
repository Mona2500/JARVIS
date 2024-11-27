import sys
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import webbrowser
import pywhatkit as kit

# Unset the HTTP_PROXY environment variable
if 'HTTP_PROXY' in os.environ:
    del os.environ['HTTP_PROXY']



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)


#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_thresold = 1
        audio = r.listen(source, timeout=10, phrase_time_limit=10)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<10:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    speak("I am AI assistant Sir. please tell me how can i help you   ")

if __name__ == "__main__":
    wish()
    #while True:
    if 1:
        query =takecommand().lower()
        #logic building for tasks

        if "open notepad" in query:
            os.system("notepad")
        elif "open command prompt" in query:
            os.system("Start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)  # Open the default camera

            if not cap.isOpened():
                print("Error: Could not open the camera.")
            else:
                while True:
                    ret, img = cap.read()
                    if not ret:
                        print("Error: Failed to capture image.")
                        break

                    cv2.imshow('Webcam', img)

                    # Wait for 1 ms and check if 'q' is pressed to quit
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

                cap.release()  # Release the camera
                cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "C:\\Users\\deepa\\Music\\New folder"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))


        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open google" in query:
            speak("Sir, what should I search on Google?")
            cm = takecommand().lower()

            if cm:
                # Format the search query for Google
                search_url = f"https://www.google.com/search?q={cm.replace(' ', '+')}"
                webbrowser.open(search_url)
                speak(f"Here are the results for {cm}")
            else:
                speak("I didn't catch that. Please try again.")
        elif "send message" in query:
            try:
                phone_number = "+919337614495"  # Replace with the recipient's phone number
                message = "Good morning"

                # Send message instantly
                kit.sendwhatmsg_instantly(phone_no=phone_number, message=message, wait_time=10)

                print("Message sent successfully!")
                speak("Message sent successfully.")
            except Exception as e:
                print(f"An error occurred: {e}")
                speak("I couldn't send the message. Please check the details.")

        elif "play song on youtube" in query:
            try:
                # Ask the user for the song name
                speak("Which song would you like to play?")
                song_name = takecommand().lower()

                if song_name:
                    # Play the song on YouTube
                    speak(f"Playing {song_name} on YouTube.")
                    kit.playonyt(song_name)
                else:
                    speak("I couldn't catch the song name. Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}")
                speak("I couldn't play the song. Please check your internet connection or try again.")

        elif "no thanks" in query:
            speak("thank for using me sir, have a good day.")
            sys.exit()

        speak("sir. do you have any other work")
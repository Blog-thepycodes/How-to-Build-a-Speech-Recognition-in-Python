import speech_recognition as sr
import pyttsx3
 
 
# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
 
 
def speak(text):
   """Converts text to speech."""
   engine.say(text)
   engine.runAndWait()
 
 
def recognize_speech_from_mic(recognizer):
   """Captures and recognizes speech."""
   mic = sr.Microphone()
   with mic as source:
       recognizer.adjust_for_ambient_noise(source, duration=0.2)
       audio = recognizer.listen(source)
       try:
           return {"success": True, "error": None,
                   "transcription": recognizer.recognize_google(audio, language='en').lower()} # change ‘en’ to the language code you want
       except sr.UnknownValueError:
           return {"success": False, "error": "Could not understand audio", "transcription": None}
       except sr.RequestError as e:
           return {"success": False, "error": f"Could not request results; {e}", "transcription": None}
 
 
 
def main():
   try:
       while True:
           print("Listening...")
           result = recognize_speech_from_mic(recognizer)
 
 
           if result["success"]:
               text = result["transcription"]
               print(f"Recognized: {text}")
               speak(f"You said: {text}")
           else:
               error = result["error"]
               print(error)
               speak(
                   error if "Could not understand audio" not in error else "Sorry, I didn't catch that. Can you please repeat?")
   except KeyboardInterrupt:
       print("Exiting...")
 
 
if __name__ == "__main__":
   main()

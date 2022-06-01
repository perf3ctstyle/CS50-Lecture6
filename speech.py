import pyttsx3

if __name__ == "__main__":
    engine = pyttsx3.init()
    name = input("What's your name? ")
    engine.say(f"hello, {name}")
    engine.runAndWait()

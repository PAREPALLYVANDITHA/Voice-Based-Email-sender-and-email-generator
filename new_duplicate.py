import speech_recognition as sr
import pyttsx3
import smtplib

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        speak_text(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I did not understand that. Say again.")
        speak_text("Sorry, I did not understand that. Say again.")
        return listen()
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""

def confirm_input(prompt):
    while True:
        print(prompt)
        speak_text(prompt)
        user_input = listen()
        print("You said: " + user_input)
        speak_text(f"You said: {user_input}. Is that correct? Say yes or no.")
        
        confirmation = listen().lower()
        if confirmation in ["yes", "y"]:
            return user_input
        
        elif confirmation in ["no", "n"]:
            print("Let's try again.")
        else:
            print("Please respond with yes or no.")

def main():
    print("Adjusting for ambient noise, please wait...")
    speak_text("Adjusting for ambient noise, please wait...")
    
    sender_email = confirm_input("Please say your email address:") + "@gmail.com"
    receiver_email = confirm_input("Please say the receiver's email address:") + "@iare.ac.in"
    subject = confirm_input("Please say the subject of the email:")
    message = confirm_input("Please say your message:")
    app_password = confirm_input("Please say your app password:")
    
    text = f"Subject: {subject}\n\n{message}"
    
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("Email has been sent to " + receiver_email)
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    main()

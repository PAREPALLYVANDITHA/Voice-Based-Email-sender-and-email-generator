import speech_recognition as sr
import pyttsx3
import smtplib

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak_text(text):
    engine.say(text)
    engine.runAndWait()
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            speak_text(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that. Say again")
            speak_text("Sorry, I did not understand that. Say again")
            return listen()
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""
 
def main():
    print("Adjusting for ambient noise, please wait...")
    speak_text("Adjusting for ambient noise, please wait...")
    print("Please say your email address:")
    speak_text("Please say your email address:")
    sender_recipient = listen()+"@gmail.com"
    sender_email = ''.join(sender_recipient.split())
    #sender_email = "vanditha08102004@gmail.com"
    print("You Said: "+sender_email)
    speak_text(sender_email)

    print("Please say the receiver's email address:")
    speak_text("Please say the receiver's email address:")
    receiver_recipient = listen()+"@iare.ac.in"
    receiver_email = ''.join(receiver_recipient.split())
    #receiver_email = "22951a66g5@iare.ac.in"
    print("You Said: "+receiver_email)
    speak_text(receiver_email)

    print("Please say the subject of the email:")
    speak_text("Please say the subject of the email:")
    subject = listen()
    print("You Said: "+subject)
    speak_text(subject)

    print("Please say your message:")
    speak_text("Please say your message:")
    message = listen()
    speak_text(message)

    print("Please say your app password:")
    speak_text("Please say your app password:")
    app_pw = listen()
    app_password = ''.join(app_pw.split())
    #app_password = "qruvbqpylbhnzwke"
    print("You Said: "+app_password)
    speak_text(app_password)

    text = f"Subject: {subject}\n\n{message}"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)
    server.sendmail(sender_email, receiver_email, text)
    server.quit()
    print("Email has been sent to " + receiver_email)

if __name__ == "__main__":
    main()


    

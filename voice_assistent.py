import pyttsx3
import speech_recognition as sr
import json
recognizer = sr.Recognizer()

with open('data.json', 'r') as file:
    data = json.load(file)
    questions = data["interview_questions"]

engine = pyttsx3.init()
rate = engine.getProperty('rate')  
engine.setProperty('rate', rate - 90) 
for i, qa_pair in enumerate(questions, start=1):
    question = qa_pair["question"]
    answer = qa_pair["answer"]
    print(f"Question {i}: {question}")
    engine.say(question)
    engine.runAndWait()
    with sr.Microphone() as source:
        print("Listening for your answer...")
        audio = recognizer.listen(source)
    try:
        user_answer = recognizer.recognize_google(audio)
        print(f"You said: {user_answer}")
        #if user_answer.lower() in answer.lower():
        #    print("Correct!")
        #else:
        #    print("Incorrect. The correct answer is:")
        #    print(answer)

    except sr.UnknownValueError:
        print("Sorry, I could not understand your answer.")

    except sr.RequestError as e:
        print(f"Error: {e}")

engine.stop()

from google import genai
from dotenv import load_dotenv
import os
# call to load_dotenv
load_dotenv

#connecting to gemini
client = genai.Client(
    api_key = os.getenv("Gemini_API_key")
)
#creating chats
chat = client.chats.create(
    model = "gemini-3.8-flash"
)

print("Gemini chatboat started!!")
print("enter 'end' to stop.\n")

#chatbot loop
while True:
    user_input = input("you: ")

    if user_input.lower() == "exit":
        print("Chatbot Stopped!!")
        break

    #sending message to gemini
    response = chat.send_message(user_input)

    #display response
    print("Gemini: ", response.text)
import openai
import os
env = open(".env", "r")
openai.api_key = env.read().strip()
completion = openai.Completion()

chat_log = None
start_chat_log = ''' This is a conversation between an human and a very smart AI. The AI will reply to nonsense with 'This does not make sense'.
Q: What is a bombobo?
A: This does not make sense

Human: Hello!
AI: Hello there!
'''

def ask(question, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    prompt = f'{chat_log}Human: {question}\nAI:'
    response = completion.create(
        prompt=prompt, engine="davinci", stop=['\nHuman'], temperature=0.9,
        top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1,
        max_tokens=150)
    answer = response.choices[0].text.strip()
    return answer


def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    return f'{chat_log}Human: {question}\nAI: {answer}\n'


def_username = "Hooman"
username = input("Hello! What is your name?\n")
if username == "":
    username = def_username
print("Ok " + username + ", go on!\n")
print(start_chat_log)
while True:
    try:
        question = input(username + ": ")
        if question.lower() == "exit":
            print("AI: Bye bye")
            exit(0)
        answer = ask(question, chat_log)
        print("AI: " + answer)
        chat_log = append_interaction_to_chat_log(question, answer, chat_log)
    except KeyboardInterrupt:
        print("Exiting")
        exit(0)
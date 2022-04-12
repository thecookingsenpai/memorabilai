import os
try:
    import openai
except:
    os.system("pip install openai")
    
openai.api_key = "s"

try:
    import PySimpleGUI as sg
except:
    os.system("pip install pysimplegui")
    
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



# Ask username

username = "Hooman"

layout = [[sg.Text('What is your name?')],      
          [sg.Input(key='-IN-')],      
          [sg.Button('Start'), sg.Exit()]]      
font = ("Arial, 14")
window = sg.Window('Welcome!', layout, font=font)      

while True:                             # The Event Loop
    event, values = window.read() 
    if event == sg.WIN_CLOSED or event == 'Exit':
        break      
    else:    
        print(event, values)
        username = values.get("-IN-")  
        break
window.close()

# Main window
layout = [  [sg.Text('Hello, welcome to MemorabilAI!')],
            [sg.Output(size=(50,10), key='-OUTPUT-')],
            [sg.In(key='-IN-', do_not_clear=False)],
            [sg.Button('Speak', bind_return_key=True), sg.Button('Clear'), sg.Button('Exit')]  ]
 
font = ("Arial, 14")
window = sg.Window('MemorabilAI', layout, font=font)

print(start_chat_log)
while True:             # Event Loop
    event, values = window.read()
    userInput = values.get("-IN-")
    if event in (sg.WIN_CLOSED, 'Exit'):
        print("AI: Bye bye")
        window.close()  
        exit(0)
    if event == 'Clear':
        window['-OUTPUT-'].update('')
    
    print(username + ": " + userInput)
    answer = ask(userInput.lower(), chat_log)
    print("AI: " + answer)
    chat_log = append_interaction_to_chat_log(userInput, answer, chat_log)

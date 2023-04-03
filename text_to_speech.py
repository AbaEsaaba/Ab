import PySimpleGUI as sg
import pyttsx3

# Initialize the pyttsx3 engine
bot = pyttsx3.init()

# Define the layout of the PySimpleGUI window
layout = [
    [sg.Text('Enter text to speak:')],
    [sg.Input(key='-TEXT-')],
    [sg.Button('Speak'), sg.Button('Exit')],
    [sg.Text('speed'), sg.Input(key='speed',size= 4, default_text= '100')],
    [sg.Text('', key='-STATUS-')],
    [sg.Text('select voice type'), sg.Radio('Male','Gender',key='Male_voice', default= True), 
     sg.Radio('Female','Gender',key='Female_voice')],
    [sg.Text('volume'), sg.Slider(key='volume', range=(0,10), orientation='hor',size=(10,10), default_value=0)]
]

# Create the PySimpleGUI window
window = sg.Window('Text-to-Speech App', layout)

# Event loop to process "Speak" button and "Exit" button clicks
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):  # If user closes window or clicks "Exit" button
        break
    if event == 'Speak':
        text = values['-TEXT-']
        if text != '':
            # Set the engine properties and speak the text
            bot.setProperty('rate', 150)  # Speed in words per minute
            bot.setProperty('volume', 1.0)  # Volume (0-1)
            bot.say(text)
            bot.runAndWait()
            window['-STATUS-'].update('Text spoken!')
        else:
            window['-STATUS-'].update('Please enter some text.')

# Close the PySimpleGUI window
window.close()
    
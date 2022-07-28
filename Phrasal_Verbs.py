import PySimpleGUI as sg

#  TODO
#  1. Hande this window closing (meaning i should be able to close the window with x - now when i do this program will crash
#  2. Make it nicer in general
#  3. Add input field to check spelling/writing

#  our layout
layout = [[sg.Text("Phrasal Verbs App")],
          [sg.Button("PhrasalVerb")],
          [sg.Text(size=(40,1), key='OUTPUT1')],
          [sg.Button("Definition")],
          [sg.Text(size=(40,1), key='OUTPUT2')],
          [sg.Button("Usage")],
          [sg.Text(size=(40, 1), key='OUTPUT3')]
          ]

# Create the window
window = sg.Window("Phrasal Verbs Aka App", layout,margins=(300,150))


data = [["ask somebody out","invite on a date","Brian asked Judy out to dinner and a movie."],
        ["ask around","ask many people the same question","I asked around but nobody has seen my wallet."]]


index=1
# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "PhrasalVerb" :
        window['OUTPUT1'].update(data[index][0])
    if event == "Definition":
        window['OUTPUT2'].update(data[index][1])
    if event == "Usage" :
        window['OUTPUT3'].update(data[index][2])
window.close()
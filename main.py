import PySimpleGUI as sg

# The main window
layout = [
    [sg.Text('Specify duplication options:')],
    [sg.Text('Number of copies: '), sg.InputText('10')],
    [sg.Text('Select a file: '), sg.Input(),
     sg.FileBrowse(key="-IN-")],
    [sg.Button("OK")],
    [sg.Button("Exit")]]

# Search box
window = sg.Window('Specify the location of the file', layout, size=(600, 200))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "OK":
        print(values["-IN-"])
        break

window.close()

file2 = open(values["-IN-"] + values[0] + ".gco", 'w')
for i in range(int(values[0])):
    file = open(values["-IN-"], 'r')
    for line in file:
        file2.write(line)
    file2.write("\n; Copy " + str(i) + "\n")
    file.close()
file2.close()
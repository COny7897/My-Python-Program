import PySimpleGUI as sg

col1 = sg.Column([[sg.Frame('Your information :', [[sg.Text(), sg.Column(
        [
            [sg.Text('Credits')],
            [sg.Text('GPAX :', size=(10,1)), sg.Spin([0],key='-CLI-1-', size=(10,1))],
            [sg.Text('GPA Math :', size=(10,1)), sg.Spin([0],key='-CLI-2-', size=(10,1))],
            [sg.Text('GPA Sci :', size=(10,1)), sg.Spin([0],key='-CLI-3-', size=(10,1))],
            [sg.Text('GPA Eng :', size=(10,1)), sg.Spin([0],key='-CLI-4-', size=(10,1))],
            [sg.Text('TGAT')],
            [sg.Text('Tgat :', size=(10,1)), sg.Spin([0],key='-CLI-5-', size=(10,1))],
            [sg.Text('Tgat 1 :', size=(10,1)), sg.Spin([0],key='-CLI-6-', size=(10,1))],
            [sg.Text('Tgat 2 :', size=(10,1)), sg.Spin([0],key='-CLI-7-', size=(10,1))],
            [sg.Text('Tgat 3 :', size=(10,1)), sg.Spin([0],key='-CLI-8-', size=(10,1))],
            [sg.Text('TPAT')],
            [sg.Text('Tpat 1 :', size=(10,1)), sg.Spin([0],key='-CLI-9-', size=(10,1))],
            [sg.Text('Tpat 2 :', size=(10,1)), sg.Spin([0],key='-CLI-10-', size=(10,1))],
            [sg.Text('Tpat 3 :', size=(10,1)), sg.Spin([0],key='-CLI-11-', size=(10,1))],
            [sg.Text('Tpat 4 :', size=(10,1)), sg.Spin([0],key='-CLI-12-', size=(10,1))],
            [sg.Text('Tpat 5 :', size=(10,1)), sg.Spin([0],key='-CLI-13-', size=(10,1))],
            [sg.Text('A-LEVEL')],
            [sg.Text('Math 1 :', size=(10,1)), sg.Spin([0],key='-CLI-14-', size=(10,1))],
            [sg.Text('Math 2 :', size=(10,1)), sg.Spin([0],key='-CLI-15-', size=(10,1))],
            [sg.Text('Sci :', size=(10,1)), sg.Spin([0],key='-CLI-16-', size=(10,1))],
            [sg.Text('Physics :', size=(10,1)), sg.Spin([0],key='-CLI-17-', size=(10,1))],
            [sg.Text('Chemistry :', size=(10,1)), sg.Spin([0],key='-CLI-18-', size=(10,1))],
            [sg.Text('Biology :', size=(10,1)), sg.Spin([0],key='-CLI-19-', size=(10,1))],
            [sg.Text('Social :', size=(10,1)), sg.Spin([0],key='-CLI-20-', size=(10,1))],
            [sg.Text('Thai :', size=(10,1)), sg.Spin([0],key='-CLI-21-', size=(10,1))],
            [sg.Text('Eng :', size=(10,1)), sg.Spin([0],key='-CLI-22-', size=(10,1))],
            [sg.Text('3th language :', size=(10,1)), sg.Spin([0],key='-CLI-23-', size=(10,1))],
        ],size=(210,725), pad=(0,0))]])], ], pad=(0,0))

col2 = sg.Column([[sg.Frame('Score Criteria :', [[sg.Text(), sg.Column(
        [
            [sg.Text('Credits')],
            [sg.Text('GPAX :', size=(10,1)), sg.Spin([0],key='-SC-1-', size=(10,1))],
            [sg.Text('GPA Math :', size=(10,1)), sg.Spin([0],key='-SC-2-', size=(10,1))],
            [sg.Text('GPA Sci :', size=(10,1)), sg.Spin([0],key='-SC-3-', size=(10,1))],
            [sg.Text('GPA Eng :', size=(10,1)), sg.Spin([0],key='-SC-4-', size=(10,1))],
            [sg.Text('TGAT')],
            [sg.Text('Tgat :', size=(10,1)), sg.Spin([0],key='-SC-5-', size=(10,1))],
            [sg.Text('Tgat 1 :', size=(10,1)), sg.Spin([0],key='-SC-6-', size=(10,1))],
            [sg.Text('Tgat 2 :', size=(10,1)), sg.Spin([0],key='-SC-7-', size=(10,1))],
            [sg.Text('Tgat 3 :', size=(10,1)), sg.Spin([0],key='-SC-8-', size=(10,1))],
            [sg.Text('TPAT')],
            [sg.Text('Tpat 1 :', size=(10,1)), sg.Spin([0],key='-SC-9-', size=(10,1))],
            [sg.Text('Tpat 2 :', size=(10,1)), sg.Spin([0],key='-SC-10-', size=(10,1))],
            [sg.Text('Tpat 3 :', size=(10,1)), sg.Spin([0],key='-SC-11-', size=(10,1))],
            [sg.Text('Tpat 4 :', size=(10,1)), sg.Spin([0],key='-SC-12-', size=(10,1))],
            [sg.Text('Tpat 5 :', size=(10,1)), sg.Spin([0],key='-SC-13-', size=(10,1))],
            [sg.Text('A-LEVEL')],
            [sg.Text('Math 1 :', size=(10,1)), sg.Spin([0],key='-SC-14-', size=(10,1))],
            [sg.Text('Math 2 :', size=(10,1)), sg.Spin([0],key='-SC-15-', size=(10,1))],
            [sg.Text('Sci :', size=(10,1)), sg.Spin([0],key='-SC-16-', size=(10,1))],
            [sg.Text('Physics :', size=(10,1)), sg.Spin([0],key='-SC-17-', size=(10,1))],
            [sg.Text('Chemistry :', size=(10,1)), sg.Spin([0],key='-SC-18-', size=(10,1))],
            [sg.Text('Biology :', size=(10,1)), sg.Spin([0],key='-SC-19-', size=(10,1))],
            [sg.Text('Social :', size=(10,1)), sg.Spin([0],key='-SC-20-', size=(10,1))],
            [sg.Text('Thai :', size=(10,1)), sg.Spin([0],key='-SC-21-', size=(10,1))],
            [sg.Text('Eng :', size=(10,1)), sg.Spin([0],key='-SC-22-', size=(10,1))],
            [sg.Text('3th language :', size=(10,1)), sg.Spin([0],key='-SC-23-', size=(10,1))],
        ],size=(210,725), pad=(0,0))]])], ], pad=(0,0))

col3 = sg.Column([[sg.Frame('', [[sg.Column(
        [
            [sg.Button('Calulate', size=(55,1))],
            [sg.Text('Output', key='-OUTPUT-')]
        ], size=(460,60), pad=(0,0))]])]], pad=(0,0))

layout = [[col1, col2],
          [col3]]

window = sg.Window('Tcas Scores Calculator', layout)


score = 0

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Calulate':
        for i in range(1,24):
            a = values[f'-CLI-{i}-']
            b = values[f'-SC-{i}-']
            if a != None or b != None:
                x = float(a)
                y = float(b)
                if i in [1,2,3,4]:
                    z = (x / 4) * y
                else:
                    z = (x * y) / 100
                score += z
        window['-OUTPUT-'].update(score)
        score = 0


window.close()

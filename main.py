from functions import lucky_number, extract_numbers
# PySimpleGUI, PySimpleGUIWx, PySimpleGUIWeb
import PySimpleGUIQt as Sg
import datetime as dt
import pandas as pd


layout = [
    [Sg.Text("Digite o número do concurso: ")],
    [Sg.Input(key='-INPUT-')],
    [Sg.Text(size=(40, 1), key='-OUTPUT0-')],
    [Sg.Text(size=(40, 1), key='-OUTPUT1-')],
    [Sg.Text(size=(40, 1), key='-OUTPUT2-')],
    [Sg.Text(size=(40, 1), key='-OUTPUT3-')],
    [Sg.Text(size=(40, 1), key='-OUTPUT4-')],
    [Sg.Text(size=(40, 1), key='-OUTPUT5-')],
    [Sg.Text(size=(40, 1), key='-OUTPUT6-')],
    [Sg.Text(size=(40, 1), key='-OUTPUT7-')],
    [Sg.Text(size=(40, 1), key='-OUTPUT8-')],
    [Sg.Text(size=(40, 1), key='-OUTPUT9-')],
    [Sg.Text(size=(40, 1), key='-OUTPUTT-')],
    [Sg.Button("Pesquisar"), Sg.Button("Cancelar")]
]

window = Sg.Window("Sorteio Loteria Federal", layout)


while True:
    event, values = window.read()
    resp = extract_numbers(values['-INPUT-'])
    if event == Sg.WINDOW_CLOSED or event == 'Cancelar':
        break

    window['-OUTPUT1-'].update("")
    window['-OUTPUT2-'].update("")
    window['-OUTPUT3-'].update("")
    window['-OUTPUT4-'].update("")
    window['-OUTPUT5-'].update("")
    window['-OUTPUT6-'].update("")
    window['-OUTPUT7-'].update("")
    window['-OUTPUT8-'].update("")
    window['-OUTPUT9-'].update("")
    window['-OUTPUTT-'].update("")

    erro = "erro"

    for error in resp.keys():
        if error == erro:
            window['-OUTPUT0-'].update("RESULTADO")
            if '503' in resp["mensagem"]:
                window['-OUTPUT1-'].update("Erro Http 503: Serviço Indisponível")
            else:
                window['-OUTPUT1-'].update("{}.".format(resp["mensagem"]))
            window['-OUTPUT2-'].update("Favor realizar a consulta novamente.")

    jogo = "tipoJogo"

    for game in resp.keys():
        if game == jogo:
            window['-OUTPUT0-'].update("RESULTADO")
            window['-OUTPUT1-'].update(resp["tipoJogo"].replace("_", " "))
            window['-OUTPUT2-'].update("Concurso: {} sorteado em: {}".format(resp["numero"], resp["dataApuracao"]))
            window['-OUTPUT3-'].update("    1º Prêmio: {}".format(resp["dezenasSorteadasOrdemSorteio"][0]))
            window['-OUTPUT4-'].update("    2º Prêmio: {}".format(resp["dezenasSorteadasOrdemSorteio"][1]))
            window['-OUTPUT5-'].update("    3º Prêmio: {}".format(resp["dezenasSorteadasOrdemSorteio"][2]))
            window['-OUTPUT6-'].update("    4º Prêmio: {}".format(resp["dezenasSorteadasOrdemSorteio"][3]))
            window['-OUTPUT7-'].update("    5º Prêmio: {}".format(resp["dezenasSorteadasOrdemSorteio"][4]))
            window['-OUTPUT8-'].update("Número da Sorte: {}".format(lucky_number(resp)))
            window['-OUTPUT9-'].update("Próximo Concurso: {}".format(resp["numeroConcursoProximo"]))
            window['-OUTPUTT-'].update("Arquivo gerado em: output/sorteio_final.csv")

    vazio = ""

    for empty in resp.keys():
        if empty == vazio:
            window['-OUTPUT2-'].update("Favor realizar a consulta novamente.")

    fileout = {"Jogo": resp["tipoJogo"].replace("_", " "), "Consurso": resp["numero"],
               "Data do Sorteio": resp["dataApuracao"], "Data da Apuração": str(dt.datetime.now()),
               "Primeiro": resp["dezenasSorteadasOrdemSorteio"][0], "Segundo": resp["dezenasSorteadasOrdemSorteio"][1],
               "Terceiro": resp["dezenasSorteadasOrdemSorteio"][2], "Quarto": resp["dezenasSorteadasOrdemSorteio"][3],
               "Quinto": resp["dezenasSorteadasOrdemSorteio"][4], "Numero da Sorte": lucky_number(resp)}

    file = pd.DataFrame(fileout, index=[0])
    file.to_csv("output/sorteio_final.csv", index=False, sep=";", header=True)

window.close()

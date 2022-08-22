import random
import PySimpleGUI as sg

# Nome_do _programa: Jogo Dado
#
# site: https://github.com/FabianoLandimDev/Jogo-Dado
#
# Autor: Fabiano Landim <landimfabiano01@gmail.com>
#
# Manutenção: Fabiano Landim <landimfabiano01@gmail.com>
#
# ESCOPO:
# O Programa nada mais é que uma interface gráfica desnvolvida em PySimpleGUI, com o intuito de proporcionar um jogo de dados
# simulando uma disputa entre o computador e você,onde ambos escolhem um número de 1 à 6, no qual resultará em um ganhador, empate, ou nenhum ganhador.
#
# Histórico:
#
# v1.0 2022-08-19, Fabiano Landim:
# - Versão Inicial do Programa.
#
# Licença: MIT.

#Criando as funções pertinentes...
#
def janela_inicio():
    sg.theme('Dark Grey 10')

    layout = [
        [sg.Text('Escolha um número de 1 à 6')],
        [sg.Text('Você:'), sg.Combo(values=list(range(1, 7)), key='-VOCE-')],
        [sg.Button('SORTEAR')],
        [sg.Text('Resultado:')],
        [sg.Output(key='-OUTPUT-', size=(20, 5))],
        [sg.Button('REPETIR'), sg.Button('SAIR')]
    ]
    return sg.Window('JODO DE DADO', layout, finalize=True)

#Condicionais....
#
window = janela_inicio()


while True:
    #Variáveis...
    #numeros_permitidos = list(range(1, 7))
    #seu_numero = values['-VOCE-']
    #numeros_computador = random.randint(1, 6)
    #dado = random.randint(1, 6)
    
    events, values = window.read()
    if events == 'SAIR' or events == sg.WIN_CLOSED():
        break
    elif events == 'REPETIR':
        window.close()
        window = janela_inicio()
    #if events == 'SORTEAR':
     #   if values['-VOCE-'] in numeros_permitidos:
     #       print('Você escolheu o número {}'.format(seu_numero))
window.close()
# importando as bibliotecas necessárias
import os
import pandas as pd
import sqlite3
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# Banco de dados
banco_de_dados = 'my_db.db'

# definindo a classe principal

class MeuApp(App):

    # método para construir a interface gráfica
    def build(self):
        
        # criando um layout principal
        layout = BoxLayout(orientation='vertical')
        
        # criando um label
        label = Label(text='Olá, mundo!')
        
        # criando um botão
        botao = Button(text='Clique aqui')

        # adicionando os widgets ao layout
        layout.add_widget(label)
        layout.add_widget(botao)

        # retornando o layout como a interface gráfica da aplicação

        return layout
                                                                                                                                        
                                                                                                                                    # inicializando a aplicação

if __name__ == '__main__':
    os.environ['DISPLAY'] = ':99'
    os.system('Xvfb :99 -screen 0 1024x768x24 &')
    MeuApp().run()







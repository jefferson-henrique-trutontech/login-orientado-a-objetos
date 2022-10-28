import PySimpleGUI as sg
import sqlite3 as sq


class Database():
    def __init__(self, banco):
        self.con = sq.connect(banco)
        self.cur = self.con.cursor()


class App(sg.Window):
    def __init__(self, **kwargs):
        self.title = 'APLICATIVO DE LOGIN'
        self.layout = self.templateLayout()
        self.database = Database('login.db')
        super().__init__(self.title, self.layout, **kwargs)
        self.iniciarApp()

    def iniciarApp(self):
        while True:
            self.ev, self.vl = self.read()

            if self.ev == sg.WIN_CLOSED:
                break

    def templateLayout(self):

        layout = [
            [sg.Text('APLICATIVO DE LOGIN')],
            [sg.Text('User: '), sg.Input(key='inpNome', expand_x=True)],
            [sg.Text('Pass: '), sg.Input(key='inpSenha', password_char='*', expand_x=True)],
            [sg.Text('', expand_x=True), sg.Button('Entrar')]
        ]

        return layout


janela = App()

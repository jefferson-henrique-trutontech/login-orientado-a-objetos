import PySimpleGUI as sg
import sqlite3 as sq


class Database():
    def __init__(self, banco):
        self.con = sq.connect(banco)
        self.cur = self.con.cursor()
        self.users = self.cur.execute("SELECT * FROM usuarios").fetchall()


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
            elif self.ev == 'Entrar':
                for user in self.database.users:
                    name = user[1]
                    passw = user[2]
                    login = name.lower() == self.vl['inpNome'].lower() and passw == self.vl['inpSenha']
                    if login:
                        self['output'].update('Logado com sucesso')
                        break
                    else:
                        self['output'].update('Erro no login')

                self['inpNome'].update('')
                self['inpSenha'].update('')
                pass

    def templateLayout(self):

        layout = [
            [sg.Text('APLICATIVO DE LOGIN')],
            [sg.Text('User: '), sg.Input(key='inpNome', expand_x=True)],
            [sg.Text('Pass: '), sg.Input(key='inpSenha',
                                         password_char='*', expand_x=True)],
            [sg.Text('',key='output', expand_x=True), sg.Button('Entrar')]
        ]

        return layout


janela = App()

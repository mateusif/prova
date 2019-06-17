from tkinter import *
import sqlite3
conexao = sqlite3.connect("usuarios.db")
Cursor= conexao.cursor()

def login():
    nome = usuario.get()
    password = senha.get()
    Cursor.execute("select * from usuarios")
    resultado=Cursor.fetchall()
    for registro in resultado:
        if(registro[0]!=nome):
            lb2["text"] = ('Usuário não existe')    
            break
        else:
            if(registro[1]!=password):
               lb2["text"] = ('Senha Incorreta')    
               break
            else:
               lb2["text"] = ('Acesso autorizado')    
               janela2 = Tk()
               janela2.title("Sistema Escola")
               janela2.geometry('500x400+200+200')
               janela2.mainloop()
               break

janela = Tk()
janela.title("Sistema Escola")
janela.geometry('500x400+200+200')

labelUsuario = Label(janela, text= "Usuário")
labelUsuario.place(x=70, y=80)
usuario = Entry(janela, width=20, fg="blue")
usuario.place(x=115, y=80)

labelSenha = Label(janela, text= "Senha")
labelSenha.place(x=70, y=110)
senha = Entry(janela, width=20, fg="blue")
senha.place(x=115, y=110)

bt = Button (janela, width=20, text= "Confirma", command=login)
bt.place(x=80 , y=200)
lb2= Label(janela, fg="red", font=("Verdana", 10))
lb2.place(x=100, y=250)

janela.mainloop()
Cursor.close()
conexao.close()
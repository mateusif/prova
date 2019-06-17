from tkinter import *
import sqlite3
conexao = sqlite3.connect("usuarios.db")
Cursor= conexao.cursor()
Cursor.execute('create table if not exists usuarios(nome text, senha text)')



def verificaSenha(password, password2):
    if(password == password2):
        if(len(password) < 8):
            lb2["text"] = "Senha não foi aceita! Senha deverá ter 8 dígitos"
            return False
        if(password.islower() == False):
            lb2["text"] = "Senha não foi aceita! Letras somente minúsculas"
            return False
        if (set('[~!@#$%^&*()_+{}":;\']+$').intersection(password)):
            lb2["text"] = "Senha não aceita caracteres especiais!"
            return False
        if(temNumeros(password) == False or password.isdigit()):
            lb2["text"] = "Senha não foi aceita! Deverá ter letras e números"
            return False
        lb2["text"] = ('senha informada foi aceita')
        return True
    else:
        lb2["text"] = ('senhas não coincidem')

def temNumeros(varSenha):
    return any(char.isdigit() for char in varSenha)

def cadastra():
    nome = usuario.get()
    password = senha.get()
    password2 = senha2.get()
    if(verificaSenha(password, password2)):
       Cursor.execute('insert into usuarios(nome, senha) values(?, ?)', (nome, password))
       conexao.commit()
       #Cursor.execute("select * from usuarios")
       #resultado=Cursor.fetchall()
       #print(resultado) 
     
    else:
        print("ERRO")
        

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

labelSenha2 = Label(janela, text= "Confirme a senha")
labelSenha2.place(x=50, y=140)
senha2 = Entry(janela, width=20, fg="blue")
senha2.place(x=150, y=140)

bt = Button (janela, width=20, text= "Confirma", command=cadastra)
bt.place(x=80 , y=200)
lb2= Label(janela, fg="red", font=("Verdana", 10))
lb2.place(x=100, y=250)



janela.mainloop()
Cursor.close()
conexao.close()
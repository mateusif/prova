from tkinter import *
import tkinter as tk
import sqlite3

janela = tk.Tk()
conexao = sqlite3.connect("usuarios.db")
Cursor = conexao.cursor()
Cursor.execute('create table if not exists alunos(nome text, cidade text, curso text)')

v = tk.IntVar()
def cadastra():
    nome = aluno.get()
    city = cidade.get()
    var = v.get()
    cur = ''
    if(var == 1):
        cur ='Informática'
    elif (var == 2):
        cur = 'Eletromecênica'
    elif (var == 3):
        cur = 'Edificações'    
    Cursor.execute('insert into alunos(nome, cidade, curso) values(?, ?, ?)', (nome, city, cur))
    conexao.commit()

    Cursor.execute("select * from alunos order by nome")
    resultado=Cursor.fetchall()
    #listbox = Listbox(janela)  
    for registro in resultado:
     #  listbox.insert(1, registro)
     print(registro)

    Cursor.execute("select * from alunos order by curso")
    resultado=Cursor.fetchall()
    for registro in resultado:
     print(registro)

janela.title("Sistema Escola")
janela.geometry('500x400+200+200')

labelAluno = Label(janela, text= "Nome do Aluno")
labelAluno.place(x=70, y=80)
aluno = Entry(janela, width=20, fg="blue")
aluno.place(x=160, y=80)

labelCidade = Label(janela, text= "Cidade do Aluno")
labelCidade.place(x=70, y=110)
cidade = Entry(janela, width=20, fg="blue")
cidade.place(x=162, y=110)

tk.Radiobutton(janela, text="Informática", padx = 70,  variable=v, value=1).pack(anchor=tk.W)
tk.Radiobutton(janela, text="Eletromecânica", padx = 70, variable=v, value=2).pack(anchor=tk.W)
tk.Radiobutton(janela, text="Edificações", padx = 70, variable=v, value=3).pack(anchor=tk.W)



bt = Button (janela, width=20, text= "Confirma", command=cadastra)
bt.place(x=80 , y=200)
lb2= Label(janela, fg="red", font=("Verdana", 10))
lb2.place(x=100, y=250)



janela.mainloop()
Cursor.close()
conexao.close()

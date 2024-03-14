from escola import Escola
from aluno import Aluno
from tkinter import *
from tkinter import ttk, messagebox

class App:
    def __init__(self, nome: str, endereco: str):
        self.escola = Escola(nome, endereco)
        self.janela = Tk()
        self.janela.title(f"Sistema - {self.escola.nome}")

        # Label
        self.label_matricula = Label(self.janela, text='Matricula',
                                     font='Tahoma 14 bold', fg='red')
        self.label_matricula.grid(row=0, column=0)

        # Entry
        self.txt_matricula = Entry(self.janela, font='Tahoma 14',
                                   width=27, state=DISABLED)
        self.txt_matricula.grid(row=0, column=1)

                # Label
        self.label_nome = Label(self.janela, text='Nome',
                                     font='Tahoma 14 bold', fg='red')
        self.label_nome.grid(row=1, column=0)

        # Entry
        self.txt_nome = Entry(self.janela, font='Tahoma 14',
                                   width=27)
        self.txt_nome.grid(row=1, column=1)


        self.label_idade = Label(self.janela, text='Idade',
                                     font='Tahoma 14 bold', fg='red')
        self.label_idade.grid(row=2, column=0)

        # Entry
        self.txt_idade = Entry(self.janela, font='Tahoma 14',
                                   width=27)
        self.txt_idade.grid(row=2, column=1)


        self.label_curso = Label(self.janela, text='Curso',
                                     font='Tahoma 14 bold', fg='red')
        self.label_curso.grid(row=3, column=0)

        self.combo_curso = ttk.Combobox(self.janela,
                                        font='Tahoma 14 bold',
                                        values=['Java', 'Python',
                                                'Javascript', 
                                                'Node'],
                                        width=21, state='readonly')
        self.combo_curso.grid(row=3, column=1)

        self.label_nota = Label(self.janela, text='Nota',
                                     font='Tahoma 14 bold', fg='red')
        self.label_nota.grid(row=4, column=0)

        # Entry
        self.txt_nota = Entry(self.janela, font='Tahoma 14',
                                   width=27)
        self.txt_nota.grid(row=4, column=1)


        self.btn_adicionar = Button(self.janela, text='Adicionar',
                                    font='Tahoma 12 bold', width=7,
                                    fg='red',
                                    command=self.addAluno)
        self.btn_adicionar.grid(row=5, column=0)


        self.btn_editar = Button(self.janela, text='Editar',
                                    font='Tahoma 12 bold', width=7,
                                    fg='red', command=self.editarAluno)
        self.btn_editar.grid(row=5, column=1)

        self.btn_excluir = Button(self.janela, text='Excluir',
                                    font='Tahoma 12 bold', width=7,
                                    fg='red', command=self.excluirAluno)
        self.btn_excluir.grid(row=5, column=2)

        self.frame = Frame(self.janela)
        self.frame.grid(row=6, column=0, columnspan=3)
        self.colunas = ['Matricula', 'Nome', 'Idade', 'Curso', 'Nota']
        self.tabela = ttk.Treeview(self.frame, columns=self.colunas,
                                   show='headings')
        for coluna in self.colunas:
            self.tabela.heading(coluna, text=coluna)
            self.tabela.column(coluna, width=110)
        
        # bind
        self.tabela.bind('<ButtonRelease-1>', self.selecionarAluno)
        self.tabela.pack()
        # resizable
    



        self.atualizarTabela()
        self.janela.mainloop()

    def atualizarTabela(self):
        # limpar a tabela
        for linha in self.tabela.get_children():
            self.tabela.delete(linha)

        for aluno in self.escola.alunos:
            self.tabela.insert('', END, values=(aluno.matricula,
                                                aluno.nome,
                                                aluno.idade,
                                                aluno.curso,
                                                aluno.nota))
    def limparCampos(self):
        self.txt_matricula.config(state=NORMAL)
        self.txt_matricula.delete(0, END)
        self.txt_matricula.config(state=DISABLED)
        self.txt_nome.delete(0, END)
        self.txt_idade.delete(0, END)
        self.combo_curso.set('')
        self.txt_nota.delete(0, END)
    
    def selecionarAluno(self, event):
        linha_selecionada = self.tabela.selection()[0]
        item = self.tabela.item(linha_selecionada)['values']
        self.limparCampos()
        # Inserindo os valores
        self.txt_matricula.config(state=NORMAL)
        self.txt_matricula.insert(0, item[0])
        self.txt_matricula.config(state=DISABLED)
        self.txt_nome.insert(0, item[1])
        self.txt_idade.insert(0, item[2])
        self.combo_curso.set(item[3])
        self.txt_nota.insert(0, item[4])

    def criarAluno(self):
        # factory
        nome = self.txt_nome.get()
        idade = int(self.txt_idade.get())
        curso = self.combo_curso.get()
        nota = float(self.txt_nota.get())
        aluno = Aluno(nome, idade, curso, nota)
        return aluno
    
    def addAluno(self):
        aluno = self.criarAluno()
        self.escola.cadastrarAluno(aluno)
        messagebox.showinfo('Sucesso!',
                             'Aluno cadastrado com sucesso!')
        self.atualizarTabela()
        self.limparCampos()
    
    def editarAluno(self):
        aluno = self.criarAluno()
        aluno.matricula = self.txt_matricula.get()
        self.escola.editarAluno(aluno)
        self.limparCampos()
        self.atualizarTabela()
        messagebox.showinfo('Sucesso !', 'Dados alterados com sucesso.')    

    def excluirAluno(self):
        matricula = self.txt_matricula.get()
        self.escola.deletarAluno(matricula)
        self.limparCampos()
        self.atualizarTabela()
        messagebox.showinfo('Sucesso !', 'Dados alterados com sucesso.')

App('Infinity school', 'Av Santos dumont')
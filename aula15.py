
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

alunos = [
    {
        "matricula": 1,
        "nome": "Jonas Lopes",
        "idade": 18,
        "curso": "Javascript",
        "novato": False
    }
]
matricula_atual = 1
index = 0


def atualizarTabela() -> None:
    # Limpando a tabela
    # get_children() -> Retorna as linhas da tabela
    for linha in tabela.get_children():
        tabela.delete(linha)

    for aluno in alunos:
        tabela.insert("", END, values=(aluno["matricula"],
                                       aluno["nome"],
                                       aluno["idade"],
                                       aluno["curso"],
                                       aluno["novato"]))


def adicionarAluno() -> None:
    global matricula_atual
    matricula_atual += 1
    nome = txtNome.get()
    idade = int(txtIdade.get())
    curso = comboCursos.get()
    novato = opcao.get()

    aluno = {
        "matricula": matricula_atual,
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "novato": novato
    }
    messagebox.showinfo("Sucesso!", "Aluno adicionado com sucesso!")
    alunos.append(aluno)

    # Limpar os campos
    limparCampos()
    atualizarTabela()


def limparCampos() -> None:
    #como habilitar o campo
    txtMatricula.config(state=NORMAL)
    txtMatricula.delete(0, END)
    txtMatricula.config(state=DISABLED)

    txtNome.delete(0, END)
    txtIdade.delete(0, END)
    comboCursos.set("")
    opcao.set(False)


def preencherCampos(event) -> None:
    linha_selecionada = tabela.selection()  # I001
    global index
    index = tabela.index(linha_selecionada)
    aluno = alunos[index]
    limparCampos()
    txtMatricula.config(state=NORMAL)
    txtMatricula.insert(END, str(aluno['matricula']))
    txtMatricula.config(state=DISABLED)
    txtNome.insert(END, aluno["nome"])
    txtIdade.insert(END, str(aluno["idade"]))
    comboCursos.set(aluno["curso"])

def editarAluno() -> None:
    # pegando as informaçoes dos campos
    nome = txtNome.get()
    idade = int(txtIdade.get())
    curso = comboCursos.get()
    novato = opcao.get()

    opcaoSelecionada = messagebox.askyesno("Tem certeza?", "Deseja alterar os dados")
    if opcaoSelecionada:
        #pegar aluno
        aluno = alunos[index]
        aluno["nome"]= nome
        aluno["idade"]= idade
        aluno["curso"]= curso
        aluno["novato"]= novato
        messagebox.showinfo("Sucesso", "Dados alterados com sucesso!")
    limparCampos()
    atualizarTabela()

def deletarAluno() -> None:
    opcaoSelecionada = messagebox.askyesno("Tem certeza?", "Deseja Remover o Aluno?")
    if opcaoSelecionada:
        alunos.remove(alunos[index])
        messagebox.showinfo("Sucesso!", "Dados apagados com sucesso!")
    limparCampos()
    atualizarTabela()


janela = Tk()

janela.title("Alunos - Infinity")

# janela.geometry("800x650")

labelMatricula = Label(janela, text="Matricula:", font="Tahoma 18 bold",
                       fg="red")
labelMatricula.grid(row=0, column=0)

txtMatricula = Entry(janela, font="Tahoma 18", width=26,
                     state=DISABLED)
txtMatricula.grid(row=0, column=1)

labelNome = Label(janela, text="Nome:", font="Tahoma 18 bold", fg="red")
labelNome.grid(row=1, column=0)

txtNome = Entry(janela, font="Tahoma 18", width=26)
txtNome.grid(row=1, column=1)

labelIdade = Label(janela, text="Idade:", font="Tahoma 18 bold", fg="red")
labelIdade.grid(row=2, column=0)

txtIdade = Entry(janela, font="Tahoma 18", width=26)
txtIdade.grid(row=2, column=1)

labelCurso = Label(janela, text="Curso:", font="Tahoma 18 bold", fg="red")
labelCurso.grid(row=3, column=0)

cursos = ["Javascript", "Python", "React", "NodeJs"]
comboCursos = ttk.Combobox(janela, font="Tahoma 18", values=cursos,
                           width=24)
comboCursos.grid(row=3, column=1, sticky=W)

labelNovato = Label(janela, text="Novato?", font="Tahoma 18 bold", fg="red")
labelNovato.grid(row=4, column=0)

opcao = BooleanVar(value=False)
checkNovato = ttk.Checkbutton(janela, width=26, variable=opcao)
checkNovato.grid(row=4, column=1, sticky=W)

btnAdicionar = Button(janela, text="Adicionar", font="Tahoma 16", fg="red",
                      height=1, command=adicionarAluno)
btnAdicionar.grid(row=5, column=0)

btnEditar = Button(janela, text="Editar", font="Tahoma 16", fg="red",
                   height=1, command=editarAluno)
btnEditar.grid(row=5, column=1)

btnExcluir = Button(janela, text="Excluir", font="Tahoma 16", fg="red",
                    height=1, command=deletarAluno)
btnExcluir.grid(row=5, column=2)

colunas = ["Matricula", "Nome", "Idade", "Curso", "Novato"]
tabela = ttk.Treeview(janela, columns=colunas, show="headings")
for coluna in colunas:
    tabela.heading(coluna, text=coluna)
    tabela.column(coluna, width=110)

tabela.grid(row=6, columnspan=3)
tabela.bind("<ButtonRelease-1>", preencherCampos)

atualizarTabela()
janela.mainloop()

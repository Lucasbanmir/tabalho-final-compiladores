import tkinter as tk
from tkinter import filedialog
from antlr4 import *
from gen.trabalhoFinal_lucasLexer import trabalhoFinal_lucasLexer
from gen.trabalhoFinal_lucasParser import trabalhoFinal_lucasParser
from myListener import trabalhoFinal_lucasListener

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.create_widgets()

        # Configurando a janela principal
        self.title("Compilador do Lucas")
        self.geometry("500x300")

    def create_widgets(self):
        self.text_widget = tk.Text(self, wrap="word")
        self.text_widget.pack(fill="both", expand=True)

        self.run_button = tk.Button(self, text="Executar", command=self.run_code)
        self.run_button.pack()

        # Criando a barra de menus
        self.menu_bar = tk.Menu(self)

        # Criando o menu Arquivo
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Novo", command=self.novo_arquivo)
        self.file_menu.add_command(label="Abrir", command=self.abrir_arquivo)
        self.file_menu.add_command(label="Salvar", command=self.salvar_arquivo)

        self.menu_bar.add_cascade(label="Arquivo", menu=self.file_menu)

        self.menu_bar.add_command(label="Executar", command=self.run_code)

        self.menu_bar.add_cascade(label="Sair", command=self.quit)

        # Adicionando a barra de menus à janela principal
        self.config(menu=self.menu_bar)

    def novo_arquivo(self):
        # Limpa o conteúdo do widget Text
        self.text_widget.delete("1.0", tk.END)

    def abrir_arquivo(self):
        # Abre uma janela de diálogo para escolher um arquivo
        arquivo = filedialog.askopenfilename()

        # Carrega o conteúdo do arquivo no widget Text
        try:
            with open(arquivo, "r") as f:
                conteudo = f.read()
                self.text_widget.delete("1.0", tk.END)
                self.text_widget.insert("1.0", conteudo)
        except:
            tk.messagebox.showerror("Erro", "Não foi possível abrir o arquivo.")

    def salvar_arquivo(self):
        # Abre uma janela de diálogo para escolher o nome do arquivo
        arquivo = filedialog.asksaveasfilename()

        # Salva o conteúdo do widget Text no arquivo
        try:
            with open(arquivo, "w") as f:
                conteudo = self.text_widget.get("1.0", tk.END)
                f.write(conteudo)
        except:
            tk.messagebox.showerror("Erro", "Não foi possível salvar o arquivo.")

    def run_code(self):
        code = self.text_widget.get("1.0", tk.END)
        file = InputStream(code)

        # parte lexica
        lexer = trabalhoFinal_lucasLexer(file)
        streams = CommonTokenStream(lexer)

        # parte analise sintatica
        parser = trabalhoFinal_lucasParser(streams)
        tree = parser.prog()

        # parte analise semantica
        l = trabalhoFinal_lucasListener()
        walker = ParseTreeWalker()
        walker.walk(l, tree)

app = App()
app.mainloop()
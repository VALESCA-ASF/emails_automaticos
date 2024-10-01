import smtplib
import sqlite3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import ttk

# Defina suas configurações de e-mail aqui
usuario_email = ''  # Altere para o seu e-mail
senha_email = ''  # Altere para sua senha de aplicativo

# Função para criar o banco de dados e tabela de destinatários (se não existir)
def inicializar_db():
    conexao = sqlite3.connect('destinatarios.db')
    cursor = conexao.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS destinatarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    )
    ''')
    conexao.commit()
    conexao.close()

# Função para adicionar destinatário no banco de dados
def adicionar_destinatario(nome, email):
    conexao = sqlite3.connect('destinatarios.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO destinatarios (nome, email) VALUES (?, ?)", (nome, email))
    conexao.commit()
    conexao.close()
    carregar_destinatarios()

# Função para carregar destinatários e preencher o combo box
def carregar_destinatarios():
    conexao = sqlite3.connect('destinatarios.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT nome, email FROM destinatarios")
    destinatarios = cursor.fetchall()
    conexao.close()

    destinatario_cb['values'] = [f"{nome} <{email}>" for nome, email in destinatarios]

# Função para enviar o e-mail
def enviar_email():
    try:
        servidor_smtp = 'smtp.titan.email'
        porta_smtp = 587
        destinatario = destinatario_entry.get()
        assunto = assunto_entry.get()
        corpo_email = corpo_entry.get("1.0", END)

        # Criando a mensagem
        msg = MIMEMultipart()
        msg['From'] = usuario_email
        msg['To'] = destinatario
        msg['Subject'] = assunto
        msg.attach(MIMEText(corpo_email, 'plain'))

        # Anexar arquivo se houver
        caminho_arquivo = anexo_path.get()
        if caminho_arquivo:
            with open(caminho_arquivo, 'rb') as anexo:
                parte = MIMEBase('application', 'octet-stream')
                parte.set_payload(anexo.read())
                encoders.encode_base64(parte)
                parte.add_header('Content-Disposition', f'attachment; filename={caminho_arquivo.split("/")[-1]}')
                msg.attach(parte)

        # Enviar o e-mail
        with smtplib.SMTP(servidor_smtp, porta_smtp) as servidor:
            servidor.starttls()
            servidor.login(usuario_email, senha_email)
            servidor.sendmail(usuario_email, destinatario, msg.as_string())

        messagebox.showinfo("Sucesso", "E-mail enviado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao enviar o e-mail: {str(e)}")

# Função para selecionar o arquivo
def selecionar_arquivo():
    arquivo = filedialog.askopenfilename()
    anexo_path.set(arquivo)

# Função para adicionar novo destinatário ao banco
def salvar_destinatario():
    nome = nome_entry.get()
    email = novo_destinatario_entry.get()
    if nome and email:
        adicionar_destinatario(nome, email)
        messagebox.showinfo("Sucesso", "Destinatário salvo!")
    else:
        messagebox.showwarning("Atenção", "Nome e e-mail não podem estar vazios!")

# Criando a interface gráfica
janela = Tk()
janela.title("Envio de E-mails Automáticos")
janela.geometry("600x500")
janela.configure(bg='#2E2E2E')  # Cor de fundo escura

# Inicializar o banco de dados
inicializar_db()

# Rótulos e campos de entrada
Label(janela, text="Remetente", bg='#2E2E2E', fg='white').grid(row=0, column=0, padx=10, pady=10)
remetente_entry = Entry(janela, width=50)
remetente_entry.insert(0, usuario_email)  # Preenche automaticamente
remetente_entry.config(state='readonly')  # Torna o campo somente leitura
remetente_entry.grid(row=0, column=1)

Label(janela, text="Destinatário", bg='#2E2E2E', fg='white').grid(row=1, column=0, padx=10, pady=10)
destinatario_entry = Entry(janela, width=50)
destinatario_entry.grid(row=1, column=1)

Label(janela, text="Assunto", bg='#2E2E2E', fg='white').grid(row=2, column=0, padx=10, pady=10)
assunto_entry = Entry(janela, width=50)
assunto_entry.grid(row=2, column=1)

Label(janela, text="Corpo do e-mail", bg='#2E2E2E', fg='white').grid(row=3, column=0, padx=10, pady=10)
corpo_entry = Text(janela, height=5, width=38)
corpo_entry.grid(row=3, column=1)

# Campo de anexo
anexo_path = StringVar()
Label(janela, text="Anexo", bg='#2E2E2E', fg='white').grid(row=4, column=0, padx=10, pady=10)
Entry(janela, width=40, textvariable=anexo_path).grid(row=4, column=1)
Button(janela, text="Selecionar Arquivo", command=selecionar_arquivo, bg='#002765', fg='white', activebackground='#003C9A').grid(row=4, column=2)

# Combo box de destinatários
Label(janela, text="Selecionar Destinatário", bg='#2E2E2E', fg='white').grid(row=5, column=0, padx=10, pady=10)
destinatario_cb = ttk.Combobox(janela, width=47)
destinatario_cb.grid(row=5, column=1)
Button(janela, text="Usar Destinatário", command=lambda: destinatario_entry.insert(0, destinatario_cb.get()), bg='#002765', fg='white', activebackground='#003C9A').grid(row=5, column=2)

# Campos para adicionar novo destinatário
Label(janela, text="Novo Destinatário", bg='#2E2E2E', fg='white').grid(row=6, column=0, padx=10, pady=10)
nome_entry = Entry(janela, width=20)
nome_entry.grid(row=6, column=1, sticky=W)

novo_destinatario_entry = Entry(janela, width=50)
novo_destinatario_entry.grid(row=6, column=1)

Button(janela, text="Salvar Destinatário", command=salvar_destinatario, bg='#002765', fg='white', activebackground='#003C9A').grid(row=6, column=2, padx=10, pady=10)

# Botão para enviar o e-mail
Button(janela, text="Enviar E-mail", command=enviar_email, bg='#002765', fg='white', activebackground='#003C9A').grid(row=7, column=1, pady=20)

# Carregar destinatários salvos no banco
carregar_destinatarios()

# Iniciar a interface gráfica
janela.mainloop()

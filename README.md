# Envio de E-mails Automáticos

Este projeto consiste em uma aplicação em Python para o envio automatizado de e-mails. A aplicação permite que você salve destinatários em um banco de dados e envie e-mails com ou sem anexos. 

## Funcionalidades

- **Interface Gráfica**: A aplicação possui uma interface gráfica intuitiva desenvolvida com Tkinter, com um design escuro e botões iluminados.
- **Banco de Dados**: Os destinatários são salvos em um banco de dados SQLite para fácil acesso e reutilização.
- **Envio de E-mails**: Envio de e-mails com suporte para anexos.
- **Seleção de Destinatários**: Possibilidade de selecionar destinatários previamente salvos no banco de dados.

## Requisitos

- Python 3.x
- Bibliotecas: `smtplib`, `sqlite3`, `email`, `tkinter`

## Como Usar

1. **Instalação**:
   - Clone este repositório para sua máquina local.
   - Crie um ambiente virtual chamado `email_virtual`:
     ```bash
     python -m venv email_virtual
     ```
   - Ative o ambiente virtual:
     - No Windows:
       ```bash
       email_virtual\Scripts\activate
       ```
     - No macOS/Linux:
       ```bash
       source email_virtual/bin/activate
       ```
   - Instale as dependências necessárias (se houver).

2. **Configuração**:
   - No código, insira seu e-mail e senha de aplicativo nas variáveis `usuario_email` e `senha_email`, respectivamente.

3. **Execução**:
   - Execute o arquivo Python para iniciar a aplicação:
     ```bash
     python seu_arquivo.py
     ```

## Importância do Ambiente Virtual

O uso de um ambiente virtual é importante para isolar as dependências do seu projeto. Isso evita conflitos entre bibliotecas que podem ser necessárias para diferentes projetos, permitindo que você mantenha um ambiente limpo e controlado.


## Contribuições

Sinta-se à vontade para contribuir com melhorias ou novas funcionalidades. Faça um fork deste repositório, crie uma branch para suas alterações e envie um pull request.

## Licença

Este projeto é de uso livre. Se você utilizar o código, por favor, mantenha os créditos.


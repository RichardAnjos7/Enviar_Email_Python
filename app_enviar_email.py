# Antes de executar o script você precisa alimentar a planinha "emails.xlsx" antes!
# O caminho do seu anexo deve está correto.
# Criar uma senha no gmail para usar no app e colocar a senha na linha 64 "server.login" para efetuar login.


import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Lendo a Planilha (Banco de Dados)
emails = pd.read_excel('./emails.xlsx')

# Loop por linhas
for index, email in emails.iterrows():

    msg = MIMEMultipart()
    # Email de onde vai ser enviado
    msg['From'] = 'seu_email@gmail.com'

    # Email para quem vai ser enviado já puxando da planinha "emails.xlsx", não precisa digitar o e-mail do destinatário
    msg['To'] = email['email']

    # Assunto do e-mail que já é puxado do banco de dados da planilha "emails.xlsx"
    msg['Subject'] = email['cargo']
 
    # Corpo da mensagem
    message = f"""\
Olá, {email['nome']}

Espero que você se encontre bem.

Gostaria de aproveitar esta oportunidade para compartilhar um pouco sobre minha jornada como Técnico de Informática.

Atenciosamente,

Seu nome
Whatsapp (00)99999-9999
"""
    msg.attach(MIMEText(message, 'plain'))

    # Adicionando o local do anexo
    pdf = 'C:\\Pasta\\Python\\Curriculo.pdf'

    with open(pdf, 'rb') as attachment:
        att = MIMEBase('application', 'octet-stream')
        att.set_payload(attachment.read())
        encoders.encode_base64(att)

        att.add_header('Content-Disposition',
                       'attchment; filename=curriculo.pdf')
        attachment.close()

    msg.attach(att)

    # Iniciando a conexão com o servidor:
    server = smtplib.SMTP('smtp.gmail.com', port=587)
    server.starttls()

    # Login e senha de app do Gmail
    # Link de como criar senha de app https://www.youtube.com/watch?v=nFbZLX2U-5k
    server.login('seu_email@gmail.com', 'senha_app')

    # Enviando o Email
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    # Fechando o servidor
    server.quit()

# Mensagem que aparecerá no console após confirmar de que foi enviado o e-mail.
input('\n E-mail enviado com sucesso! Boa sorte:)')

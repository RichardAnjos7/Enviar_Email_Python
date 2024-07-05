# Script de Envio de E-mails

Este script em Python permite enviar e-mails para uma lista de destinatários a partir de um banco de dados (Planilha do Excel). Ele utiliza a biblioteca `smtplib` para se conectar a um servidor SMTP (no exemplo, usamos o Gmail) e envia e-mails com anexos.


## Pré-requisitos

Antes de executar o script, certifique-se de ter o seguinte:

1. Uma planilha Excel chamada `emails.xlsx` ou o nome que desejar contendo as seguintes colunas:
    - `nome`: Nome do destinatário.
    - `email`: Endereço de e-mail do destinatário.
    - `cargo`: Assunto do e-mail.

2. Um arquivo PDF chamado `Curriculo.pdf` ou de sua preferência que será anexado aos e-mails.

3. Uma conta de e-mail do Gmail com a autenticação de dois fatores ativada. Você também precisará gerar uma senha de aplicativo para usar no script. Veja aqui como criar uma senha de aplicativo, acesse https://www.youtube.com/watch?v=nFbZLX2U-5k


## Como usar

1. Abra o terminal ou prompt de comando e navegue até o diretório onde o script está localizado.

2. Execute o script com o seguinte comando:
   ```
   python nome_do_script.py
   ```

3. O script lerá os dados da planilha emails.xlsx, enviará os e-mails e exibirá uma mensagem de sucesso no console.

4. Verifique a caixa de saída do e-mail para confirmar o envio.


## Observações

1. Lembre-se de substituir 'seu_email@gmail.com' e 'senha_app' pelas suas próprias credenciais de e-mail.

2. Certifique-se de que o arquivo Curriculo.pdf esteja no caminho especificado no script.

3. Caso queira usar outro provedor de e-mail, ajuste as configurações do servidor SMTP no script.


## Criar arquivo executável do script

1. **Instalação do PyInstaller**:
   - Abra um terminal ou prompt de comando.
   - Execute o seguinte comando para instalar o PyInstaller:
     ```
     pip install pyinstaller
     ```

2. **Navegação para o Diretório do Script**:
   - Navegue até o diretório onde seu script Python está localizado. Você pode usar o comando cd para mudar de diretório.

3. **Criação do Executável**:
   - No terminal, execute o seguinte comando para criar o executável:
     ```
     pyinstaller --onefile nome_do_script.py
     ```

Substitua nome_do_script.py pelo nome real do seu arquivo Python. O PyInstaller criará um único arquivo executável (.exe no Windows) que pode ser executado em qualquer computador sem a necessidade de ter o Python ou bibliotecas instaladas.


## Créditos

Este projeto foi criado e inspirado por mim mesmo. Estou desempregado e sei como é cansativo enviar currículos todos os dias, anexar arquivos e escrever mensagens para destinatários diferentes. Por isso, desenvolvi um script que automatiza o envio de e-mails com meu currículo anexado, mensagem personalizada e destinatário específico.

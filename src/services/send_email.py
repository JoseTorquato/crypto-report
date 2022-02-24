import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Email:
    
    SMTP = 'smtp.gmail.com'
    PORT = 465
    #fafixfztousosehr
    #yifgnluwwgtizoik

    def __init__(self, email="cryptocoinreports@gmail.com", token="yifgnluwwgtizoik", remetente="cryptocoinreports@gmail.com"):
        self._email = email
        self._token = token
        self._remetente = remetente
    
    def send(self, messagem):
        print(messagem)
        message_html = f'''
        <html>
        <head></head>
        <body>
            <p>Olá!<br>
            Como você está?<br>
            Aqui está o report do dia {messagem}
            </p>
        </body>
        </html>
        '''
        print('Criando mensagem...')
        email_msg = MIMEMultipart()
        email_msg['From'] = self._remetente
        email_msg['To'] = "jltorquato12@gmail.com"
        email_msg['Subject'] = 'Report Daily'
        print('Adicionando texto...')
        email_msg.attach(MIMEText(message_html, 'html'))
        server = smtplib.SMTP_SSL(self.SMTP, self.PORT)
        server.login(self._email, self._token)
        print('Enviando mensagem...')
        server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
        print('Mensagem enviada!')
        server.quit()

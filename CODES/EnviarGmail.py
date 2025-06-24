#Bibliotecas
import smtplib
import email.message

def enviar_email():  
    corpo_email = """
    <p>Muito Obrigado Por Testar o Codigo </p>
    <p> Agora Faz o L e o Pix </p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Agradecimento"
    msg['From'] = 'caerlosfreefire@gmail.com'
    msg['To'] = 'caerlosfreefire@gmail.com'
    password = 'wzqt dnwa iatc yeqk' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


# In[ ]:


enviar_email()


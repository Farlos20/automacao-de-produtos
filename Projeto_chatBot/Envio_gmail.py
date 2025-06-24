# Bibliotecas
import smtplib
import email.message


def enviar_email(email_destino):  
    corpo_email = """
    <p> 🎉Muito Obrigado Por Testar o Codigo  Zé da manga  </p>
    <p> Agora Faz o L e o Pix 💰💰 </p>
    <p> 🎼 Aproveite esta playlist para programar: </p>
    <p><a href="https://youtu.be/4wDcSEKeZlo?si=01uACy-IOsOZUqA-">Clique aqui</a></p>
    <p> deixe sua opinião deste codigo no meu zap<p>
    <h1> Segue  o formulario dos clientes conforme pedido Chefe!!</h1>
    <p><a href="https://drive.google.com/file/d/1rAlsv4WYDpALsDSOQE5_17NZGFaR6671/view?usp=sharing">Formulario aqui</a></p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Agradecimento"
    msg['From'] = 'caerlosfreefire@gmail.com'
    msg['To'] = email_destino
    password = 'wzqt dnwa iatc yeqk' 
    msg.add_header('Content-Type', 'text/html')
    
    # Defina o payload antes de converter para string
    msg.set_payload(corpo_email)

    # Aqui você pode converter a mensagem para string e codificá-la
    msg_str = msg.as_string().encode('utf-8')

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    
    print(f"Enviando email para: {msg['To']}")  # para garantir que tem destinatário
    
    # Envie a string codificada
    s.sendmail(msg['From'], [msg['To']], msg_str)
    
    s.quit()


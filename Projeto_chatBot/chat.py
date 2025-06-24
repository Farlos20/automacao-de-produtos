import streamlit as st
import time
from Envio_gmail import enviar_email
from streamlit_autorefresh import st_autorefresh

st.title("Recebimento de Pagamento")
st.write("Siga os passos para receber seu salário:")

if "nome" not in st.session_state:
    st.session_state.nome = ""
if "email" not in st.session_state:
    st.session_state.email = ""
if "etapa" not in st.session_state:
    st.session_state.etapa = 0
if "enviando" not in st.session_state:
    st.session_state.enviando = False
if "enviado" not in st.session_state:
    st.session_state.enviado = False
if "erro_email" not in st.session_state:
    st.session_state.erro_email = False
if "tempo_inicial" not in st.session_state:
    st.session_state.tempo_inicial = 0

def avancar_nome():
    nome = st.session_state.nome_input.strip()
    if nome:
        st.session_state.nome = nome
        st.session_state.etapa = 1

def avancar_email():
    email = st.session_state.email_input.strip()
    if email:
        st.session_state.email = email
        st.session_state.etapa = 2

if st.session_state.etapa == 0:
    st.text_input("Digite seu nome completo", key="nome_input", on_change=avancar_nome)

elif st.session_state.etapa == 1:
    st.text_input("Digite seu email (Gmail)", key="email_input", on_change=avancar_email)

elif st.session_state.etapa == 2:
    st.write(f"Nome: {st.session_state.nome}")
    st.write(f"E-mail: {st.session_state.email}")

    if st.session_state.enviado:
        st.success("Email enviado com sucesso!")
        st.success("Tudo concluído. Obrigado!")

    else:
        if st.session_state.enviando:
            st.button("Enviando email...", disabled=True)
            st.info("Aguarde, estamos enviando seu email...")

            count = st_autorefresh(interval=600, limit=3, key="auto_refresh")

            if time.time() - st.session_state.tempo_inicial >= 1.8:
                st.session_state.enviado = True
                st.session_state.enviando = False
                st.session_state.etapa = 3

        else:
            enviar = st.button("Enviar email")
            if enviar:
                email = st.session_state.email
                if "@" in email and email.endswith(".com"):
                    st.session_state.enviando = True
                    st.session_state.tempo_inicial = time.time()
                    try:
                        enviar_email(email)
                        st.session_state.erro_email = False
                    except Exception as e:
                        st.error(f"Erro ao enviar email: {e}")
                        st.session_state.erro_email = True
                        st.session_state.enviando = False
                else:
                    st.error("E-mail inválido! Verifique e tente novamente.")
                    st.session_state.erro_email = True

        if st.session_state.erro_email:
            st.error("E-mail inválido! Verifique e tente novamente.")

elif st.session_state.etapa == 3:
    st.success("Email enviado com sucesso!")
    st.success("Tudo concluído. Obrigado!")

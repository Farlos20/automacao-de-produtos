import streamlit as st
#python -m streamlit run "C:\Users\Carlos\Documents\Python\CODES\chat_site.py"


st.title("here")
st.write("Mensagem de bot")

mensagem_usuario = st.chat_input("escreva aqui")  # Corrigido o nome da variável


if mensagem_usuario:
    st.write("Você escreveu:", mensagem_usuario)

# ❌ print() não funciona como esperado no Streamlit (em vez disso, use st.write)
# print("here")  # Removido ou substituído

st.write("here")  # Substitui o print para aparecer na tela do app

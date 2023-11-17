import streamlit as st
import pandas as pd
from views import View
import time

class AbrirContaUI:
  def main():
    st.header("Abrir Conta no Sistema")
    AbrirContaUI.inserir()
  
  def inserir():
    nome = st.text_input("Informe o nome")
    email = st.text_input("Informe o e-mail")
    fone = st.text_input("Informe o fone")
    senha = st.text_input("Informe a senha")
    if st.button("Inserir"):
      try:
        st.write(nome + email + fone + senha)
        View.cliente_inserir(nome, email, fone, senha)
        st.success("Conta criada com sucesso")
        time.sleep(2)
        st.rerun()
      except ValueError as error:
        st.error(f"Erro: {error}")
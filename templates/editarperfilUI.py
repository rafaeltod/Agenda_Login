import streamlit as st
from views import View
import time

class EditarPerfilUI:

    def main():
        st.header("Editar Perfil")
        EditarPerfilUI.editar_perfil()

    def editar_perfil():
        clientes = View.cliente_listar()
        if st.session_state["cliente_nome"] == clientes[0].get_nome():
            email = st.text_input("E-mail")
            fone = st.text_input("Fone")
            senha = st.text_input("Senha")
            if st.button("Editar"):
                View.editar_perfil(st.session_state["cliente_id"], nome, email, fone, senha)
                st.success('Perfil editado com sucesso!')
                time.sleep(2)
                st.rerun()
        else:
            nome = st.text_input("Nome")
            email = st.text_input("E-mail")
            fone = st.text_input("Fone")
            senha = st.text_input("Senha")
            if st.button("Editar"):
                View.editar_perfil(st.session_state["cliente_id"], nome, email, fone, senha)
                st.success('Perfil editado com sucesso!')
                time.sleep(2)
                st.rerun()
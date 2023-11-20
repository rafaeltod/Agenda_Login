import streamlit as st
import pandas as pd
from views import View
import time

class ConfirmarAgendamentoUI:
    def main():
        st.header("Horários da semana")
        ConfirmarAgendamentoUI.listar_atendimentos()
        ConfirmarAgendamentoUI.confirmar_agendamento()

    def listar_atendimentos():
        agendas = View.listar_naoconfirmados()
        if len(agendas) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            dic = []
            for obj in agendas: dic.append(obj.to_json())
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def confirmar_agendamento():
        horarios = View.listar_naoconfirmados()
        horario = st.selectbox("Selecione o horário", horarios)
        if st.button("Confirmar"):
            View.agenda_atualizar(horario.get_id(), horario.get_data(), True, horario.get_id_cliente(), horario.get_id_servico())
            st.success("Horário confirmado com sucesso")
            time.sleep(2)
            st.rerun()
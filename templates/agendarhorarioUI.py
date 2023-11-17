import streamlit as st
import pandas as pd
from views import View
import time
import datetime
from datetime import datetime
from models.agenda import Agenda
from models.agenda import NAgenda

class AgendarHorarioUI:
  def main():
    st.header("Horários da semana")
    AgendarHorarioUI.listar_semana()
    AgendarHorarioUI.inserir()

  def listar_semana():
    agendas = View.listar_horarios()
    if len(agendas) == 0:
      st.write("Nenhum horário cadastrado")
    else:
      dic = []
      for obj in agendas: dic.append(obj.to_json())
      df = pd.DataFrame(dic)
      st.dataframe(df)

  def inserir():
    id = st.session_state['cliente_id']
    horarios = View.listar_horarios()
    horario = st.selectbox("Selecione o horário", horarios)
    servicos = View.servico_listar()
    servico = st.selectbox("Selecione o serviço", servicos)
    if st.button("Inserir"):
      try:
        View.agenda_inserir(horario, True, id, servico.get_id())
        st.success("Horário inserido com sucesso")
        time.sleep(2)
        st.rerun()
      except ValueError as error:
        st.error(f"Erro: {error}")
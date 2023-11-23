import streamlit as st
import pandas as pd
from views import View
import time

class AgendarHorarioUI:
  def main():
    st.header("Horários da semana")
    AgendarHorarioUI.listar_semana()
    AgendarHorarioUI.agendar()

  def listar_semana():
    agendas = View.listar_horarios()
    if len(agendas) == 0:
      st.write("Nenhum horário cadastrado")
    else:
      dic = []
      for obj in agendas: dic.append(obj.to_json())
      df = pd.DataFrame(dic)
      st.dataframe(df)

  def agendar():
    id = st.session_state['cliente_id']
    horarios = View.listar_horarios()
    horario = st.selectbox("Selecione o horário", horarios)
    servicos = View.servico_listar()
    servico = st.selectbox("Selecione o serviço", servicos)
    if st.button("Alocar"):
      try:
        View.agenda_atualizar(horario.get_id(), horario.get_data(), False, id, servico.get_id())
        st.success("Horário agendado com sucesso")
        time.sleep(2)
        st.rerun()
      except ValueError as error:
        st.error(f"Erro: {error}")
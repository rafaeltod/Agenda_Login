import streamlit as st
import pandas as pd
from views import View

class VisualizarAgendamentoUI:
    def main():
        st.header("Horários da semana")
        VisualizarAgendamentoUI.listar_agendamentos()

    def listar_agendamentos():
        datainicial = st.text_input("Informe a data inicial no formato *dd/mm/aaaa*")
        datafinal = st.text_input("Informe a data final no formato *dd/mm/aaaa*")
        
        if st.button("Visualizar"):
            agendas = View.periodo_informado(datainicial, datafinal, st.session_state["cliente_id"])
            
            if len(agendas) == 0:
                st.write("Nenhum horário cadastrado")
            else:
                dic = []
                for obj in agendas: dic.append(obj.to_json())
                
                df = pd.DataFrame(dic)
                st.dataframe(df)

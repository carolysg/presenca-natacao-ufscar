# Importando bibliotecas
import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

# Criando a conexão
conn = st.connection("gsheets", type=GSheetsConnection)

# Lendo o arquivo
df = conn.read(
    worksheet="Página1",
    usecols=list(range(3)),
    ttl=0
)
df.dropna(how='all', inplace=True)

# Lendo o nome dos atletas
df_atletas = conn.read(
    worksheet="Página2",
    usecols=list(range(1)),
    ttl=0
)
df_atletas.dropna(how='all', inplace=True)

# Criar lista suspensa
atletas = df_atletas['Atletas'].unique()

# Criando o formulário
st.title("Natação UFSCar")
st.subheader("Formulário de presença")
with st.form(key="presenca"):
    data = st.date_input(label="Data de hoje*", format="DD/MM/YYYY")
    nome = st.selectbox("Nome*", options=atletas, index=None, placeholder="Selecione seu nome")
    senha = st.text_input(label="Digite a senha de hoje*")

    st.markdown("**obrigatório*")

    submit = st.form_submit_button(label="Enviar")

    if submit:
        if not data or not nome or not senha:
            st.warning("Preencha todos os dados!")
            st.stop()
        elif datetime.strftime(data, "%d/%m/%Y") in df[df['Nome']==nome]['Data'].values:
            st.warning("Você já preencheu o formulário hoje!")
            st.stop()
        else:
            atleta_data = pd.DataFrame(
                [
                    {
                        "Data": datetime.strftime(data, "%d/%m/%Y"),
                        "Nome": nome,
                        "Senha do dia": senha
                    }
                ]
            )
            df_final = pd.concat([df, atleta_data], ignore_index=True)
            conn.update(worksheet="Página1", data=df_final)
            st.success("Sua presença foi registrada!")

st.markdown('#')
st.markdown('#')
st.text('Criado por:\nCarol Yumi e Gui Messias')
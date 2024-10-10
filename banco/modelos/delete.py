import streamlit as st
from datetime import datetime

def Create(cursor, conexao):
    st.write("Cadastro de um novo aluno")
    
    nome = st.text_input('Informe o nome do aluno:')
    profissao = st.text_input('Insira a profissão do aluno: ')
    nascimento = st.date_input(
        'Insira a Data de Nascimento: ',
        value=datetime(2000, 1, 1),
        min_value=datetime(1900, 1, 1),
        max_value=datetime.now()
        )
    sexo = st.text_input('Sexo(M, F):').upper
    peso = st.number_input('Peso: ',  min_value=0.0, step=0.01, format="%.2f")
    altura = st.number_input('Altura: ',  min_value=0.0, step=0.01, format="%.2f")
    nacionalidade = st.text_input('Nacionalidade: ')
    curso_preferido = st.number_input('Id do curso preferido:', min_value=1)
    
    
    if st.button('Cadastrar Aluno'):
        if nome != '':
            comando = f"INSERT INTO alunos (id, nome, profissao, nascimento, sexo, peso, altura, nacionalidade, curso_preferido) VALUES (default,'{nome}','{profissao}', '{nascimento}', '{sexo}','{peso}', '{altura}', '{nacionalidade}','{curso_preferido}');"
            cursor.execute(comando)
            conexao.commit()
            st.success('Aluno cadastrado com sucesso.')
        else:
            st.error("Por favor, insira um nome no formato caractere!")

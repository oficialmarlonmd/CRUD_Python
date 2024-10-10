import streamlit as st

def Update(cursor, conexao):
    st.write("Atualizar o Cruso Preferio:")
    
    nome = st.text_input('Digite o nome do aluno:')
    
    curso_preferido = st.number_input('Informe o novo curso preferido:', min_value=1)
    
    if st.button('Atualizar'):
        if nome != '':
            comando = f'UPDATE alunos SET curso_preferido = {curso_preferido} WHERE nome = "{nome}"'
            cursor.execute(comando)
            conexao.commit()
            st.success(f'O curso preferido do aluno {nome} foi atualizado para {curso_preferido}.')
        else:
            st.error("Por favor, insira um nome de um aluno que está na lista.")

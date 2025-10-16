# import streamlit as st
# st.header("Minha dashboard")
# st.sidebar.header("menu")
# st.button("test")

# meu_site.py
import streamlit as st
import pandas as pd
import numpy as np

# 1. Título e cabeçalho
st.title("Meu Primeiro Site com Streamlit! 🚀")

# 2. Texto simples
st.write("Esta é uma demonstração simples de como o Streamlit funciona.")

# 3. Exemplo de componente interativo (Slider)
idade = st.slider("Selecione sua idade:", 0, 100, 25) # (label, min, max, valor inicial)
st.write(f"Você tem {idade} anos.")

# 4. Exemplo de visualização de dados (DataFrame e Gráfico)
st.header("Visualização de Dados")

# Cria um DataFrame de exemplo
data = {
    'coluna A': np.random.randn(20),
    'coluna B': np.random.randn(20),
    'coluna C': np.random.choice(['X', 'Y', 'Z'], 20)
}
df = pd.DataFrame(data)

# Exibe o DataFrame
st.dataframe(df.head(5))

# Exibe um gráfico de linha
st.line_chart(df[['coluna A', 'coluna B']])

# 5. Exemplo de botão
if st.button('Clique aqui!'):
    st.success('O botão foi clicado! 🎉')
else:
    st.info('Aguardando clique no botão...')

# 6. Barra Lateral (Sidebar)
st.sidebar.title("Opções da Barra Lateral")
nome = st.sidebar.text_input("Qual é o seu nome?")
if nome:
    st.sidebar.write(f"Olá, {nome}!")
"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st
import dados

st.set_page_config(layout="wide")
st.title("📚 Dashboard de Livros")
st.write("Se você está vendo esta página, o seu ambiente está pronto! 🎉")

col1, col2, col3 = st.columns(3)

livros = dados.ler_livros()

qtd_livros = len(livros)
col1.metric("Quantidade de livros", qtd_livros)

preco_medio = dados.calcular_preco_medio(livros)
col2.metric("Preço médio", f"£{round(preco_medio, 2)}")

qtd_cinco = dados.contar_cinco_estrelas(livros)
col3.metric("Livros com 5 estrelas", qtd_cinco)


st.dataframe(livros)
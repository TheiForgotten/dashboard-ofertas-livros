"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st

import dados



def montar_tabela(livros):
    livros = dados.carregar_livros()
    tabela = []
    for livro in livros:
        linha = {
            "Título": livro["titulo"],
            "Categoria": livro["categoria"],
            "Nota": "⭐" * livro["nota"],
            "Preço": f"£ {livro["preco"]: .2f}",
            "Faixa": dados.classificar_preco(livro["preco"])
        }
        tabela.append(linha)
    return tabela


def main():
    st.set_page_config(page_title="Dashboard de Livros", page_icon="📚", layout="wide")
    st.title("📚 Dashboard de Livros")

    livros = dados.ler_livros()

    col1, col2, col3, col4 = st.columns(4)
    qtd_livros = len(livros)
    col1.metric("Total de Livros", qtd_livros)

    preco_medio = dados.calcular_preco_medio(livros)
    col2.metric("Preço médio", f"£{preco_medio:.2f}")

    cinco_estrelas = dados.contar_cinco_estrelas(livros)
    col3.metric("Qtd. livros 5 Estrelas", cinco_estrelas)

    mais_caro = dados.encontrar_mais_caro(livros)
    col4.metric("Livro mais caro", mais_caro["preco"])
    col4.caption(mais_caro["titulo"])

    st.dataframe(montar_tabela(livros))


if __name__ == "__main__":
    main()

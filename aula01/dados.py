"""Leitura dos arquivos CSV do projeto.
"""

from pathlib import Path
import csv
# Pasta onde este arquivo .py está. Assim o programa encontra o CSV
# mesmo quando é executado a partir de outra pasta (como no Streamlit Cloud).
PASTA = Path(__file__).parent
CAMINHO_LIVROS = PASTA / "livros.csv"

def ler_livros():
    livros = []
    try:
        with open(CAMINHO_LIVROS, "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                livros.append(linha)
    except FileNotFoundError:
        print("o arquivo não foi encontrado") 
    except Exception as error:
        print("Ocorreu um erro na leitura do arquivo", error)

    return livros


def ler_livros_v2():
    try:
        with open("livros.csv", "r", encoding="utf-8") as arquivo:
            print(arquivo.readline())
    except FileNotFoundError:
        print("o arquivo não foi encontrado") 
    except Exception as error:
        print("Ocorreu um erro na leitura do arquivo", error)


def ler_livros_v1():
    arquivo = None
    try:
        arquivo = open("livros.csv", "r", encoding="utf-8")
        print(arquivo.readline())
    except FileNotFoundError:
        print("o arquivo não foi encontrado")
    except Exception as error:
        print("Ocorreu um erro na leitura do arquivo", error)
    finally:
        if arquivo is not None:
            arquivo.close()

def calcular_preco_medio(livros):
    soma: float = 0
    for livro in livros:
        preco_original: str = livro["preco"]
        preco_original_limpo: str = preco_original.replace("£", "")
        preco_num: float = float(preco_original_limpo)
        soma += preco_num

    preco_medio: float = soma / len(livros)
    return preco_medio


def contar_cinco_estrelas(livros):
    contador: int = 0
    for livro in livros:
        nota_limpa: str = livro["nota"].lower().strip()
        if nota_limpa == "five":
            contador += 1

    return contador

def achar_livro_mais_caro(livros):
    livro_mais_caro = ["", ""]
    max: float = 0
    for livro in livros:
        preco_original: str = livro["preco"]
        preco_original_limpo: str = preco_original.replace("£", "")
        preco_num: float = float(preco_original_limpo)
        if preco_num > max:
            max = preco_num
            livro_mais_caro[0] = livro["titulo"]
            livro_mais_caro[1] = livro["preco"]
    return livro_mais_caro



if __name__ == "__main__":
    livros = ler_livros()
    # print(f"a quantidade de livros da coleção é de {len(livros)} livros")
    
    # preco_medio: float = calcular_preco_medio(livros)
    # print(f"o preco medio dos livros é de {round(preco_medio, 2)}")

    # cinco_estrelas = contar_cinco_estrelas(livros)
    # print(f"existe {cinco_estrelas} livros com cinco estrelas")

    livro_mais_caro = achar_livro_mais_caro(livros)
    print(f"o livro mais caro é {livro_mais_caro[0]} com o preco de {livro_mais_caro[1]}")
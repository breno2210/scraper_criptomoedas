
import requests
import pandas as pd
from datetime import datetime

# Lista de criptos para buscar
criptos = ["bitcoin", "ethereum", "solana", "ripple", "cardano"]

# Função para buscar preços na CoinGecko
def buscar_precos(criptos):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ",".join(criptos),
        "vs_currencies": "brl"
    }

    resposta = requests.get(url, params=params)
    if resposta.status_code != 200:
        raise Exception("Erro ao consultar a API:", resposta.text)

    dados = resposta.json()
    lista_resultado = []

    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for cripto in criptos:
        preco = dados[cripto]["brl"]
        lista_resultado.append({
            "Criptomoeda": cripto.capitalize(),
            "Preço (BRL)": preco,
            "Data/Hora": agora
        })

    return pd.DataFrame(lista_resultado)

# Execução principal
if __name__ == "__main__":
    print(" Buscando preços das criptomoedas em tempo real...\n")
    df = buscar_precos(criptos)
    print(df)

    # Salvar no CSV
    nome_arquivo = f"precos_cripto_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    df.to_csv(nome_arquivo, index=False, encoding="utf-8-sig")
    print(f"\n Dados salvos em: {nome_arquivo}")

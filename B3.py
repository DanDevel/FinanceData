import pandas_datareader as pdr

def obter_dados_ativo_b3(ticker):
    # Use 'yahoo' como source para obter dados da B3
    dados = pdr.get_data_yahoo(f"{ticker}.SA")
    print('dados::::::: ')
    print(dados)
    return dados

if __name__ == "__main__":
    ticker = "PEJA11"
    
    try:
        dados_peja11 = obter_dados_ativo_b3(ticker)
        print(f"Informações sobre o ativo {ticker}:\n")
        
        # Imprime informações sobre os últimos dias
        print(dados_peja11.tail())
    except Exception as e:
        print(f"Erro ao obter dados do ativo {ticker} da B3: {e}")

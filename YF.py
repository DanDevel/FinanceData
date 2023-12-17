import yfinance as yf

def obter_dados_ativo(ticker):
    ativo = yf.Ticker(ticker)
    dados = ativo.info
    return dados

if __name__ == "__main__":
    ticker = "PEJA11"
    
    try:
        dados_peja11 = obter_dados_ativo(ticker)
        print(f"Informações sobre o ativo {ticker}:\n")
        
        # Verifica se a chave 'taxa_anbima' existe nos dados
        if 'taxa_anbima' in dados_peja11:
            print(f"Taxa Anbima: {dados_peja11['taxa_anbima']}")
        else:
            print("Taxa Anbima não disponível para este ativo.")
        
        # Imprime outras informações disponíveis
        for chave, valor in dados_peja11.items():
            if chave != 'taxa_anbima':
                print(f"{chave}: {valor}")
    except Exception as e:
        print(f"Erro ao obter dados do ativo {ticker}: {e}")

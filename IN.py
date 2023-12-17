import investpy

def obter_dados_ativo_investpy(ticker, from_date, to_date):
    pesquisa_resultados = investpy.search(text=ticker, products=['stocks'], countries=['brazil'], n_results=1)
    
    if not pesquisa_resultados:
        raise ValueError(f"Ativo {ticker} não encontrado.")
    
    ativo_info = pesquisa_resultados[0]
    
    ativo_historico = investpy.get_stock_historical_data(
        stock=ativo_info.symbol,
        country=ativo_info.country,
        from_date=from_date,
        to_date=to_date
    )
    
    return ativo_historico

if __name__ == "__main__":
    ticker = "PEJA11"
    from_date = "01/01/2022"  # Substitua pela data desejada
    to_date = "31/12/2022"    # Substitua pela data desejada
    
    try:
        dados_peja11 = obter_dados_ativo_investpy(ticker, from_date, to_date)
        print(f"Informações sobre o ativo {ticker}:\n")
        
        # Imprime informações sobre os últimos dias
        print(dados_peja11.tail())
    except Exception as e:
        print(f"Erro ao obter dados do ativo {ticker} do Investpy: {e}")

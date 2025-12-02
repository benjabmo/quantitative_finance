import pandas as pd
import numpy as np
from modules.financials_functions import portfolio_volatility, portfolio_returns, VaR
from modules.backend import tickers_by_issuer

if __name__ == '__main__': 
    
    # Obtener tickers de ishares
    tickers = tickers_by_issuer(issuer='iShares')

    # Portafolio de Renta Fija
    tickers_rf = tickers[tickers['CATEGORIA']== 'ETF RF']
    list_tickers_rf = list(tickers_rf['TICKER'])

    # Portafolio de Renta Variable
    tickers_rv = tickers[tickers['CATEGORIA']== 'ETF RV']
    list_tickers_rv = list(tickers_rv['TICKER'])

    # Rango de Fechas
    start = '2024-01-01'
    end = '2024-12-31'

    # Nivel de Confianza
    confidence = 0.05
    lst = []
    for portafolio in [list_tickers_rf, list_tickers_rv]:
        
        
        # Obtener retornos
        df = portfolio_returns(tickers=portafolio, start=start, end=end)
        

        vector_w = np.array([1/len(portafolio)]* len(portafolio))
        

        # Calculo Volatilidad
        sigma = portfolio_volatility(df=df, vector_w=vector_w)
        

        # Value at Risk
        var = VaR(sigma=sigma, confidence=confidence)
        var = np.abs(var)
        var_mensual = var * np.sqrt(20)
        lst.append(var_mensual)
    
    df_final = pd.DataFrame(
        {
            'PORTAFOLIO': ['iShares Renta Fija', 'iShares Renta Variable'], 
            f'Value at Risk: {1-confidence}%': lst

        }
    )
    df_final = df_final.sort_values(
        by=f'Value at Risk: {1-confidence}%', 
        ascending=False)
    print(df_final)
        


    
        



    
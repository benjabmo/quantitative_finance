import numpy as np
from modules.financials_functions import portfolio_volatility, portfolio_returns, VaR


if __name__ == '__main__':
    # Datos del portafolio
    tickers = ['IEF', 'SPTL', 'TLT', 'VGLT']
    start = '2023-01-01'
    end = '2024-12-31'

    # Descargar retornos del portafolio
    df = portfolio_returns(tickers=tickers, start=start, end=end)
    print(df.head(10))
in
    # Calculo Volatilidad
    vector_w = np.array([1/len(tickers)] * len(tickers))
    sigma = portfolio_volatility(df=df,vector_w=vector_w)
    print(sigma)
    print('='*100)

    # Value at Risk (VaR)
    confidence = 0.05
    var = VaR(sigma=sigma, confidence=confidence)
    print(var)
    
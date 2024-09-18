import requests
import streamlit as st
import pandas as pd

@st.cache_data
def get_prices():
    """
    Gets the current prices of all symbols from Binance.

    Returns
    -------
    df : pd.DataFrame
        A DataFrame with a single row for each symbol. The columns are:
            - symbol : str
                The symbol of the crypto currency.
            - priceChange : float
                24 hour price change.
            - priceChangePercent : float
                24 hour price change percentage.
            - weightedAvgPrice : float
                Weighted average price of the last 24 hours.
            - prevClosePrice : float
                Previous day's closing price.
            - lastPrice : float
                Last price.
            - lastQty : float
                Last quantity.
            - bidPrice : float
                Present bid price.
            - bidQty : float
                Present bid quantity.
            - askPrice : float
                Present ask price.
            - askQty : float
                Present ask quantity.
            - openPrice : float
                Opening price of the 24 hour period.
            - highPrice : float
                Highest price of the 24 hour period.
            - lowPrice : float
                Lowest price of the 24 hour period.
            - volume : float
                Total traded volume in the 24 hour period.
            - quoteVolume : float
                Total traded quote volume in the 24 hour period.
            - openTime : int
                Timestamp of the opening time of the 24 hour period.
            - closeTime : int
                Timestamp of the closing time of the 24 hour period.
            - firstId : int
                ID of the first trade in the 24 hour period.
            - lastId : int
                ID of the last trade in the 24 hour period.
            - count : int
                Number of trades in the 24 hour period.
    """

    df = pd.read_json("https://api.binance.com/api/v3/ticker/24hr")
    return df

@st.cache_data
def get_candles(symbol):
    """
    Gets the 1h candlesticks for a given symbol.

    Parameters
    ----------
    symbol : str
        The symbol to get the candlesticks for.

    Returns
    -------
    df : pd.DataFrame
        A DataFrame with the following columns:
            - Date : datetime
                The date of the candle.
            - Open : float
                The opening price of the candle.
            - High : float
                The highest price of the candle.
            - Low : float
                The lowest price of the candle.
            - Close : float
                The closing price of the candle.
            - Volume : float
                The volume of the candle.
    """

    url = "https://api.binance.com/api/v3/klines"
    params = {"symbol": symbol, "interval": "1h"}
    response = requests.get(url, params=params)
    data = response.json()
    df = pd.DataFrame(data)
    df = df.iloc[:, :6]
    df.columns = ["Date", "Open", "High", "Low", "Close", "Volume"]
    df["Date"] = pd.to_datetime(df["Date"], unit="ms")
    df = df.set_index("Date")
    return df


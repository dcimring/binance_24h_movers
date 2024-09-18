import streamlit as st
from libs.charts import plot_candles
from libs.data import get_prices, get_candles

# use wide layout
st.set_page_config(layout="wide")

st.header("Binance largest 24h price changes")

# add css for headers
st.markdown('''
            <style>
                h1, h2 {
                    color: #7eefa1;
                }
            </style>''',
            unsafe_allow_html=True)

# get price changes last 24 hours and sort
prices = get_prices()
prices.sort_values(by="priceChange", ascending=False, inplace=True)
prices = prices.iloc[:20]
symbols = prices['symbol'].tolist()

prices_summary = prices[['symbol', 'priceChangePercent']]

with st.sidebar:
    symbol = st.selectbox("Select symbol", symbols, key="symbol")
    st.slider("Weeks for chart", 1, 10, 2, key="count")
    st.dataframe(prices_summary, hide_index=True)

# show price chart, updates when symbol changes
candles = get_candles(symbol)
fig = plot_candles(candles)
st.plotly_chart(fig, use_container_width=True)

# show dataframe with all data
st.header("All data")
st.dataframe(prices, hide_index=True, use_container_width=True)





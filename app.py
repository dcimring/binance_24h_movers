import streamlit as st
from libs.charts import plot_candles
from libs.data import get_prices, get_candles

# use wide layout
st.set_page_config(layout="wide")

# get price changes last 24 hours and sort
prices = get_prices()
prices.sort_values(by="priceChange", ascending=False, inplace=True)
symbols = prices['symbol'].tolist()

# show dataframe of price changes with symbol selection box
st.markdown("## :green[Binance largest 24h price changes]")
symbol = st.selectbox("Select symbol", symbols, key="symbol")
st.dataframe(prices, hide_index=True, use_container_width=True)

# show price chart, updates when symbol changes
st.markdown(f"#### :green[{symbol} price chart]")
candles = get_candles(symbol)
fig = plot_candles(candles)
st.plotly_chart(fig, use_container_width=True)

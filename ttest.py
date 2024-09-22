import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

st.title("Stock Portfolio Analysis")

ticker = st.text_input("Enter Stock Ticker (e.g. AAPL):")
if ticker:
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1y")
    
    st.line_chart(hist['Close'])
    
    st.write("Last 5 days data:")
    st.dataframe(hist.tail())
    
    st.write("Summary:")
    st.write(stock.info)

import streamlit as st
from datetime import date
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
import pandas as pd
from alpha_vantage.timeseries import TimeSeries

# 🔐 Insert your Alpha Vantage API Key here
API_KEY = '26TD6UB6I18UVGXK'  # Replace with your real key

st.set_page_config(page_title="Stock Forecast App")
st.title("📈 Stock Forecast App (Alpha Vantage)")

selected_stock = st.text_input("Enter stock ticker (e.g., AAPL, MSFT, TSLA):", value="AAPL").upper()

if not selected_stock:
    st.warning("Please enter a stock ticker to proceed.")
    st.stop()

n_years = st.slider("Years of prediction:", 1, 4)
period = n_years * 365

# 🧠 Load data from Alpha Vantage
@st.cache_data
def load_data(ticker):
    try:
        ts = TimeSeries(key=API_KEY, output_format='pandas')
        data, _ = ts.get_daily(symbol=ticker, outputsize='full')
        data = data.rename(columns={
            '1. open': 'Open',
            '2. high': 'High',
            '3. low': 'Low',
            '4. close': 'Close',
            '5. volume': 'Volume'
        })
        data.reset_index(inplace=True)
        data = data.sort_values('date')
        data = data.rename(columns={'date': 'Date'})
        return data
    except Exception as e:
        st.error(f"⚠️ Failed to fetch data for {ticker}. Error: {e}")
        return pd.DataFrame()

# 📥 Load and validate data
data_load_state = st.text("Loading data...")
data = load_data(selected_stock)
data_load_state.text("Loading data... done!")

if data.empty or not {'Date', 'Open', 'Close'}.issubset(data.columns):
    st.error("❌ Could not fetch valid stock data. Try again later or check your API key.")
    st.stop()

# 📄 Show raw data
st.subheader("Raw Data (tail)")
st.write(data.tail())

# 📊 Plot data
def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data["Date"], y=data["Open"], name="Open"))
    fig.add_trace(go.Scatter(x=data["Date"], y=data["Close"], name="Close"))
    fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data()

# 🔮 Forecasting
df_train = data[["Date", "Close"]].rename(columns={"Date": "ds", "Close": "y"})

if df_train.shape[0] < 2 or df_train["y"].isnull().all():
    st.error("⚠️ Not enough data to train the forecast model.")
    st.stop()

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# 📈 Show forecast
st.subheader("Forecast Data")
st.write(forecast.tail())

st.write(f"📉 Forecast plot for {n_years} year(s)")
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("🧩 Forecast Components")
fig2 = m.plot_components(forecast)
st.write(fig2)

# ✅ Compare predicted vs actual
st.subheader("📊 Actual vs Predicted Closing Prices")

# Merge forecast with original close prices
merged_df = pd.merge(
    df_train,                      # actual prices
    forecast[["ds", "yhat"]],      # predicted prices
    on="ds",
    how="inner"
)

# Plot actual vs predicted
fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=merged_df["ds"], y=merged_df["y"], name="Actual Close"))
fig3.add_trace(go.Scatter(x=merged_df["ds"], y=merged_df["yhat"], name="Predicted Close"))
fig3.update_layout(title="Actual vs Predicted Close Price", xaxis_title="Date", yaxis_title="Price")
st.plotly_chart(fig3)

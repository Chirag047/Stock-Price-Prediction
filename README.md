
# 📈 Stock Forecast App

A sleek, interactive **Streamlit-based web application** that enables users to **forecast stock prices** using **Meta’s Prophet** and data from **Alpha Vantage**. The app visualizes historical data, generates future forecasts, and compares predicted vs actual closing prices — all in one dashboard.

---

### 🚀 Features

- 🔍 **Select popular stocks** like AAPL, MSFT, TSLA, AMZN, and GOOGL
- 📊 Visualize historical **Open** and **Close** prices
- 🔮 **Forecast future stock prices** up to 4 years using [Prophet](https://facebook.github.io/prophet/)
- 📉 Compare **actual vs predicted closing prices**
- 🧠 Powered by **Alpha Vantage API** for real-time stock data

---

### 📷 App Preview

<img width="1215" height="758" alt="Image" src="https://github.com/user-attachments/assets/53cd3723-c69f-4bf1-ae8d-38a643dcc11d" />
<img width="1105" height="628" alt="Image" src="https://github.com/user-attachments/assets/0cca3671-3fb8-402c-9207-196da08286c1" />
<img width="746" height="298" alt="Image" src="https://github.com/user-attachments/assets/caee0784-5b7a-4dc0-a5c4-766a2e5df4c1" />
*Replace with actual screenshot of your app UI*

---

### 📦 Dependencies

Install all required packages using:

```bash
pip install streamlit prophet alpha_vantage plotly pandas
```

---

###  Get Your Alpha Vantage API Key to use the dataset

1. Visit [Alpha Vantage](https://www.alphavantage.co/support/#api-key)
3. You'll receive an API key immediately on screen and by email
4. Copy the API key and use 

Then, in the Python file (`stock predictior.py`), replace this line:

```python
API_KEY = 'YOUR_API_KEY_HERE'
```

with your actual API key:

```python
API_KEY = 'your_real_key_here'
```

---

### 💻 How to Run the App

1. Make sure your terminal is in the directory containing `stock predictior.py`
2. Run the Streamlit app with:

```bash
streamlit run "stock predictior.py"
```

3. The app will open automatically in your default web browser

---

### 📈 How It Works

- ⬇️ **Loads historical daily stock prices** from Alpha Vantage
- 📊 **Visualizes open/close price trends**
- 🤖 **Uses Prophet to forecast** future close prices
- 🔁 **Compares actual vs predicted** prices on the same graph

---


---


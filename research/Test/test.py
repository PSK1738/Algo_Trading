import yfinance as yf
import matplotlib.pyplot as plt

df = yf.download("QQQ", start="2015-01-01")
df["Close"].plot(title="QQQ Price")
plt.show()

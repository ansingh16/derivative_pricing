import numpy as np
import matplotlib.pyplot as plt
from Code.MonteCarlo import StockMovement
from Option_pricing import Pricing_Models


duration = 2 # years
dt = 1/252 # years
volatility = 0.5
mean_return = 0.1
stock = StockMovement(100, duration, dt, volatility, mean_return)

stock.get_prices()

# Plot the simulated stock price
plt.figure(figsize=(10, 6))
plt.plot(stock.time, stock.prices)
plt.xlabel('Time (years)')
plt.ylabel('Stock Price')
plt.title('Simulated Stock Price Using Brownian Motion')
plt.grid(True)
plt.show()

# options
strike_price = 105
risk_free_rate = 0.05
Expiry = 0.2
t=0.15
models = Pricing_Models(strike_price, risk_free_rate, Expiry, volatility,dt)
option_price = models.binomial_pricing(stock.prices[0],t)

print("Option price:", option_price)


from Stock_movement import StockMovement
from Binomial_pricing import Pricing_Models

duration = 2 # years
dt = 1/252 # years
volatility = 1
mean_return = 0.1
stock = StockMovement(100, duration, dt, volatility, mean_return)
stock.get_prices()


# options
strike_price = 105
risk_free_rate = 0.05
time2expire = 0.015
models = Pricing_Models(strike_price, risk_free_rate, time2expire, volatility,dt)
option_price = models.binomial_pricing(stock.prices[0])

print("Option price:", option_price)
# print(stock.prices)
# # Example usage:
# T = 1.0          # Total time (in years)
# mu = 0.1         # Drift (average return)
# sigma = 0.2      # Volatility (standard deviation of return)
# S0 = 100.0       # Initial stock price
# dt = 1/252.0     # Time step (trading days per year)

# t, S = brownian_motion(T, mu, sigma, S0, dt)

# # Example usage:
# S0 = 100  # Initial stock price
# K = 105   # Strike price
# T = 1     # Time to expiration (in years)
# r = 0.05  # Risk-free interest rate
# sigma = 0.2  # Volatility
# n = 100   # Number of time steps

# option_price = binomial_pricing(S0, K, T, r, sigma, n)
# print("Option price:", option_price)

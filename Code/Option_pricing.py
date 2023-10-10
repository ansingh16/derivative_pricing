from Stock_movement import StockMovement
from Binomial_pricing import binomial_pricing

duration = 2 # years
dt = 1/252 # years
volatility = 1
mean_return = 0.1
stock = StockMovement(100, duration, dt, volatility, mean_return)
stock.get_prices()

print(stock.prices)
# # Example usage:
# T = 1.0          # Total time (in years)
# mu = 0.1         # Drift (average return)
# sigma = 0.2      # Volatility (standard deviation of return)
# S0 = 100.0       # Initial stock price
# dt = 1/252.0     # Time step (trading days per year)

# t, S = brownian_motion(T, mu, sigma, S0, dt)
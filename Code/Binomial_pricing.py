import numpy as np

def binomial_pricing(S, K, T, r, sigma, n):
    dt = T / n
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)
    
    # Initialize stock price tree
    stock_tree = np.zeros((n+1, n+1))
    stock_tree[0, 0] = S
    
    # Calculate stock prices at each node
    for i in range(1, n+1):
        for j in range(i+1):
            stock_tree[i, j] = stock_tree[i-1, j] * u
            if j > 0:
                stock_tree[i, j] *= d
                
    # Calculate option prices at the final time step
    option_tree = np.maximum(0, stock_tree - K)
    
    # Backward induction to calculate option prices at earlier time steps
    for i in range(n-1, -1, -1):
        for j in range(i+1):
            option_tree[i, j] = np.exp(-r * dt) * (p * option_tree[i+1, j] + (1 - p) * option_tree[i+1, j+1])
    
    return option_tree[0, 0]

# Example usage:
S0 = 100  # Initial stock price
K = 105   # Strike price
T = 1     # Time to expiration (in years)
r = 0.05  # Risk-free interest rate
sigma = 0.2  # Volatility
n = 100   # Number of time steps

option_price = binomial_pricing(S0, K, T, r, sigma, n)
print("Option price:", option_price)

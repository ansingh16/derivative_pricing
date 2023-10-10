import pandas as pd 
import numpy as np
import datetime

class StockMovement:
    def __init__(self, price, duration,dt,volatility,mean_return=0.1):
        self.initial_price = price
        self.duration = duration
        self.dt = dt
        self.sigma = volatility
        self.mean_return = mean_return
        self.time = []
        self.prices = []
        self.time.append(0)
        self.prices.append(price)
    def get_prices(self):
        """
        Calculates the new price based on the current price, drift rate, and volatility.
        
        Returns:
            float: The updated current price.
        """
    
        n = int(self.duration/ self.dt)
        self.time = np.linspace(0.0,self.duration, n+1)
        W = np.random.standard_normal(size=n+1)
        W = np.cumsum(W) * np.sqrt(self.dt)
        self.returns = (self.mean_return - 0.5 * self.sigma**2) * self.time + self.sigma * W
        self.prices = self.initial_price * np.exp(self.returns)
        




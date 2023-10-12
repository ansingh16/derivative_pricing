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
        #self.time.append(0)
        #self.prices.append(np.array([price]))
    def get_prices(self):
        """
        Calculates the new price based on the current price, drift rate, and volatility.
        
        Returns:
            float: The updated current price.
        """
        price = self.initial_price
        for t in np.linspace(0.0,self.duration, int(self.duration/self.dt)):
            self.time.append(t)
            self.prices.append(price)
            price = (price * np.exp((self.mean_return - 0.5 * self.sigma**2) * self.dt + self.sigma * np.sqrt(self.dt) * np.random.standard_normal()))

        # n = int(self.duration/ self.dt)
        # self.time = np.linspace(0.0,self.duration, n+1)
        # W = np.zeros(n+1)  # Initialize W with zeros
        # W[1:] = np.random.standard_normal(size=n) * np.sqrt(self.dt)  # Exclude the first element
        # W = np.cumsum(W) * np.sqrt(self.dt)
        # self.returns = (self.mean_return - 0.5 * self.sigma**2) * self.time + self.sigma * W

        # self.prices.append(self.initial_price * np.exp(self.returns))

        # self.prices = np.concatenate(self.prices)

        




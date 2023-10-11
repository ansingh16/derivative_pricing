import numpy as np
from Stock_movement import StockMovement

class Pricing_Models:
    
    def __init__(self,strike_price,risk_free_rate,time2expire,volatility,deltat):
        self.strike_price = strike_price
        self.risk_free_rate = risk_free_rate
        self.time2expire = time2expire
        self.sigma = volatility
        self.dt = deltat

    #def get_node_prices(self, i, u, v, p):
        # return np.exp(-self.risk_free_rate * self.dt*i) * (p * self.
    def binomial_pricing(self,S):
        n = int(self.time2expire/self.dt)
        u = np.exp(self.sigma * np.sqrt(self.dt))
        
        p0 = (u - np.exp(-self.risk_free_rate * self.dt)) / (u**2 - 1)
        p1 = np.exp(-self.risk_free_rate * self.dt) - p0
        p = np.zeros(n+1)
        # initial values at time T
        for i in range(n+1):
            p[i] = self.strike_price - S * u**(2*i - n)
            if p[i] < 0:
                p[i] = 0
        
        # move to earlier times
        for j in range(n-1):
            for i in range(j):
                # binomial value
                p[i] = p0 * p[i+1] + p1 * p[i];   
                # exercise value
                exercise = self.strike_price - S * u**(2*i - j)  
                if p[i] < exercise:
                    p[i] = exercise
            
        
        return p[0]



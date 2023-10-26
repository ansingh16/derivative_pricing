import numpy as np
# from Code.MonteCarlo import StockMovement
import scipy.stats as stats

class Pricing_Models:
    
    def __init__(self,strike_price,risk_free_rate,expiry,volatility,deltat):
        self.strike_price = strike_price
        self.risk_free_rate = risk_free_rate
        self.expiry = expiry
        self.sigma = volatility
        self.dt = deltat

    
    def binomial_pricing(self,S,t):
        self.time2expire = self.expiry - t
        # number of time steps
        n = int(self.time2expire/self.dt)

        # fraction of moving upwards
        u = np.exp(self.sigma * np.sqrt(self.dt))
        
        # probability of upwards movement
        p0 = (u - np.exp(-self.risk_free_rate * self.dt)) / (u**2 - 1)
        # prob of downward movement
        p1 = np.exp(-self.risk_free_rate * self.dt) - p0

        # container for prices
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
                # exercise = self.strike_price - S * u**(2*i - j)  
                # if p[i] < exercise:
                #     p[i] = exercise
            
        # return current option price
        return p[0]
    
    def Black_Scholes(self,S,t,type):
        self.time2expire = self.expiry - t
        # calculate d1 and d2
        d1 = (np.log(S / self.strike_price) + (self.risk_free_rate + 0.5 * self.sigma**2) * self.time2expire) / (self.sigma * np.sqrt(self.time2expire))
        d2 = d1 - self.sigma * np.sqrt(self.time2expire)
        if type=="call":
            return S* stats.norm.cdf(d1) - self.strike_price * np.exp(-self.risk_free_rate * self.time2expire) * stats.norm.cdf(d2)
        else:
            return self.strike_price * np.exp(-self.risk_free_rate * self.time2expire) * stats.norm.cdf(-d2) - S *stats.norm.cdf(-d1) 

    def MonteCarlo(self,S,t,N):
        self.time2expire = self.expiry - t
        # number of time steps
        n = int(self.time2expire/self.dt)

        ST = np.log(S) +  np.cumsum(((r - self.sigma**2/2)*self.dt +\
                            self.sigma*np.sqrt(self.dt) * \
                            np.random.normal(size=(n,N))),axis=0)

        return np.exp(ST)


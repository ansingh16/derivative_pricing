import numpy as np
# from Code.MonteCarlo import StockMovement
import scipy.stats as stats
import numpy.random as npr
from scipy.stats import norm

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
    
    def Black_Scholes(self,S,type):
        self.time2expire = self.expiry
        # calculate d1 and d2
        d1 = (np.log(S / self.strike_price) + (self.risk_free_rate + 0.5 * self.sigma**2) * self.time2expire) / (self.sigma * np.sqrt(self.time2expire))
        d2 = d1 - self.sigma * np.sqrt(self.time2expire)
        if type=="call":
            call_price = S* stats.norm.cdf(d1) - self.strike_price * np.exp(-self.risk_free_rate * self.time2expire) * stats.norm.cdf(d2)
            return call_price
        else:
            put_price = self.strike_price * np.exp(-self.risk_free_rate * self.time2expire) * stats.norm.cdf(-d2) - S *stats.norm.cdf(-d1) 
            return put_price
    
    def vega(self,S):
        '''Parameters:
            S: Asset price
        returns: partial derivative w.r.t volatility
        '''
        self.time2expire = self.expiry
        ### calculating d1 from black scholes
        d1 = (np.log(S / self.strike_price) + (self.risk_free_rate + 0.5 * self.sigma**2) * self.time2expire) / (self.sigma * np.sqrt(self.time2expire))

        #print(f"sigma in vega: {self.sigma}")
        #see hull derivatives chapter on greeks for reference
        vega = S * norm.pdf(d1) * np.sqrt(self.expiry)

        if vega==0:
            print(f"S: {S}, strike: {self.strike_price}, d1: {d1}, expiry: {self.expiry}, sigma: {self.sigma}")
        return vega


    def MonteCarlo(self,S,N,type):

        # N is the number of trials

        steps = int(self.expiry/self.dt)
        
        # Generate random stock price paths
        np.random.seed(0)
        z = np.random.standard_normal((N, 1))
        ST = S * np.exp((self.risk_free_rate - 0.5 * self.sigma ** 2) * self.expiry + self.sigma* np.sqrt(self.expiry) * z)

        # Calculate option payoffs
        if type=="call":
            payoff = np.maximum(ST-self.strike_price, 0)
        else:
            # it's put option
            payoff = np.maximum(self.strike_price -ST, 0)

        # Calculate option price
        option_price = np.exp(-self.risk_free_rate * self.expiry) * np.mean(payoff)

  
        return option_price
    
    def mc_call_price(self,asset_price,i):
        return np.exp(-self.risk_free_rate*self.expiry)*max(asset_price - self.strike_price,0)


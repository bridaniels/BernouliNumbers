# Bernouli Numbers 

# Import Libraries 
import numpy as np 



class Bernoulli(): 

    # Bernoulli Probability Mass Function 
    def pmf(x,p): 
        f = p**x * (1-p)**(1-x)
        return f 

    # Mean/Expected Value E(x) of Random Variable: 
    def mean(p):
        return p 

    # Variance and Standard Deviation 
    def var(p): 
        return p*(1-p)
    def std(p): 
        return Bernoulli.var(p)**(1/2)

    # Generate Random Variates 
    # Size = Parameter 
    def rvs(p, size=1): 
        rvs = np.array([])
        for i in range(0,size): 
            if np.random.rand() <= p: 
                a = 1 
                rvs = np.append(rvs,a)
            else: 
                a = 0 
                rvs = np.append(rvs,a)
        return rvs 


p = 0.2 # Probability of Accident 

print("Probability of an Accident: {} \nMean: {} \nVariance: {} \nStandard Deviation: {} \nRandom Generated Number Array: {}".format(p, Bernoulli.mean(p), Bernoulli.var(p), Bernoulli.std(p), Bernoulli.rvs(p,size=10)))
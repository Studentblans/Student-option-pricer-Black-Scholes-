# Explanation of the code and the mathematic model behind it :

So, I learn a few weeks ago what is an "option", I never heard of it in my classes at the university and I found the concept really interesting, especially the mathematic approach to analyse an option, that's what leads me to develop this option pricer (and to test my knowledge on the subject).

# Option in finance : definition

If you're not familiar with the concept of option, here is a quick overview of it :

An option is a contract between a buyer and a seller, either a call or a put, a call is a contract that gives the right (and not the obligation) for the buyer to acquire a share with an agreed price (named "striike") until a certain time noted T (also called "maturity") and a put is a contract that allows the buyer to sell a share at a certain price.
To use his right, the buyer has to purchase the option, and its amount is called the "prime", the Black-Scholes formula is the mathematical approach to determine this prime.

# Black-Scholes Model

The assumptions of the model :

The price of the underlying asset St follows a geometric Brownian motion with constant volatility σ and constant drift μ:

<img width="140" height="25" alt="image" src="https://github.com/user-attachments/assets/cb067c33-c8f7-4795-b5b8-6e3357943de4" />

there are no arbitrage opportunities;
time is a continuous variable;
short selling is possible;
there are no transaction costs;
there is a risk-free interest rate that is constant and known in advance;
all underlying assets are perfectly divisible (for example, one can buy one-hundredth of a share);
in the case of a stock, it pays no dividends between the time of the option's valuation and its expiration.

This model does not represent the reality of the stock market, however, the widespread adoption of this model points to the concept of "rational mimicry" (or, in this specific case, "irrational") mimicry, which gives rise to the phenomenon of "self-fulfilling" decision-making.

Black-Scholes Formula

As previously stated, the Black-Scholes formula is the mathematical approach to determine the prime of an option (its theoretical value) :

To do so, the formula needs five data points : 
S₀ the current value of the underlying stock,
T the time remaining until the option's expiration (expressed in years), (also known as its tenor),
K the strike price set by the option,
r the risk-free interest rate,
σ the volatility of the stock price.

The theoretical price of a call option—which grants the right, but not the obligation, to purchase asset S at value K on date T—is characterized by its payoff: <img width="130" height="24" alt="image" src="https://github.com/user-attachments/assets/bedb5c78-33a3-48fe-ab8a-e78adc2785d3" />



It is given by the risk-neutral expectation of the discounted terminal payoff : <img width="103" height="20" alt="image" src="https://github.com/user-attachments/assets/b4ad8e61-9363-4dc3-aa85-1d6cbda09b95" />


Consider the Black-Scholes formula:
<img width="186" height="25" alt="image" src="https://github.com/user-attachments/assets/3162da27-cb91-43f9-b501-6bbb69e40054" />

Similarly, the theoretical price of a put option with a payoff : <img width="127" height="23" alt="image" src="https://github.com/user-attachments/assets/8f2bd83d-121c-4610-b2dc-633a1dbf7410" /> is given by: 
<img width="218" height="23" alt="image" src="https://github.com/user-attachments/assets/c5700a29-28c5-4936-a207-8b57110c0920" />

with :
N the cumulative distribution function of the standard normal distribution N(0,1) :

<img width="149" height="78" alt="image" src="https://github.com/user-attachments/assets/89c0e191-d9d5-43b5-b2d8-af928c805e64" />


# Option Greeks

The "Greeks" measure an option's price sensitivity to each parameter of the Black-Scholes model. It's 5 indicators : delta, gamma, theta, vega and rho.

Delta :  first derivative of the option price with respect to the price of the underlying asset

<img width="163" height="46" alt="image" src="https://github.com/user-attachments/assets/538b9cbd-49f9-4257-8da5-c51f4fe63f3f" />

Gamma : represents the convexity or curvature of an option's price in relation to the price of the underlying asset. It indicates whether the option's price tends to move faster or slower than the price of the underlying asset.

<img width="125" height="32" alt="image" src="https://github.com/user-attachments/assets/81086489-a365-4997-8384-7a1d26dc179a" />

Theta : The cost (or gain) associated with the passage of time for an options portfolio. It measures how the passage of time affects the value of an option.

<img width="345" height="58" alt="image" src="https://github.com/user-attachments/assets/c5e9edc3-0a74-4a41-a329-966ed0dfdd4a" />

Vega : measurement of sensitivity to implied volatility

<img width="146" height="26" alt="image" src="https://github.com/user-attachments/assets/4c1960eb-6f3c-4066-96ed-cd345b348eb3" />

Rho : Rate of change of the premium value with respect to the risk-free rate.

<img width="260" height="47" alt="image" src="https://github.com/user-attachments/assets/0017cb14-a751-4786-97a1-2e33921eb784" />

# Code implementation :

To implement the Black Scholes formula in my code, I defined two functions, one for call and one for put :

def black_scholes_call():
    S0 = spot_price_choice.get()
    K = strike_price_choice.get()
    r = rate_choice.get()
    T = maturity_choice.get()
    sigma = volatility_choice.get()
    d1 = (math.log(S0/K)+((r+(1/2)*(sigma**2)))*T)/(sigma*math.sqrt(T))
    d2 = d1 - sigma*math.sqrt(T)
    C = S0*norm.cdf(d1) - K*(math.e**(-(r*T))*norm.cdf(d2))
    return C

def black_scholes_put():
    S0 = spot_price_choice.get()
    K = strike_price_choice.get()
    r = rate_choice.get()
    T = maturity_choice.get()
    sigma = volatility_choice.get()
    d1 = (math.log(S0/K)+((r+(1/2)*(sigma**2)))*T)/(sigma*math.sqrt(T))
    d2 = d1 - sigma*math.sqrt(T)
    P = K*math.e**(-(r*T))*norm.cdf(-d2)-S0*norm.cdf(-d1)
    return P

and the same for the greeks : 

def delta_call():
    S0 = spot_price_choice.get()
    K = strike_price_choice.get()
    r = rate_choice.get()
    T = maturity_choice.get()
    sigma = volatility_choice.get()
    d1 = (math.log(S0/K)+((r+(1/2)*(sigma**2)))*T)/(sigma*math.sqrt(T))
    return norm.cdf(d1)
def delta_put():
    S0 = spot_price_choice.get()
    K = strike_price_choice.get()
    r = rate_choice.get()
    T = maturity_choice.get()
    sigma = volatility_choice.get()
    d1 = (math.log(S0/K)+((r+(1/2)*(sigma**2)))*T)/(sigma*math.sqrt(T))
    return norm.cdf(d1)-1

def gamma_call_put():
    S0 = spot_price_choice.get()
    K = strike_price_choice.get()
    r = rate_choice.get()
    T = maturity_choice.get()
    sigma = volatility_choice.get()
    d1 = (math.log(S0/K)+((r+(1/2)*(sigma**2)))*T)/(sigma*math.sqrt(T))
    return ((1/(math.sqrt(2*math.pi))*math.exp(-(d1**2)/2)))/(S0*sigma*math.sqrt(T))

def vega_call_put():
    S0 = spot_price_choice.get()
    K = strike_price_choice.get()
    r = rate_choice.get()
    T = maturity_choice.get()
    sigma = volatility_choice.get()
    d1 = (math.log(S0/K)+((r+(1/2)*(sigma**2)))*T)/(sigma*math.sqrt(T))
    return S0*math.sqrt(T)*(1/(math.sqrt(2*math.pi))*math.exp(-(d1**2)/2))

def theta_call():
    S0 = spot_price_choice.get()
    K = strike_price_choice.get()
    r = rate_choice.get()
    T = maturity_choice.get()
    sigma = volatility_choice.get()
    d1 = (math.log(S0/K)+((r+(1/2)*(sigma**2)))*T)/(sigma*math.sqrt(T))
    d2 = d1 - sigma*math.sqrt(T)
    return -((S0*(1/(math.sqrt(2*math.pi))*math.exp(-(d1**2)/2))*sigma)/(2*math.sqrt(T)))-r*K*math.exp(-r*T)*norm.cdf(d2)
def theta_put():
    S0 = spot_price_choice.get()
    K = strike_price_choice.get()
    r = rate_choice.get()
    T = maturity_choice.get()
    sigma = volatility_choice.get()
    d1 = (math.log(S0/K)+((r+(1/2)*(sigma**2)))*T)/(sigma*math.sqrt(T))
    d2 = d1 - sigma*math.sqrt(T)
    return -((S0*(1/(math.sqrt(2*math.pi))*math.exp(-(d1**2)/2))*sigma)/(2*math.sqrt(T)))+r*K*math.exp(-r*T)*norm.cdf(-d2)

def rho_call():
    S0 = spot_price_choice.get()
    K = strike_price_choice.get()
    r = rate_choice.get()
    T = maturity_choice.get()
    sigma = volatility_choice.get()
    d1 = (math.log(S0/K)+((r+(1/2)*(sigma**2)))*T)/(sigma*math.sqrt(T))
    d2 = d1 - sigma*math.sqrt(T)
    return K*T*math.exp(-r*T)*norm.cdf(d2)
def rho_put():
    S0 = spot_price_choice.get()
    K = strike_price_choice.get()
    r = rate_choice.get()
    T = maturity_choice.get()
    sigma = volatility_choice.get()
    d1 = (math.log(S0/K)+((r+(1/2)*(sigma**2)))*T)/(sigma*math.sqrt(T))
    d2 = d1 - sigma*math.sqrt(T)
    return -K*T*math.exp(-r*T)*norm.cdf(-d2)

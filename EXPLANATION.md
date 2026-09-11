# Explanation of the code and the mathematic model behind it

So, I learn a few weeks ago what is an "option", I never heard of it in my classes at the university and I found the concept really interesting, especially the mathematic approach to analyse an option, that's what leads me to develop this option pricer (and to test my knowledge on the subject).

# Option in finance : definition

If you're not familiar with the concept of option, here is a quick overview of it :

An option is a contract between a buyer and a seller, either a call or a put, a call is a contract that gives the right (and not the obligation) for the buyer to acquire a share with an agreed price (named "strike") until a certain time noted T (also called "maturity") and a put is a contract that allows the buyer to sell a share at a certain price.
To use his right, the buyer has to purchase the option, and its amount is called the "prime", the Black-Scholes formula is the mathematical approach to determine this prime.

# Black-Scholes Model

## The assumptions of the model 

The price of the underlying asset St follows a geometric Brownian motion with constant volatility σ and constant drift μ:

<img width="140" height="25" alt="image" src="https://github.com/user-attachments/assets/cb067c33-c8f7-4795-b5b8-6e3357943de4" />

There are no arbitrage opportunities;
Time is a continuous variable;
Short selling is possible;
There are no transaction costs;
There is a risk-free interest rate that is constant and known in advance;
All underlying assets are perfectly divisible (for example, one can buy one-hundredth of a share);
In the case of a stock, it pays no dividends between the time of the option's valuation and its expiration.

This model does not represent the reality of the stock market. However, some researchers have suggested that its widespread adoption — a form of market-wide mimicry — has contributed to a 'self-fulfilling' effect, where the model's assumptions become more accurate simply because most market participants rely on it.

## Black-Scholes Formula

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

With :
N the cumulative distribution function of the standard normal distribution N(0,1) :

<img width="149" height="78" alt="image" src="https://github.com/user-attachments/assets/89c0e191-d9d5-43b5-b2d8-af928c805e64" />


## Option Greeks

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

## Code implementation

To implement the Black Scholes formula in my code, I defined two functions, one for call and one for put :

To retrieve the parameters, I use the tkinter .get() function; I will come back to this in the UI section.

```
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
```
```
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
```

Same for greeks : 
```
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
```
# Graph Simulation (GBM)
Using the same data employed in the Black-Scholes formula, it is possible to model a prediction of the underlying asset's price.

To simulate the price paths of an asset, we solve a stochastic differential equation (SDE). A common SDE for modeling asset prices is the geometric Brownian motion:

<img width="110" height="20" alt="image" src="https://github.com/user-attachments/assets/1c1c437d-2a8d-406f-b76b-dd3b9455a9d6" />

(You will notice that μ has been replaced by r to represent the risk-free interest rate (which replaces the constant drift).)

We therefore reuse:
S0 – the price of the underlying asset
r – the risk-neutral interest rate
σ – the volatility
dW – the Wiener process or Brownian motion

We transform S using the logarithm to simplify the equation:

<img width="152" height="25" alt="image" src="https://github.com/user-attachments/assets/1c357b34-d50b-4bb9-a767-6fd459ea9a55" />

and by integrating the equation, we obtain the exact solution:

<img width="158" height="23" alt="image" src="https://github.com/user-attachments/assets/5ca57e83-8913-4e48-8935-bb491daea2fe" />

Since geometric Brownian motion has a closed-form solution, we can simulate it exactly at each time step, with no discretization error.

<img width="175" height="24" alt="image" src="https://github.com/user-attachments/assets/3f3b75f7-3327-488a-aad9-9417feda5383" />

φ is a random variable drawn from a standard normal distribution.

## Implementation of the Geometric Brownian movement in python :

We have previously established the mathematical formula for geometric Brownian motion; it is now time to incorporate it into the pricer's code.

The line ```S[i+1] = S[i]*np.exp((r-(1/2)*sigma**2)*dt+sigma*np.sqrt(dt)*w)``` below is the direct Python translation of this formula, where w corresponds to φ.
```
def geometric_brownian_movement_simulate_path():
    try:
        seed = 2026
        rng = np.random.default_rng(seed)
        S0 = spot_price_choice.get()
        r = rate_choice.get()
        T = maturity_choice.get()
        sigma = volatility_choice.get()
        t = int(timestep.get())
        n = int(paths_number.get())
        dt = T/t
        #array to store simulated paths
        S = np.zeros((t,n))
        S[0] = S0
        for i in range(0,t-1):
            w = rng.standard_normal(n)
            S[i+1] = S[i]*np.exp((r-(1/2)*sigma**2)*dt+sigma*np.sqrt(dt)*w)

        df = pd.DataFrame(S)
        ax.clear()
        ax.plot(df.iloc[:,:100])
        ax.set_xlabel('Time steps')
        ax.set_ylabel('Stock price')
        ax.set_title('Simulated Paths')
        fig.tight_layout()
        canvas_graph.draw()
    except(ValueError, ZeroDivisionError):
        result_text_label.config(text="/!\\ t and n should be + (≥1)")
```
"Seed" is an arbitrary variable; I chose the year 2026 because that is when the code was created, but it could have been any number. This choice ensures the same results are obtained every time the code is run.

"t" represents the timestep, earlier in the code, the defaults value is 252, to represent the standard number of trading days

"n" is the number of paths, its default value is 1000.

# Example

Here is an example of how to use the pricer:

Consider an at-the-money call option, where S0 equals K (both equal to 100), volatility is 20%, maturity is one year, and the interest rate is zero.

<img width="397" height="257" alt="image" src="https://github.com/user-attachments/assets/287ea9ad-30b6-4f57-a87f-eee6ede4fa84" />

## Results 

<img width="396" height="256" alt="image" src="https://github.com/user-attachments/assets/ccba5c96-786f-4b2a-8ed9-006baa493375" />

The result for the Black-Scholes formula provided by the pricer is 7.97, which means the option is worth €7.97 for an underlying asset priced at €100.

Delta is equal to 0.54, which means that for every €1 change in the underlying asset, the call option will change by €0.54.

Gamma is equal to 0.02; since it indicates the rate at which Delta changes as the underlying asset moves, if the underlying asset increases by €1, Delta will increase by +(0.54 + 0.02), resulting in €0.56.

Theta is equal to -€3.97, so the option loses approximately €3.97 per year.

Rho is equal to 46.02, which means that if the rate were to rise from 0% to 1%, the option would gain approximately €0.46.

Vega is 39.70, which means that if volatility rises by 1 point, the option increases by approximately €0.40.

This analysis remains very simple.

# UI (tkinter)

To create the user interface, I used the Tkinter library, which allows for the creation of graphical interfaces; I used `Entry` classes to capture user input. I will spare you the details of the UI design, but it was a rather long and tedious process.

 # The limitations of the option pricer

The Black-Scholes model and its formula remain a subject of considerable debate within the economics community.
Its underlying logic is viewed as overly simplistic, and it is true that the model's approach is disconnected from the realities of financial markets.
Critics point out that, because the model is based on a normal distribution (or Gaussian distribution), it underestimates "improbable" events such as financial crises.
Furthermore, this pricer only calculates European options (extending it to American options could be an avenue for exploration).
Alternatively, regarding the absence of dividends: for stocks that do not pay them, the pricing model works, but as soon as a stock begins paying dividends, the price becomes distorted.

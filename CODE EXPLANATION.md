# Explanation of the code and the mathematic model behind it

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

# Code implementation

To implement the Black Scholes formula in my code, I defined two functions, one for call and one for put :

To retrieve the parameters, I use the tkinter .get() function; I will come back to this in the UI section.

<img width="458" height="158" alt="image" src="https://github.com/user-attachments/assets/2f7f32b4-e65b-4a29-848f-fa14eab1827f" />
<img width="455" height="158" alt="image" src="https://github.com/user-attachments/assets/6d7abd5f-b4b8-476a-bae1-7f242a56e821" />

Same for greeks : 

<img width="458" height="245" alt="image" src="https://github.com/user-attachments/assets/df535f29-fea9-45a8-89ed-906b681e6085" />
<img width="529" height="128" alt="image" src="https://github.com/user-attachments/assets/9a7406dc-8a6f-4dfe-b38b-15829bee0b21" />
<img width="470" height="128" alt="image" src="https://github.com/user-attachments/assets/d0fe62f8-55f9-4781-b219-e60735e0add2" />
<img width="773" height="275" alt="image" src="https://github.com/user-attachments/assets/f94f1d9f-9dbc-4897-b162-f9b3fdfbcaf3" />
<img width="449" height="272" alt="image" src="https://github.com/user-attachments/assets/3fe69c79-85ec-43a3-87dc-cbc914f235ca" />

# Graph Simulation (GBM)
Using the same data employed in the Black-Scholes formula, it is possible to model a prediction of the underlying asset's price.

To simulate the price paths of an asset, we use the Euler-Maruyama scheme, a numerical method to solve stochastic differential equations (SDEs). A common SDE for modeling asset prices is the geometric Brownian motion:

<img width="110" height="20" alt="image" src="https://github.com/user-attachments/assets/1c1c437d-2a8d-406f-b76b-dd3b9455a9d6" />

(You will notice that  has been replaced by r to represent the risk-free interest rate (which replaces the constant drift).

We therefore reuse:
S0 – the price of the underlying asset
r – the risk-neutral interest rate
σ – the volatility
dW – the Wiener process or Brownian motion

We transform S using the logarithm to simplify the equation:

<img width="152" height="25" alt="image" src="https://github.com/user-attachments/assets/1c357b34-d50b-4bb9-a767-6fd459ea9a55" />

and by integrating the equation, we obtain the exact solution:

<img width="158" height="23" alt="image" src="https://github.com/user-attachments/assets/5ca57e83-8913-4e48-8935-bb491daea2fe" />

This solution is useful for understanding S and its dynamics, but for practical purposes, it is approximated using the Euler-Maruyama scheme.

<img width="175" height="24" alt="image" src="https://github.com/user-attachments/assets/3f3b75f7-3327-488a-aad9-9417feda5383" />

# Implementation of the Geometric Brownian movement in python :

<img width="471" height="260" alt="image" src="https://github.com/user-attachments/assets/75ea6fda-82fc-4dfd-ac8e-7e584bc35f24" />
<img width="473" height="158" alt="image" src="https://github.com/user-attachments/assets/110946fa-28a5-4d3c-b178-423c252ef82d" />

"Seed" is an arbitrary variable; I chose the year 2026 because that is when the code was created, but it could have been any number. This choice ensures the same results are obtained every time the code is run.

"t" represents te timestep, earlier in the code, the defaults value is 252, to represent the standard number of trading days

"n" is the number of paths, its default value is 1000.

# Example

Here is an example of how to use the pricer:

Consider an at-the-money call option, where S0 equals K (both equal to 100), volatility is 20%, maturity is one year, and the interest rate is zero.

<img width="395" height="248" alt="image" src="https://github.com/user-attachments/assets/f1096995-5b46-4a77-9729-eed0bba5e6d3" />

Results : 

<img width="394" height="247" alt="image" src="https://github.com/user-attachments/assets/11c3bf37-fa9e-48f9-a5d2-023221a7b65f" />

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

The model itself :

The Black-Scholes model and its formula remain a subject of considerable debate within the economics community.
Its underlying logic is viewed as overly simplistic, and it is true that the model's approach is disconnected from the realities of financial markets.
Critics point out that, because the model is based on a normal distribution (or Gaussian distribution), it underestimates "improbable" events such as financial crises.
Furthermore, this pricer only calculates European options (extending it to American options could be an avenue for exploration).
Alternatively, regarding the absence of dividends: for stocks that do not pay them, the pricing model works, but as soon as a stock begins paying dividends, the price becomes distorted.




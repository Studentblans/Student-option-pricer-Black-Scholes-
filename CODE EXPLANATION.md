# Explanation of the code and the mathematic model behind it :

So, I learn a few weeks ago what is an "option", I never heard of it in my classes at the university and I found the concept really interesting, especially the mathematic approach to analyse an option, that's what leads me to develop this option pricer (and to test my knowledge on the subject).

# Option in finance : definition

If you're not familiar with the concept of option, here is a quick overview of it :

An option is a contract between a buyer and a seller, either a call or a put, a call is a contract that gives the right (and not the obligation) for the buyer to acquire a share with an agreed price (named "striike") until a certain time noted T (also called "maturity") and a put is a contract that allows the buyer to sell a share at a certain price.
To use his right, the buyer has to purchase the option, and its amount is called the "prime", the Black-Scholes formula is the mathematical approach to determine this prime.

# Black-Scholes Model

The assumptions of the model :

The price of the underlying asset St follows a geometric Brownian motion with constant volatility σ and constant drift μ:
<img width="281" height="157" alt="image" src="https://github.com/user-attachments/assets/31ee796f-afd2-4387-833c-29fa7eb31f7d" />

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

The theoretical price of a call option—which grants the right, but not the obligation, to purchase asset S at value K on date T—is characterized by its payoff: (ST-K)+=max(ST-K;0)

It is given by the risk-neutral expectation of the discounted terminal payoff : C=𝔼(Payoffe-rT)

Consider the Black-Scholes formula:
C(S0,K,r,T,)=S0N(d1)-Ke-rTN(d2)
Similarly, the theoretical price of a put option with a payoff : (K-ST)+=max(K-ST;0) is given by: 
P(S0,K,r,T,)=-S0N(-d1)+Ke-rTN(-d2)
with :
N the cumulative distribution function of the standard normal distribution N(0,1) :
N(x)=-x12e-12u2du
d1=1T[ln(S0K)+(r+122)T]
d2=d1-T

2 - Option Greeks

The "Greeks" measure an option's price sensitivity to each parameter of the Black-Scholes model. It's 5 indicators : delta, gamma, theta, vega and rho.

Delta :  first derivative of the option price with respect to the price of the underlying asset


=∂∂S
call=N(d1)	put=N(d1)-1

Gamma : represents the convexity or curvature of an option's price in relation to the price of the underlying asset. It indicates whether the option's price tends to move faster or slower than the price of the underlying asset.

γcall=γput=∂2P∂S2=N'(d1)S0T

Theta : The cost (or gain) associated with the passage of time for an options portfolio. It measures how the passage of time affects the value of an option.


=-∂P∂T
call=-SN'(d1)2T-rKe-rTN(d2)		put=-SN'(d1)2T+rKe-rTN(-d2)

Vega : measurement of sensitivity to implied volatility

call=put=∂P∂=STN'(d1)

Rho : Rate of change of the premium value with respect to the risk-free rate.

=∂P∂r
call=KTe-rTN(d2)		put=-KTe-rTN(-d2)

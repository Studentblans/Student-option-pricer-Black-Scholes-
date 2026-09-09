from scipy.stats import norm
import math 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sys,os

black_scholes_result = 0
delta = 0
gamma = 0
theta = 0
rho = 0
vega = 0

#-----------------UI------------------------
from tkinter import *
window = Tk()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

#window
window.title("Student Option Pricer")
window.geometry("800x480")
window.minsize(800,480)
window.iconbitmap(resource_path("logo.ico"))
window.config(background='white')
window.resizable(width=False, height=False)

#pricer title
label_title = Label(window,
                    text="Option pricer made by a student (S.Blanchard)",
                    height=1,
                    relief=None,
                    fg='black',
                    font=("Calibri",14),
                    bg='white'
)
label_title.grid(row=0,column=0,columnspan=7, padx=10, pady=15)


#frame for call/put
call_put_frame = LabelFrame(window,
                            width=300,
                            text='Option Choice',
                            font=('Calibri',11,'italic'),
                            bg='white',
                            labelanchor='nw')
call_put_frame.grid(row=1,column=0, columnspan=2)

#puce choice call/put
vals = ['call','put']
etiqs = ['call','put']
varOption = StringVar()
varOption.set(vals[0])
for i in range(2):
    buttons = Radiobutton(call_put_frame,
                          variable=varOption,
                          text=etiqs[i],
                          value=vals[i],
                          indicatoron = 0,
                          bg='light grey')
    buttons.pack(side=LEFT, expand=1)

#parameters choice
spot_price_choice = DoubleVar() #S0
spot_price_choice.set(0)
spot_price = Entry(window,
               textvariable=spot_price_choice,
               width=30,
               bg='white',
               fg='black')

strike_price_choice = DoubleVar() #K
strike_price_choice.set(0)
strike_price = Entry(window,
                       textvariable=strike_price_choice,
                       bg='white',
                       fg='black')

rate_choice = DoubleVar() #r
rate_choice.set(0)
rate = Entry(window,
             textvariable=rate_choice,
             bg='white',
             fg='black')

maturity_choice = DoubleVar() #T
maturity_choice.set(0)
maturity = Entry(window,
                 textvariable=maturity_choice,
                 bg='white',
                 fg='black')

volatility_choice = DoubleVar() #sigma
volatility_choice.set(0)
volatility = Entry(window,
                   textvariable=volatility_choice,
                   bg='white',
                   fg='black')

spot_price.grid(row=2,column=1, sticky=W)
strike_price.grid(row=3,column=1, sticky=W)
rate.grid(row=4,column=1, sticky=W)
maturity.grid(row=5,column=1, sticky=W)
volatility.grid(row=6,column=1, sticky=W)

#indicators frame
S0_label = Label(window,
                text="S0",
                height=1,
                relief=None,
                fg='black',
                font=("Calibri",14),
                bg='white')
K_label = Label(window,
                text = "K",
                height = 1,
                relief=None,
                fg='black',
                font=("Calibri",14),
                bg='white')
r_label = Label(window,
                text ='r',
                relief=None,
                fg='black',
                font=("Calibri",14),
                bg='white')
T_label = Label(window,
                text = 'T',
                relief = None,
                fg='black',
                font=("Calibri",14),
                bg='white')
sigma_label = Label(window,
                    text = 'σ',
                    relief=None,
                    fg='black',
                    font=("Calibri",14),
                    bg='white')
S0_label.grid(row=2,column=0,)
K_label.grid(row=3,column=0)
r_label.grid(row=4,column=0)
T_label.grid(row=5,column=0)
sigma_label.grid(row=6,column=0)

#Black-Scholes result
result_text_label = Label(window,
                     text=f"Formula result : {black_scholes_result}",
                     relief=None,
                     fg='black',
                     font=('Calibri',14),
                     bg='white')
result_text_label.grid(row=7,column=0, columnspan=2, sticky=W)

#greeks label
greeks_label_title = Label(window,
                     text="Option Greeks :",
                     relief=None,
                     fg='black',
                     font=("Calibri",14),
                     bg='white')
greeks_label_title.grid(row=6,column=2,columnspan=5)

greeks_label_calculus = Label(window,
                              text=f"Δ = {delta} γ = {gamma} θ = {theta} ρ = {rho} ν = {vega}",
                              relief = None,
                              fg='black',
                              font=("Calibri",14),
                              bg='white')
greeks_label_calculus.grid(row=7,column=2,columnspan=5)

# simulation parameters
simulation_paremeters_title = Label(window,
                                    text = "Simulation parameters :",
                                    relief = None,
                                    fg='black',
                                    font=("Calibri",10),
                                    bg='white')
simulation_paremeters_title.grid(row=1, column=7, columnspan=2)
timestep_label = Label(window,
                       text="t :",
                       relief = None,
                       fg='black',
                       font=("Calibri",10),
                       bg='white')
paths_number_label = Label(window,
                           text="n :",
                           relief = None,
                           fg='black',
                           font=("Calibri",10),
                           bg="white")
timestep_label.grid(row=2,column=7)
paths_number_label.grid(row=3,column=7)

timestep = DoubleVar()
timestep.set(252)
timestep = Entry(window,
                 textvariable=timestep,
                 bg='white',
                 fg='black')
paths_number = DoubleVar()
paths_number.set(1000)
paths_number = Entry(window,
                 textvariable=paths_number,
                 bg='white',
                 fg='black')
timestep.grid(row=2,column=8)
paths_number.grid(row=3,column=8)

#----------------simulation graph----------------------
fig = plt.figure(figsize=(4,3), dpi=100)
ax = fig.add_subplot(111)
canvas_graph = FigureCanvasTkAgg(fig, master=window)
canvas_graph.get_tk_widget().grid(row=1, column=3, rowspan=5, columnspan=4)


#N(x) denotes the standard normal cumulative distribution function
#norm.cdf(x)
#N'(x) denotes the standard normal probability density function
#derivate of norm.cdf(x) or (1/(math.sqrt(2*math.pi))*math.exp(-(x**2)/2))

#---------------------calculate call and put---------------------------
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

#-----------------------Option greeks----------------------------
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

#--------------------start button command--------------------------------
def start_simulation():
    call_put_choice = varOption.get()
    try :
        if call_put_choice == "call":
            black_scholes_result = black_scholes_call()
            delta = delta_call()
            gamma = gamma_call_put()
            theta = theta_call()
            rho = rho_call()
            vega = vega_call_put()
        else:
            black_scholes_result = black_scholes_put()
            delta = delta_put()
            gamma = gamma_call_put()
            theta = theta_put()
            rho = rho_put()
            vega = vega_call_put()
        result_text_label.config(text=f"Formula result : {black_scholes_result:.2f}")
        greeks_label_calculus.config(text=f"Δ = {delta:.2f} γ = {gamma:.2f} θ = {theta:.2f} ρ = {rho:.2f} ν = {vega:.2f}")
    except ZeroDivisionError:
        result_text_label.config(text="/!\\ σ or T can't ≠ 0")
    except ValueError:
        result_text_label.config(text="/!\\ S0 and K should be +")

#------------Geometric brownian movement method (risk neutral)--------------
#Analytical solution of the GBM stochastic differential equation :
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


#execute function
def execute():
    start_simulation()
    geometric_brownian_movement_simulate_path()

#start button
start_button = Button(window,
                      text = "Start pricing",
                      command=execute)
start_button.grid(row=8,column=0,columnspan=9)

#display
window.mainloop()

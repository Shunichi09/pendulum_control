[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Documentation Status](https://travis-ci.org/Shunichi09/pendulum_control.svg?branch=master)

# pendulum_control
This repository is about controlling pendulum with cart. We use control method based on LQR theory and Learning theory

![original_simulation](https://github.com/Shunichi09/pendulum_control/blob/demo_gifs/pendulum_1.gif)

# DEMO
- LQR


# Problem formulation
We set the problem as controlling the pendulum with the cart.
The motion equation of the problem is as following.



The parameters are 

- mass of pendulums = 2 [kg]
- mass of cart = 8 [kg]
- viscous resistance coefficient of pendulum = 27.41 * 10e-6
- viscous resistance coefficient of cart = 27.41 * 10e-6
- pendulum inertia = 3.2 * 10e-4 

# Linear control
I assume the situation is around the equibliumpoints.
this problem become easier.
The state equation is defined as following

I applied 
- LQR method
- polar setting method
- Model Predictive Control method

# Nonlinear control
Sometimes the assumption of linearizing is not correct in real situation

I applied 
- SDRE method
- Nonlinear Model Predictive Control method

# Learning control
Reinforcement learning is widely used in recent years
I attemp to apply the method to this problem

- Q_learning method
- Montecarlo method

# Usage

```
$ python main.py
```

You can chose the control methods from following methods

- LQR

# Requirement
You should install following software

- python(3.5>)
- numpy
- matplotlib
- python-control
- slycot

# Licence
- MIT


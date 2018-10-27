# pendulum_control
This repository is about controlling pendulum. We use control method based on LQR theory and Learning theory

# Problem formulation
We set the problem as controlling the pendulum with the cart.
The motion equation of the problem is as following.



The parameter is 

mass of pendulums = 
mass of cart = 
fraction coefficient of pendulum = 
fraction coefficient of cart = 

Therefore, the problem is 

# Liner control
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

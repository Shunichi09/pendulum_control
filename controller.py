import math
import numpy as np
from control.matlab import lqr

class LQR():
    """
    Attributes
    ------------
    pendulum : SinglePendulumWithCart class
    A : numpy.ndarray
        Matrix A of state equation
    B : numpy.ndarray
        Matrix B of state equation 
    C : numpy.ndarray
        Matrix C of state equation 
    R : numpy.ndarray
        Matrix R of evaluation function 
    Q : numpy.ndarray
        Matrix R of evaluation function 
    
    Notes
    ---------
    this control method is calculated by the LQR methods 
    the state vector x is [z, th, v_z, v_th]
    """

    def __init__(self, pendulum):
        # controllers

        alpha_0 = pendulum.p_j * (pendulum.p_m + pendulum.c_m) + pendulum.c_m * pendulum.p_m * (pendulum.p_l**2)
        inerter_mass = pendulum.p_j + pendulum.p_m * (pendulum.p_l**2) 
        mass = pendulum.p_m + pendulum.c_m
        
        self.A = np.array([[0.0, 0.0, 1.0, 0.0], 
                           [0.0, 0.0, 0.0, 1.0],
                           [0.0, 0.0, 0.0, 0.0],
                           [0.0, 0.0, 0.0, 0.0]])

        self.A[2, 1] = - (pendulum.p_m**2) * (pendulum.p_l**2) * pendulum.g / alpha_0
        self.A[2, 2] = - pendulum.c_mu * inerter_mass / alpha_0
        self.A[2, 3] = pendulum.p_mu * pendulum.p_m * pendulum.p_l / alpha_0

        self.A[3, 1] = mass * pendulum.p_m * pendulum.p_l * pendulum.g / alpha_0
        self.A[3, 2] = pendulum.c_mu * pendulum.p_m * pendulum.p_l / alpha_0
        self.A[3, 3] = - pendulum.p_mu * mass / alpha_0

        self.B = np.array([[0.0], 
                           [0.0],
                           [0.0],
                           [0.0]])

        self.B[2, 0] = inerter_mass / alpha_0
        self.B[3, 0] = -pendulum.p_m * pendulum.p_l / alpha_0
        
        self.C = np.array([[1.0, 0.0, 0.0, 0.0], 
                           [0.0, 1.0, 0.0, 0.0]])

        self.R = 5.0

        self.Q = np.diag([10, 10, 10, 10])

        self.K, self.P, self.e = lqr(self.A, self.B, self.Q, self.R)

    def calc_input(self, pendulum):
        """
        Parameters
        -------------
        pendulum : pendulum class

        Returns
        ----------
        f : float in [N]
            input of the system
        """
        state = np.array([pendulum.z, pendulum.th, pendulum.v_z, pendulum.v_th])
        f = - self.K * state.T

        return f
        



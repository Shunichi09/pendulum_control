import math
import numpy as np
from control.matlab import lqr

class SDRE():
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
        # initialize
        self.A = np.array([[0.0, 0.0, 1.0, 0.0], 
                           [0.0, 0.0, 0.0, 1.0],
                           [0.0, 0.0, 0.0, 0.0],
                           [0.0, 0.0, 0.0, 0.0]])

        self.B = np.array([[0.0], 
                           [0.0],
                           [0.0],
                           [0.0]])

        self.C = np.array([[1.0, 0.0, 0.0, 0.0], 
                           [0.0, 1.0, 0.0, 0.0]])

        self.R = 0.0
        self.Q = np.zeros((4, 4))

    def calc_input(self, pendulum, reference_z=None):
        """
        Parameters
        -------------
        pendulum : pendulum class

        Returns
        ----------
        f : float in [N]
            input of the system
        """

        # freeze the state
        self._freeze_state(pendulum)
        self._freeze_weight(pendulum)

        K, P, e  = lqr(self.A, self.B, self.Q, self.R)
        
        state = np.array([[pendulum.z], [pendulum.th], [pendulum.v_z], [pendulum.v_th]])

        if reference_z is not None:
            state = np.array([[pendulum.z - reference_z], [pendulum.th], [pendulum.v_z], [pendulum.v_th]])

        f = - np.dot(K, state)

        return f

    def _freeze_state(self, pendulum):
        """
        freeze state
        
        Parameters
        ------------
        pendulum : pendulum class

        """

        M = np.array([[pendulum.c_m + pendulum.p_m , pendulum.p_m * pendulum.p_l * math.cos(pendulum.th)],
                      [pendulum.p_m * pendulum.p_l * math.cos(pendulum.th), pendulum.p_j + pendulum.p_m * (pendulum.p_l**2.)]])
        
        N = np.array([[0.0, -pendulum.p_m * pendulum.p_l * math.sin(pendulum.th) * pendulum.v_th], 
                      [0.0, 0.0 ]])
        
        G = np.array([[0.0, 0.0],
                      [0.0, -pendulum.g * pendulum.p_m * pendulum.p_l * self._h(pendulum.th)]])

        L = np.array([[1.0], [0.0]])

        self.A[2:, :2] = - np.dot(np.linalg.inv(M), G)
        self.A[2:, 2:] = - np.dot(np.linalg.inv(M), N)
        self.B[2:, :] = np.dot(np.linalg.inv(M), L)

        print("A = {0}".format(self.A))
        print("B = {0}".format(self.B))
        
    def _freeze_weight(self, pendulum):
        """
        freeze the weight

        Parameters
        -----------
        pendulum : pendulunm class
        """

        self.R = 10000.0 # + 10000.0 / (1.0 + math.exp(100.0*((abs(pendulum.th)-0.1))))
        self.Q[0, 0] = 1000.0  # + 10000.0 / (1.0 + math.exp(-100.0*((abs(pendulum.z)-2.5))))
        self.Q[1, 1] = 1.0 # + 10000.0 / (1.0 + math.exp(100.0*((abs(pendulum.th)-0.1))))
        self.Q[2, 2] = 1000.0 # + 10000.0 / (1.0 + math.exp(100.0*((abs(pendulum.th)-0.1))))
        self.Q[3, 3] = 1000.0

    def _h(self, th):
        """
        """
        threshold = 0.001
        ep = 0.01

        if abs(th) < threshold:
            h = 1.
        else:
            h = (math.sin(th) + 0.01 * math.exp(-100 * ((abs(th) - math.pi)**2) )) / (th + ep)

        # print("h = {0}".format(h))

        return h


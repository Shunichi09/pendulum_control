# pendulum simulator
import numpy as np
import 

class SinglePendulum():
    """
    Attributes
    ------------
    th : float in radians
        pendulum angle
    z : float in meters
        cart position
    history_th : list
        time history of pendulum angle
    history_z : list
        time history of cart position
    
    Notes
    --------
    state definition is writen in README 
    """

    def __init__(self, init_th=0.0, init_v_th=0.0, init_z=0.0, init_v_z=0.0):
        """
        Parameters
        --------------
        init_th : float in radians
            initial pendulum angle, defalt is 0.0
        init_v_th : float in radians
            initial pendulum angle, defalt is 0.0
        init_z : float in meters
            initial cart position, defalt is 0.0
        init_v_z : float in meters
            initial cart position, defalt is 0.0
        """
        self.th = init_th
        self.v_th = init_v_th
        self.z = init_z
        self.v_z = init_v_z
        self.history_th = []
        self.history_v_th = []
        self.history_z = []
        self.history_v_z = []

    def update_state(self, dt=0.01):
        """
        Parameters
        -------------
        dt : float in seconds
            sampling time of simulation

        Notes
        --------
        the state is updated by 4th Runge-Kutta method
        """

        # Parameters
        p_m = 0.023 # pendulum weight
        p_l = 0.2 # pendulum length, especially the length from origin to center gravity position( 0.4 / 2 )
        p_j = 3.2 * 10e-4 # pendulum inertia
        mu = 27.41 * 10e-6 # viscous resistance coefficient of pendulum
        zeta = 240.0
        xi = 90.0 # parameter of cart

        # Runge-Kutta method



        # update
        self.th += 1/6 * ()
        self.z += 1/6 * ()
        self.v_th += 
        self.v_z += 

    def _z(self):
        """
        """

        k1 = self.z
        k2 = self.z + 0.5 * k1 * self.dt
        k3 = self.z + 0.5 * k2 * self.dt
        k4 = self.z + k3 * self.dt

        return k1, k2, k3, k4

    def _th(self):
        """
        """

        k1 = self.th
        k2 = self.th + 0.5 * k1 * self.dt
        k3 = self.th + 0.5 * k2 * self.dt
        k4 = self.th + k3 * self.dt

        return k1, k2, k3, k4
    
    def _v_th(self):
        """
        """

        k1 = sel
        k2 = self.th + 0.5 * k1 * self.dt
        k3 = self.th + 0.5 * k2 * self.dt
        k4 = self.th + k3 * self.dt

        return k1, k2, k3, k4


        

        






        


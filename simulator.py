# pendulum simulator
import numpy as np
import math
from common.math import fit_angle_in_rad_range

class SinglePendulumWithCart():
    """
    Attributes
    ------------
    z : float in meters
        cart position in z-coordinate
    th : float in radians
        pendulum angle
    v_z : float in m/s
         cart velocity in z-coordinate
    v_th : float in rad/s
        pendulum angle velocity
    history_z : list
        time history of cart position in z-coordinate
    history_th : list
        time history of pendulum angle
    history_v_z : list
        time history of cart velocity in z-coordinate
    history_v_th : list
        time history of pendulum angle velocity
    
    Notes
    --------
    state definition is writen in README 
    """

    def __init__(self, init_z=0.0, init_th=0.0, init_v_z=0.0, init_v_th=0.0):
        """
        Parameters
        --------------
        init_z : float in meters
            initial cart position, defalt is 0.0
        init_th : float in radians
            initial pendulum angle, defalt is 0.0
        init_v_z : float in meters
            initial cart position, defalt is 0.0
        init_v_th : float in radians
            initial pendulum angle, defalt is 0.0
        """
        self.z = init_z
        self.th = init_th

        self.v_z = init_v_z
        self.v_th = init_v_th

        self.history_z = []
        self.history_th = []
        self.history_v_th = []
        self.history_v_z = []
        self.history_input_f = []

        # Parameters
        self.p_m = 0.23 # pendulum mass
        self.p_l = 0.6096 # pendulum length, especially the length from origin to center gravity position( 0.4 / 2 )
        self.p_j = 3.2 * 10e-2 # pendulum inertia
        self.p_mu = 27.41 * 10e-6 # viscous resistance coefficient of pendulum

        self.c_m = 0.94 # cart mass
        self.c_mu = 27.41 * 10e-6 # viscous resistance coefficient of cart
        self.c_width = 0.25
        self.c_height = 0.1
        self.c_wheel_size = 0.025 # radius of wheel

        self.g = 9.8 # acceleration of gravity

    def update_state(self, input_f=0.0, dt=0.01):
        """
        Parameters
        -------------
        input_f : float in N
            input for the system, default is 0.0 [N]
        dt : float in seconds
            sampling time of simulation, default is 0.01 [s]

        Also see
        ------------
        _func_z
        _func_th
        _func_v_z
        _func_v_th

        all functions is defined by the motion equation 

        Notes
        --------
        the state is updated by 4th Runge-Kutta method
        """
        # Runge-Kutta method
        k0 = [0.0 for _ in range(4)]
        k1 = [0.0 for _ in range(4)]
        k2 = [0.0 for _ in range(4)]
        k3 = [0.0 for _ in range(4)]
        
        functions = [self._func_z, self._func_th, self._func_v_z, self._func_v_th]
        
        for i, func in enumerate(functions):
            k0[i] = dt * func(self.z, self.th, self.v_z, self.v_th, input_f)

        for i, func in enumerate(functions):
            k1[i] = dt * func(self.z + k0[0]/2.0 , self.th + k0[1]/2.0,
                         self.v_z + k0[2]/2.0, self.v_th + k0[3]/2.0, input_f)

        for i, func in enumerate(functions):
            k2[i] = dt * func(self.z + k1[0]/2.0 , self.th + k1[1]/2.0,
                         self.v_z + k1[2]/2.0, self.v_th + k1[3]/2.0, input_f)

        for i, func in enumerate(functions):
            k3[i] = dt * func(self.z + k2[0] , self.th + k2[1],
                         self.v_z + k2[2], self.v_th + k2[3], input_f)

        self.z += (k0[0] + 2 * k1[0] + 2 * k2[0] + k3[0]) / 6.0
        self.th += (k0[1] + 2 * k1[1] + 2 * k2[1] + k3[1]) / 6.0
        self.v_z += (k0[2] + 2 * k1[2] + 2 * k2[2] + k3[2]) / 6.0
        self.v_th += (k0[3] + 2 * k1[3] + 2 * k2[3] + k3[3]) / 6.0

        # self.th, = fit_angle_in_rad_range([self.th])
        # self.th = abs(self.th)

        variables = [self.z, self.th, self.v_z, self.v_th, input_f]
        histories = [self.history_z, self.history_th, self.history_v_z, self.history_v_th, self.history_input_f]

        for i, variable in enumerate(variables):
            histories[i].append(variable)
        
        # print('z = {0}'.format(self.z))
        # print('th = {0}'.format(self.th))
        # print('v_z = {0}'.format(self.v_z))
        # print('v_th = {0}'.format(self.v_th))

    def _func_z(self, z, th, v_z, v_th, input_f):
        """
        Parameters
        ------------
        z : float in meters
            cart position in z-coordinate
        th : float in radians
            pendulum angle
        v_z : float in m/s
            cart velocity in z-coordinate
        v_th : float in rad/s
            pendulum angle velocity
        input_f : float in N
            input for the system
        Returns
        -----------
        y : float
            Differential coefficient of z

        """

        y = v_z
        return y

    def  _func_th(self, z, th, v_z, v_th, input_f):
        """
        Parameters
        ------------
        z : float in meters
            cart position in z-coordinate
        th : float in radians
            pendulum angle
        v_z : float in m/s
            cart velocity in z-coordinate
        v_th : float in rad/s
            pendulum angle velocity
        input_f : float in N
            input for the system
        Returns
        -----------
        y : float
            Differential coefficient of th

        """
        y = v_th
        return y

    def _func_v_z(self, z, th, v_z, v_th, input_f):
        """
        Parameters
        ------------
        z : float in meters
            cart position in z-coordinate
        th : float in radians
            pendulum angle
        v_z : float in m/s
            cart velocity in z-coordinate
        v_th : float in rad/s
            pendulum angle velocity
        input_f : float in N
            input for the system
        Returns
        -----------
        y : float
            Differential coefficient of v_z

        """
        
        alpha = self.p_j * (self.p_m + self.c_m) + self.c_m * self.p_m * (self.p_l**2) +\
               (self.p_m**2) * (self.p_l**2) * (math.sin(th)**2)

        mass_total = self.p_j + self.p_m * (self.p_l**2)

        temp_y = mass_total * input_f - self.c_mu * mass_total * v_z +\
                 self.p_mu * self.p_m * self.p_l * math.cos(th) * v_th +\
                 mass_total * self.p_m * self.p_l * math.sin(th) * (v_th**2) -\
                 (self.p_m**2) * (self.p_l**2) * self.g * math.sin(th) * math.cos(th)
        
        y = temp_y / alpha

        return y
    
    def _func_v_th(self, z, th, v_z, v_th, input_f):
        """
        Parameters
        ------------
        z : float in meters
            cart position in z-coordinate
        th : float in radians
            pendulum angle
        v_z : float in m/s
            cart velocity in z-coordinate
        v_th : float in rad/s
            pendulum angle velocity
        input_f : float in N
            input for the system

        Returns
        -----------
        y : float
            Differential coefficient of v_th
        """

        alpha = self.p_j * (self.p_m + self.c_m) + self.c_m * self.p_m * (self.p_l**2) +\
               (self.p_m**2) * (self.p_l**2) * (math.sin(th)**2)

        mass_total = self.p_m + self.c_m

        temp_y = -self.p_m * self.p_l * math.cos(th) * input_f +\
                  self.c_mu * self.p_m * self.p_l * math.cos(th) * v_z -\
                  self.p_mu * mass_total * v_th -\
                  (self.p_m**2) * (self.p_l**2) * math.sin(th) * math.cos(th) * (v_th**2) +\
                  mass_total * self.p_m * self.p_l * self.g * math.sin(th)

        y = temp_y / alpha

        return y 

# memo
    """
    coeffice_v_z = (self.p_m + self.c_m) -\
                    (self.p_m**2 * self.p_l**2 * math.cos(th)**2 / (self.p_j + self.p_m * self.p_l**2))
    
    const = - self.p_m * self.p_l * math.cos(th) / (self.p_j + self.p_m * self.p_l**2)

    temp_y = (self.p_m * self.p_l * self.g * math.sin(th) - self.p_mu * v_th) * const +\
                self.p_m * self.p_l * v_th**2 * math.sin(th) - self.c_mu * v_z + input_f

    y = temp_y / coeffice_v_z

    coeffice_v_th = (self.p_j + self.p_m + self.p_l**2) -\
                    (self.p_m**2 * self.p_l**2 * math.cos(th)**2 / (self.p_m + self.c_m))

    const = - self.p_m * self.p_l * math.cos(th) / (self.p_m + self.c_m)
    
    temp_y = (self.p_m * self.p_l * v_th**2 * math.sin(th) - self.c_mu * v_z + input_f) * const +\
                self.p_m * self.p_l * self.g * math.sin(th) - self.p_mu * v_th

    y = temp_y / coeffice_v_th
    """


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import matplotlib.font_manager as fon
import sys
import math
# del fon.weight_dict['roman']
# fon._rebuild()

# default setting of figures
plt.rcParams['font.family'] = 'Times New Roman' # Fonts
plt.rcParams["mathtext.fontset"] = 'stix' # math fonts
plt.rcParams['xtick.direction'] = 'in' # x axis in
plt.rcParams['ytick.direction'] = 'in' # y axis in 
plt.rcParams["font.size"] = 10
plt.rcParams['axes.linewidth'] = 1.0 # axis line width
plt.rcParams['axes.grid'] = True # make grid

class FigDrawer():
    """create figure of path and robot

    This class could creat the following figures
    
    Attributes
    ------------
    time_history_fig : figure of matplotlib
        this figure shows the time_history
    z_axis : axis of matplotlib
        this axis shows the time_history
    th_axis : axis of matplotlib
        this axis shows the time_history
    v_z_axis : axis of matplotlib
        this axis shows the time_history
    v_th_axis : axis of matplotlib
        this axis shows the time_history
    input_fig : figure of matplotlib
        this figure shows the inputs
    input_f_axis : axis of matplotlib
        this axis shows the u_vs
    """
    def __init__(self, pendulum):
        """
        Parameters
        ------------
        pendulum : SinglePendulumWithCart class
        """
        self.pendulum = pendulum

        # setting up figure
        self.time_history_fig = plt.figure(dpi=100)
        self.z_axis = self.time_history_fig.add_subplot(411)
        self.th_axis = self.time_history_fig.add_subplot(412)
        self.v_z_axis = self.time_history_fig.add_subplot(413)
        self.v_th_axis = self.time_history_fig.add_subplot(414)

        self.input_fig = plt.figure(dpi=100)
        self.input_f_axis = self.input_fig.add_subplot(111)
        
    def draw_fig(self, dt=0.01):
        """draw the figures

        Parameters
        -----------
        dt : float in seconds
            sampling time of system default is 1 [ms]

        """
        self.dt = dt
        self._set_axis()
        self._draw_fig()

        plt.show()

    
    def _set_axis(self):
        """ initialize the animation axies
            this private method execute as following
        
        executing list
        ----------------
            (1) : set the axis name
            (2) : set the xlim and ylim
        """
        # (1) set the axis name
        self.z_axis.set_xlabel(r'time [s]')
        self.z_axis.set_ylabel(r'$\it{z}$ [m]')
        self.th_axis.set_xlabel(r'time [s]')
        self.th_axis.set_ylabel(r'$\it{th}$ [rad]')
        self.v_z_axis.set_xlabel(r'time [s]')
        self.v_z_axis.set_ylabel(r'$\it{v_z}$ [m]')
        self.v_th_axis.set_xlabel(r'time [s]')
        self.v_th_axis.set_ylabel(r'$\it{v_th}$ [rad]')

        self.input_f_axis.set_xlabel(r'time [s]')
        self.input_f_axis.set_ylabel(r'$\it{f} $')

    def _draw_fig(self):
        """plot the data
        """
        self._draw_time_history()
        # self._draw_input()

        plt.show()
    
    def _draw_time_history(self):
        """plot time histories of state 
        """
        times = np.arange(len(self.pendulum.history_z)) * self.dt
        self.z_axis.plot(times, self.pendulum.history_z, label="z")
        self.th_axis.plot(times, self.pendulum.history_th, label="th")
        self.v_z_axis.plot(times, self.pendulum.history_v_z, label="v_z")
        self.v_th_axis.plot(times, self.pendulum.history_v_th, label="v_th")
        plt.legend()
    
    def _draw_input(self):
        """plot time histories of input
        """
        times = np.arange(len(self.pendulum.history_input_f)) * self.dt
        self.input_f_axis.plot(times, self.pendulum.history_input_f, label="input")
        plt.legend()

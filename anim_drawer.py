import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import matplotlib.font_manager as fon
import sys
import math

# functions
from common.drawing_tools import circle_make, square_make

# default setting of figures
plt.rcParams['font.family'] = 'Times New Roman' # Fonts
plt.rcParams["mathtext.fontset"] = 'stix' # math fonts
plt.rcParams['xtick.direction'] = 'in' # x axis in
plt.rcParams['ytick.direction'] = 'in' # y axis in 
plt.rcParams["font.size"] = 10
plt.rcParams['axes.linewidth'] = 1.0 # axis line width
plt.rcParams['axes.grid'] = True # make grid

class AnimDrawer():
    """create animation of pendulum with cart
    
    Attributes
    ------------
    pendulum : pendulum class
    anim_fig : figure of matplotlib
    axis : axis of matplotlib

    """

    def __init__(self, pendulum):
        """
        Parameters
        ------------
        pendulum : SinglePendulumWithCart class
        
        """
        self.pendulum = pendulum

        # setting up figure
        self.anim_fig = plt.figure(dpi=150)
        self.axis = self.anim_fig.add_subplot(111)

        # imgs
        self.p_imgs = [] # img of pendulum
        self.c_imgs = [] # img of cart

    def draw_anim(self, interval=10):
        """draw the animation and save

        Parameteres
        -------------
        interval : int, optional
            animation's interval time, you should link the sampling time of systems
            default is 10 [ms]

        """
        self._set_axis()
        self._set_img()

        animation = ani.FuncAnimation(self.anim_fig, self._update_anim, interval=interval, frames=len(self.pendulum.history_z)-1)

        # self.axis.legend()
        print('save_animation?')
        shuold_save_animation = int(input())

        if shuold_save_animation: 
            print('animation_number?')
            num = int(input())
            animation.save('pendulum_{0}.mp4'.format(num), writer='ffmpeg')
            # animation.save("Sample.gif", writer = 'imagemagick') # gif保存

        plt.show()

    def _set_axis(self):
        """ initialize the animation axies
            this private method execute as following

            (1) : set the axis name
            (2) : set the xlim(= +-5.0) and ylim(= -2.0~+5.0) 
        """
        # (1) set the axis name
        self.axis.set_xlabel(r'$\it{x}$ [m]')
        self.axis.set_ylabel(r'$\it{y}$ [m]')
        self.axis.set_aspect('equal', adjustable='box')

        # (2) set the xlim and ylim
        max_x = 2.5
        min_x = -2.5
        max_y = 1.0 
        min_y = -0.5
        
        self.axis.set_xlim(min_x, max_x)
        self.axis.set_ylim(min_y, max_y)         

    def _set_img(self):
        """ initialize the imgs of animation
            this private function execute the make initial imgs for animation

            following imgs will creat
            pendulum_imgs is composed of [pendulum]
            cart_imgs is composed of [cart wheels * 2, cart]
            
        """
        # pendulum img
        p_color_list = ["b"]

        temp_img, = self.axis.plot([], [], color=p_color_list[0], linewidth=5)
        self.p_imgs.append(temp_img)
    
        # cart imgs
        c_color_list = ["k", "k", "k"] 

        for i in range(len(c_color_list)):
            temp_img, = self.axis.plot([],[], color=c_color_list[i])
            self.c_imgs.append(temp_img)

    def _update_anim(self, i):
        """the update animation
        this function should be used in the animation functions

        Parameters
        ------------
        i : int
            time step of the animation
            the sampling time should be related to the sampling time of system

        Returns
        -----------
        p_imgs : list of img
            this list is including 1 imgs
        c_imgs : list of img
            this list is including 3 imgs
        """
        self._draw_pendulum(i)
        self._draw_cart(i)
        
        return self.p_imgs, self.c_imgs
    
    def _draw_pendulum(self, i):
        """
        This private function is just divided thing of
        the _update_anim to see the code more clear
        Drawing pendulum

        Parameters
        ------------
        i : int
            time step of the animation
            the sampling time should be related to the sampling time of system
        """
        p_x = [self.pendulum.history_z[i], self.pendulum.history_z[i] + 2 * self.pendulum.p_l * math.sin(self.pendulum.history_th[i])]
        p_y = [0.0, 2 * self.pendulum.p_l * math.cos(self.pendulum.history_th[i])]

        self.p_imgs[0].set_data([p_x, p_y])

    def _draw_cart(self, i):
        """
        This private function is just divided thing of
        the _update_anim to see the code more clear
        Drawing pendulum

        Parameters
        ------------
        i : int
            time step of the animation
            the sampling time should be related to the sampling time of system
        """
        # cart
        xs, ys = square_make(self.pendulum.history_z[i], 0.0, width=self.pendulum.c_width, height=self.pendulum.c_height)
        self.c_imgs[0].set_data([xs, ys])

        # wheel 1
        center_x = self.pendulum.history_z[i] + self.pendulum.c_width/2 - self.pendulum.c_wheel_size
        center_y = - self.pendulum.c_height/2 - self.pendulum.c_wheel_size

        wheel_xs, wheel_ys = circle_make(center_x, center_y, self.pendulum.c_wheel_size)
        self.c_imgs[1].set_data([wheel_xs, wheel_ys])

        # wheel 2
        center_x = self.pendulum.history_z[i] - self.pendulum.c_width/2 + self.pendulum.c_wheel_size
        center_y = - self.pendulum.c_height/2 - self.pendulum.c_wheel_size

        wheel_xs, wheel_ys = circle_make(center_x, center_y, self.pendulum.c_wheel_size)
        self.c_imgs[2].set_data([wheel_xs, wheel_ys])


    




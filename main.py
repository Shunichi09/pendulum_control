# main program of pendulum control
import numpy as np
import matplotlib.pyplot as plt
import math

from simulator import SinglePendulumWithCart
from controllers.LQR import LQR
from controllers.SDRE import SDRE
from anim_drawer import AnimDrawer
from fig_drawer import FigDrawer

def main():
    print("please set initial state of pendulum angle theta (cart position z is always 0.0)")

    th = float(input())

    # pendulum = SinglePendulumWithCart(init_z=-0.1, init_th= -20. * math.pi / 180., init_v_th= 50. * math.pi / 180.)

    pendulum = SinglePendulumWithCart(init_z=-0.5, init_th= th, init_v_th= -100. * math.pi / 180.)

    print("please chose controller ! you can chose [LQR], [SDRE]")
    controller = input()

    if controller == "LQR":
        controller = LQR(pendulum)
    elif controller == "SDRE":
        controller = SDRE(pendulum) 
    else:
        raise ValueError("you should chose controller from LQR , SDRE!!")

    simulation_time = 2000
    sampling_time = 0.01

    reference_z_history = []

    for step in range(simulation_time):
        
        time = step * sampling_time
        """
        T = 10.0
        reference_z = 0.2 * math.sin((2 * math.pi) / T * time)
        reference_z_history.append(reference_z)
        """

        reference_z = None

        f = controller.calc_input(pendulum, reference_z)

        # f[0, 0] = 0.0
        """
        if step == 1000:
            f[0, 0] = 100.0
        """
        
        pendulum.update_state(input_f=f[0, 0], dt=0.01)

    anim = AnimDrawer(pendulum)
    anim.draw_anim(interval=10)

    # plt.plot(range(len(reference_z_history)), reference_z_history)
    # plt.show()
    
    fig = FigDrawer(pendulum, controller)
    fig.draw_fig(dt=0.01)

if __name__ == '__main__':
    main()
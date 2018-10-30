# main program of pendulum control
import numpy as np
import matplotlib.pyplot as plt

from simulator import SinglePendulumWithCart
from controllers.LQR import LQR
from anim_drawer import AnimDrawer
from fig_drawer import FigDrawer

def main():
    
    pendulum = SinglePendulumWithCart(init_th=0.05)
    
    controller = LQR(pendulum)

    simulation_time = 2000

    for _ in range(simulation_time):
        f = controller.calc_input(pendulum)
        # f[0, 0] = 0.0
        pendulum.update_state(input_f=f[0, 0], dt=0.01)

    anim = AnimDrawer(pendulum)
    anim.draw_anim(interval=10)
    
    fig = FigDrawer(pendulum)
    fig.draw_fig(dt=0.01)

if __name__ == '__main__':
    main()
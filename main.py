# main program of pendulum control
import numpy as np
import matplotlib.pyplot as plt

from simulator import SinglePendulum
from animation import Anim

def main():
    
    pendulum = SinglePendulum(init_th=0.1)
    anim = Anim
    
    # controller = SDRE()

    simulation_time = 10000

    for t in range(simulation_time):

        # opt_f = controller.calc_input(pendulum.state)
        
        pendulum.update_state(input_f=0.0)
    
    anim.write_anim
    

if __name__ == '__main__':
    main()



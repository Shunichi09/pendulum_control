import math
import numpy as np

def circle_make(center_x, center_y, radius):
    '''
    Create circle matrix

    Parameters
    -------
    center_x : float
        the center x position of the circle
    center_y : float
        the center y position of the circle
    radius : float

    Returns
    -------
    circle x : numpy.ndarray
    circle y : numpy.ndarray
    '''

    point_num = 100 # 分解能

    circle_xs = []
    circle_ys = []

    for i in range(point_num + 1):
        circle_xs.append(center_x + radius * math.cos(i*2*math.pi/point_num))
        circle_ys.append(center_y + radius * math.sin(i*2*math.pi/point_num))

    return np.array(circle_xs), np.array(circle_ys)

def square_make(center_x, center_y, width=1.0, height=1.0):
    '''
    Create square matrix with angle line matrix(2D)
    
    Parameters
    -------
    center_x : float in meters
        the center x position of the square
    center_y : float in meters
        the center y position of the square
    width : float in meters
        the square's width, default is 1.0
    height : float in meters
        the square's height, default is 1.0

    Returns
    -------
    square xs : numpy.ndarray
        lenght is 5 (counterclockwise from right-up)
    square ys : numpy.ndarray
        length is 5 (counterclockwise from right-up)
    '''

    # start with the up right points
    # create point in counterclockwise
    height /= 2
    width /= 2

    square_xys = np.array([[width, height], [-width, height], [-width, -height], [width, -height], [width, height]])
    square_points = square_xys.T + np.array([[center_x], [center_y]])

    square_xs = square_points[0, :]
    square_ys = square_points[1, :]

    return square_xs, square_ys
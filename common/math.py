import math
import numpy as np

def fit_angle_in_rad_range(angles, min_angle=(-math.pi), max_angle=(math.pi)):
    """
    Check angle range and correct the range
    Parameters
    -------
    angle : array-like
        unit is radians
    min_angle : float 
        maximum of range in radians, default -math.pi
    max_angle : float 
        minimum of range in radians, default math.pi
    Returns
    -------
    correct_angle : numpy.ndarray
        correct range angle in radians
    """

    if max_angle < min_angle:
        raise ValueError('max angle must be greater than min angle')
    if (max_angle - min_angle) < 2.0 * math.pi:
        raise ValueError('difference between max_angle and min_angle must be greater than 2.0 * pi')
    
    output = np.array(angles)
    output_shape = output.shape

    output = output.flatten()
    output -= min_angle
    output %= 2 * math.pi
    output += 2 * math.pi
    output %= 2 * math.pi
    output += min_angle

    output = np.minimum(max_angle, np.maximum(min_angle, output))
    return output.reshape(output_shape)
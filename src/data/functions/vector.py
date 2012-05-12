import math

def calculate_shift(base, angle, length):
    angle = (angle-90)*0.00555*math.pi
    
    x_shift = round(length*math.cos(angle))
    y_shift = round(length*math.sin(angle))
    
    base[0] += x_shift
    base[1] += y_shift
    return base
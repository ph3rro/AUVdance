
'''Right.right outputs and array of format [duration, x_thrust, y_thrust, z_thrust, angular_thrust]
    secs: Duration of movement in seconds
    strength: Strength of thrust out of 1000.0
    spin: Strength of rotation out of 1000'''
def right(secs, strength, spin = 0):
    neutral = 500.0
    return [secs, 0, 0 + strength, neutral, 0 + spin]

'''Right.diagonal_right outputs and array of format [duration, x_thrust, y_thrust, z_thrust, angular_thrust]
    secs: Duration of movement in seconds
    strength_right: Strength of thrust left out of 1000.0
    strength_forward: Strength of thrust forward out of 1000.0
    spin: Strength of rotation out of 1000'''
def diagonal_right(secs, strength_right, strength_forward, spin = 0):
<<<<<<< HEAD
    neutral = 0.0
=======
    neutral = 50.0
>>>>>>> 32c588aecb53d3606f344c96114f924956884dcf
    return [secs, 0 + strength_forward, 0 + strength_right, neutral, 0 + spin]

'''Right.diagonal_up_right outputs and array of format [duration, x_thrust, y_thrust, z_thrust, angular_thrust]
    secs: Duration of movement in seconds
    strength_right: Strength of thrust right out of 1000.0
    strength_forward: Strength of thrust forward out of 1000.0
    strength_up: Strength of thrust up out of 1000.0
    spin: Strength of rotation out of 1000'''
def diagonal_up_right(secs, strength_right, strength_forward, strength_up, spin = 0):
<<<<<<< HEAD
    neutral = 0.0
=======
    neutral = 50.0
>>>>>>> 32c588aecb53d3606f344c96114f924956884dcf
    return [secs, 0 + strength_forward, 0 + strength_right, neutral + strength_up, 0 + spin]

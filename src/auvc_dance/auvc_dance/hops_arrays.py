
'''Hops.hop outputs and array of format [duration, x_thrust, y_thrust, z_thrust, angular_thrust]
    secs: Duration of movement in seconds
    strength: Strength of thrust out of 1000.0
    spin: Strength of rotation out of 1000'''
def hop(secs, strength, spin = 0):
<<<<<<< HEAD
    neutral = 0.0
=======
    neutral = 50.0
>>>>>>> 32c588aecb53d3606f344c96114f924956884dcf
    return [secs, 0, 0, neutral + strength, 0 + spin]

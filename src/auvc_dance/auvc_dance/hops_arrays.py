
'''Hops.hop outputs and array of format [duration, x_thrust, y_thrust, z_thrust, angular_thrust]
    secs: Duration of movement in seconds
    strength: Strength of thrust out of 1000.0
    spin: Strength of rotation out of 1000'''
def hop(secs, strength, spin = 0):
    neutral = 0.0
    return [secs, 0, 0, neutral + strength, 0 + spin]

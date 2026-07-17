'''Back.back outputs and array of format [duration, x_thrust, y_thrust, z_thrust, angular_thrust]
    secs: Duration of movement in seconds
    strength: Strength of thrust out of 1000.0
    spin: Strength of rotation out of 1000'''
def back(secs, strength, spin=0):
    neutral = 50.0
    return [secs, 0 - strength, 0, neutral, 0 + spin]

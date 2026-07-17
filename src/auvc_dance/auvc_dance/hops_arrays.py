class Hops:
    '''Hops.hop outputs and array of format [duration, x_thrust, y_thrust, z_thrust, angular_thrust]
       secs: Duration of movement in seconds
       strength: strength of thrust out of 500.0
       spin: strangth of rotation out of 500'''
    def hop(secs, strength, spin = 0):
        neutral = 500.0
        return [secs, neutral, neutral, neutral + strength, neutral + spin]
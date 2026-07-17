class Back:
    '''Back.back outputs and array of format [duration, x_thrust, y_thrust, z_thrust, angular_thrust]
       secs: Duration of movement in seconds
       strength: Strength of thrust out of 500.0
       spin: Strength of rotation out of 500'''
    def back(secs, strength, spin):
        neutral = 500.0
        return [secs, neutral - strength, neutral, neutral, neutral + spin]
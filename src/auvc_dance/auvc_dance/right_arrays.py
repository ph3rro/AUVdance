class Right:
    '''Right.right outputs and array of format [duration, x_thrust, y_thrust, z_thrust, angular_thrust]
       secs: Duration of movement in seconds
       strength: Strength of thrust out of 500.0
       spin: Strength of rotation out of 500'''
    def right(secs, strength, spin = 0):
        neutral = 500
        return [secs, neutral, neutral + strength, neutral, neutral + spin]
    
    '''Right.diagonal_right outputs and array of format [duration, x_thrust, y_thrust, z_thrust, angular_thrust]
       secs: Duration of movement in seconds
       strength_right: Strength of thrust left out of 500.0
       strength_forward: Strength of thrust forward out of 500.0
       spin: Strength of rotation out of 500'''
    def diagonal_left(secs, strength_right, strength_forward, spin = 0):
        neutral = 500
        return [secs, neutral + strength_forward, neutral + strength_right, neutral, neutral + spin]
    
    '''Right.diagonal_up_right outputs and array of format [duration, x_thrust, y_thrust, z_thrust, angular_thrust]
       secs: Duration of movement in seconds
       strength_right: Strength of thrust right out of 500.0
       strength_forward: Strength of thrust forward out of 500.0
       strength_up: Strength of thrust up out of 500.0
       spin: Strength of rotation out of 500'''
    def diagonal_up_left(secs, strength_right, strength_forward, strength_up, spin = 0):
        neutral = 500
        return [secs, neutral + strength_forward, neutral + strength_right, neutral + strength_up, neutral + spin]
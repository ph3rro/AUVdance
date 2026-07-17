class Left:
    '''Left.left outputs and array of format [duration, x_thrust, y_thrust, z_thrust, angular_thrust]
       secs: Duration of movement in seconds
       strength: Strength of thrust out of 500.0
       spin: Strength of rotation out of 500'''
    def left(secs, strength, spin = 0):
        neutral = 500.0
        return [secs, 0, 0 - strength, neutral, 0 + spin]
    
    '''Left.diagonal_left outputs and array of format [duration, x_thrust, y_thrust, z_thrust, angular_thrust]
       secs: Duration of movement in seconds
       strength_left: Strength of thrust left out of 500.0
       strength_forward: Strength of thrust forward out of 500.0
       spin: Strength of rotation out of 500'''
    def diagonal_left(secs, strength_left, strength_forward, spin = 0):
        neutral = 500.0
        return [secs, 0 + strength_forward, 0 - strength_left, neutral, 0 + spin]
    
    '''Left.diagonal_up_left outputs and array of format [duration, x_thrust, y_thrust, z_thrust, angular_thrust]
       secs: Duration of movement in seconds
       strength_left: Strength of thrust left out of 500.0
       strength_forward: Strength of thrust forward out of 500.0
       strength_up: Strength of thrust up out of 500.0
       spin: Strength of rotation out of 500'''
    def diagonal_up_left(secs, strength_left, strength_forward, strength_up, spin = 0):
        neutral = 500.0
        return [secs, 0 + strength_forward, 0 - strength_left, neutral + strength_up, 0 + spin]
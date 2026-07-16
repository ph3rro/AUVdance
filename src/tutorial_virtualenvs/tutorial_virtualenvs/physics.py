import numpy as np
def calculate_buoyancy(V, density_fluid):
    return V*density_fluid*9.81 # Newtons

def will_it_float(V, mass):
    return calculate_buoyancy(V, 1000, mass) >= mass * 9.81

def calculate_pressure(depth):
    return 1000*9.81*depth

def calculate_acceleration(F, m):
    return F/m

def calculate_angular_acceleration(tau, I):
    return tau/I

def calculate_torque(F_magnitude, F_direction, r):
    return F_magnitude*r*np.sin(F_direction)

def calculate_moment_of_inertia(m, r):
    return (m * r**2)

def calculate_auv_acceleration(F_magnitude, F_angle, mass, volume, length, width, thruster_distance=0.5):
    return (F_magnitude / mass)

def calculate_auv_inertia(mass, length, width, thruster_distance):
    return (mass*(length**2 + width**2)/12 + calculate_moment_of_inertia(mass, thruster_distance))

def calculate_auv_angular_acceleration(F_magnitude, F_angle, mass, volume, length, width, thruster_distance=0.5):
    torque = thruster_distance * F_magnitude * np.sin(F_angle) # R x F
    inertia = calculate_auv_inertia(mass, length, width, thruster_distance)
    return (torque/inertia)

def calculate_auv2_acceleration(T, alpha, theta, mass=100.0):
    F_x = (np.cos(alpha+theta))*T[0]
    F_y = (np.sin(alpha+theta))*T[0]
    
    F_x += (np.cos(-alpha+theta))*T[1]
    F_y += (np.sin(-alpha+theta))*T[1]
    
    F_x += (np.cos(alpha+theta+np.pi))*T[2]
    F_y += (np.sin(alpha+theta+np.pi))*T[2]
    
    F_x += (np.cos(-alpha+theta+np.pi))*T[3]
    F_y += (np.sin(-alpha+theta+np.pi))*T[3]
    
    return np.array([F_x / mass, F_y / mass])

def calculate_auv2_angular_acceleration(T, alpha, L, l, inertia):
    
    r = np.sqrt((L**2) + (l**2))
    thruster_offset = np.arctan(l/L)
    torque=0
    torque += T[0]*np.sin(thruster_offset + alpha)
    torque -= T[1]*np.sin(thruster_offset + alpha)
    torque += T[2]*np.sin(thruster_offset + alpha)
    torque -= T[3]*np.sin(thruster_offset + alpha)

    return torque*r/inertia

def simulate_auv2_motion(T, alpha, L, l, mass, inertia, dt, t_final, x0, y0, theta0):
    
    length = int(t_final/dt+1)
    theta = np.zeros((length), dtype=np.float64)
    theta[0] = theta0
    xy = np.zeros((length, 2), dtype=np.float64)
    xy[0,:] = np.array([x0,y0], dtype=np.float64)
    omega = np.zeros((length), dtype=np.float64)
    v = np.zeros((length, 2), dtype=np.float64)
    a = np.zeros((length, 2), dtype=np.float64)
    i=0
    for i in range(length-1):
        
        w = calculate_auv2_angular_acceleration(T, alpha, L, l, inertia) 
        omega[i+1] = omega[i] + w*dt
        print(theta[i] + omega[i+1]*dt)
        theta[i+1] = theta[i] + omega[i+1]*dt
        a[i+1] = calculate_auv2_acceleration(T, alpha, theta[i+1], mass)
        v[i + 1] = v[i] + a[i + 1] * dt
        xy[i+1] = xy[i] + v[i+1] * dt
        
    return np.arange(0, t_final+dt, dt), xy[:,0], xy[:,1], theta, v, omega, a


if __name__ == "__main__":
    calculate_auv2_acceleration(np.array([1.5, 3.5, 7.0, 6.0], ))
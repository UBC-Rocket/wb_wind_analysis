import numpy as np
import math
import csv
import environment as env
import helper

class Main():

    def __init__(self):
        self.helper=helper.Helper()
        self.env = env.Environment(self.helper)
        self.run_simulation()
        #print(self.helper.get("Vehicle Starting Mass"))

    def mass(self,time):
        m_i = self.helper.get("Vehicle Starting Mass")
        m_f = self.helper.get("Vehicle Final Mass")
        b_t = self.helper.get("Burn Time")
        
        return m_i - (m_f - m_i)/b_t * time
    
    def velocity(self,time):
        v_i = self.helper.get("Starting Velocity")
        v_f = self.helper.get("Final Velocity")
        b_t = self.helper.get("Burn Time")

        return v_i + (v_f - v_i)/b_t * time
    
    def run_simulation(self):
        dt = self.helper.get("Simulation Step Size")
        t_max = self.helper.get("End Time")
        A = self.helper.get("Vehicle Cross Sectional Area")

        results = [["Altitude (m)","Wind X (m/s)","Wind Y (m/s)","Vehicle X (m/s)","Vehicle Y (m/s)","Difference Magnitude (m/s)"]]

        #initial state
        t = self.helper.get("Start Time")
        h = self.helper.get("Starting Altitude")
        v_rocket_x = 0.0
        v_rocket_y = 0.0

        while(t <= t_max):
            t += dt
            dh = self.velocity(t) * dt
            h += dh

            rho = self.env.density(h)
            m = self.mass(t)

            wind_x, wind_y = self.env.wind(h)
            v_rocket_x += np.sign(wind_x)* 0.5 * A * rho / m * (wind_x - v_rocket_x)**2
            v_rocket_y += np.sign(wind_y)* 0.5 * A * rho / m * (wind_y - v_rocket_y)**2
            mag = math.sqrt((v_rocket_x-wind_x)**2 + (v_rocket_y-wind_y)**2)
            
            results.append([h,wind_x,wind_y,v_rocket_x,v_rocket_y,mag])
        
        self.helper.write_results(results)

Main()        
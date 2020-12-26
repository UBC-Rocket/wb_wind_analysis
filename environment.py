import tables as atm
import math
import numpy as np
from scipy import interpolate

class Environment():

    def __init__(self,helper):
        self.helper = helper
        self.build_wind_model()

    def density(self, altitude):
        altitude /= 1000
        (sigma, delta, theta) = atm.Atmosphere(altitude)
        rho = self.helper.get("Sea Level Density") * sigma
        return rho

    def wind(self, altitude):
        return float(self.wind_x(altitude)), float(self.wind_y(altitude))

    def build_wind_model(self):
        alt = self.helper.wind_alt
        x = self.helper.wind_x
        y = self.helper.wind_y
        self.wind_x = interpolate.interp1d(alt, x, fill_value = "extrapolate")
        self.wind_y = interpolate.interp1d(alt, y, fill_value = "extrapolate")

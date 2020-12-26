import csv
import os
import time

class Helper():

    def __init__(self):
        self.config = {}
        self.config_unit = {}
        self.wind_alt = []
        self.wind_y = []
        self.wind_x = []

        self.load_config()
        self.get_wind_data()

    
    def load_config(self):
        input_config={}
        input_config_unit={}
        with open("config/configs_to_use.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                for name in row:
                    with open("config/" + name.strip() + ".csv", 'r') as f:
                        reader = csv.reader(f)

                        for row in reader:
                            try:
                                input_config[row[0]] = float(row[1])
                                input_config_unit[row[0]] = str(row[2]).strip()
                            except ValueError:
                                input_config[row[0]] = str(row[1]).strip()
                                input_config_unit[row[0]] = ""
                            except IndexError:
                                input_config[row[0]] = float(row[1])
                                input_config_unit[row[0]] = ""

        self.config = dict(input_config)
        self.config_unit = dict(input_config_unit)

    def get_wind_data(self):
        with open("input/wind.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                self.wind_alt.append(float(row[0]))
                self.wind_x.append(float(row[1]))
                self.wind_y.append(float(row[2]))


    def get(self, key):
        return self.config[key]

    def write_results(self, results):
        t = int(time.time())
        with open("output/output" + str(t) + ".csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow([t])
            for key, value in self.config.items():
                writer.writerow([key, value, self.config_unit[key]])
            writer.writerows(results)

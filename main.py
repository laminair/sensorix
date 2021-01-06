import time

from barometric_pressure import Barometer
from battery_status import VoltMeter

from .utils import transform_to_nmea_sentence


class Sensorix(object):

    def __init__(self):
        self.battery = VoltMeter()
        self.baro = Barometer()

    def read_barometric_data(self):
        sp_measurement = self.baro.read_static_pressure()
        # dp_measurement = self.baro.read_dynamic_pressure()

        return sp_measurement

    def read_battery_data(self):
        # Default I2C address for the A/D converter is 0x48 (48)
        measurement = self.battery.generate_measurement_point()
        return measurement


if __name__ == "__main__":
    sens = Sensorix()
    while True:
        voltage = sens.battery.generate_measurement_point()
        baro_data = sens.baro.generate_barometric_output()

        output = transform_to_nmea_sentence(f"{baro_data}, {voltage}")
        print(output)
        time.sleep(.2)

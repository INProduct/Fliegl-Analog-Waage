from hx711 import HX711
from machine import Pin


class Waage:

    def __init__(self):
        self.hx711 = HX711(d_out=25, pd_sck=26)
        self.hx711.power_on()
        self.count_cells = 1
        self._zeropoint = 0
        self.tara_weight = 0
        self._cal_factor = 1
        self._cal_factor_res = 1

    def get_raw_weight(self):
        return self.hx711.read() // self.count_cells if self.hx711.is_ready() else None

    def get_unscaled_weight(self):
        return self.get_raw_weight() - self._zeropoint

    def get_scaled_weight(self):
        return self.get_unscaled_weight() * self._cal_factor_res

    def get_tared_weight(self):
        return self.get_scaled_weight() - self.tara_weight

    def get_tara(self):
        return self.tara_weight

    def set_tara(self):
        self.tara_weight = self.get_scaled_weight()

    def set_calibration(self, known_weight):
        self._cal_factor = self.get_unscaled_weight() / known_weight
        self._cal_factor_res = 1 / self._cal_factor

    def set_zeropoint(self):
        self._zeropoint = self.get_raw_weight()

    def set_count_cells(self, cells: int):
        if cells > 0:
            self.count_cells = cells

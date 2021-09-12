from hx711 import HX711
import json

config_file = '/etc/weight_config.json'

class Waage:

    def __init__(self):
        self.hx711 = HX711(d_out=25, pd_sck=26)
        self.hx711.power_on()
        self.count_cells = 1
        self._zeropoint = 0
        self.tara_weight = 0
        self._cal_factor = 1
        self._cal_factor_res = 1
        self.restore_data()

    def get_raw_weight(self):
        return self.hx711.read() // self.count_cells

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
        self.save_data()

    def set_calibration(self, known_weight):
        self._cal_factor = self.get_unscaled_weight() / known_weight
        self._cal_factor_res = 1 / self._cal_factor
        self.save_data()

    def set_zeropoint(self):
        self._zeropoint = self.get_raw_weight()
        self.save_data()

    def set_count_cells(self, cells: int):
        if cells > 0:
            self.count_cells = cells
            self.save_data()

    def save_data(self):
        weight_data = {
            'count_cells': self.count_cells,
            'zeropoint': self._zeropoint,
            'cal_factor': self._cal_factor,
            'cal_factor_res': self._cal_factor_res,
            'tara_weight': self.tara_weight,

        }
        js = json.dumps(weight_data)
        with open(config_file, 'w') as file:
            file.write(js)

    def restore_data(self):
        try:
            with open(config_file, 'r') as file:
                js = json.loads(file.read())
                self.count_cells = js['count_cells']
                self._zeropoint = js['zeropoint']
                self._cal_factor = js['cal_factor']
                self._cal_factor_res = js['cal_factor_res']
                self.tara_weight = js['tara_weight']
        except:
            # ToDo Logger.log
            return False


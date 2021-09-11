import machine
from machine import Pin
from waage import Waage
from logger import Logger
from stimer import STimer
from machine import Timer
import json


config_file = '/etc/app_config.json'

class App:

    def __init__(self):
        self.portion_weight = 0
        self.stop_by_weight = 0
        self.run = False
        self.out_pin = Pin(2, mode=Pin.OUT)
        self.out_pin.off()
        self.tim0 = machine.Timer(0)

        self.logger = Logger()
        self.rtc = STimer(False)
        self.waage = Waage()
        self._restore_data()

    def start(self):
        self.out_pin.on()
        self.run = True
        self.logger.log_info('Start', self.__class__, self.rtc.get_time())

    def stop(self):
        self.out_pin.off()
        self.run = False
        self.logger.log_info('Start', self.__class__, self.rtc.get_time())

    def start_one_portion(self):
        if self.waage.get_tared_weight() - self.portion_weight <= 0:
            self.logger.log_error('Kann nicht starten - zu wenig Gewicht', self.__class__, self.rtc.get_time())
            return False
        self.logger.log_info('Start One Portion with ' + str(self.waage.get_tared_weight()), self.__class__, self.rtc.get_time())
        self.stop_by_weight = self.waage.get_tared_weight() - self.portion_weight
        self.tim0.init(mode=Timer.PERIODIC, period=1000, callback=self._check_weight)
        self.start()

    def _check_weight(self, timer):
        print('check check')
        if self.waage.get_tared_weight() <= self.stop_by_weight:
            self.tim0.deinit()
            self.logger.log_info('Stopped by ' + str(self.waage.get_tared_weight()), self.__class__, self.rtc.get_time())
            self.stop()

    def set_portion(self, portion_weight: int):
        self.portion_weight = portion_weight
        self._save_data()

    def get_portion(self):
        return self.portion_weight

    def _save_data(self):
        js = {
            'portion': self.portion_weight,

        }
        js = json.dumps(js)
        with open(config_file, 'w') as file:
            file.write(js)

    def _restore_data(self):
        try:
            with open(config_file, 'r') as file:
                js = file.read()
                js = json.loads(js)
                self.portion_weight = js['portion']
        except:
            self.logger.log_error('Can\'t load app config file', self.__class__, self.rtc.get_time())

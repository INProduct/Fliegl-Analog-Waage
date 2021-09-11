from machine import Pin
from waage import Waage
from logger import Logger
from stimer import Timer

class App:

    def __init__(self):
        self.portion_weight = 0
        self.stop_by_weight = 0
        self.run = False
        self.out_pin = Pin(2, mode=Pin.OUT)
        self.out_pin.off()

        self.logger = Logger()
        self.rtc = Timer(False)

    def start(self):
        self.out_pin.on()
        self.run = True
        self.logger.log_info('Start', self.__class__, self.rtc.get_time())

    def stop(self):
        self.out_pin.off()
        self.run = False
        self.logger.log_info('Start', self.__class__, self.rtc.get_time())

    def start_one_portion(self):
        self.logger.log_info('Start One Portion', self.__class__, self.rtc.get_time())


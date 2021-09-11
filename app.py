from machine import Pin
from waage import Waage


class App:

    def __init__(self):
        self.portion_weight = 0
        self.stop_by_weight = 0
        self.run = False
        self.out_pin = Pin(2, mode=Pin.OUT)

    def start(self):
        self.out_pin.on()

    def start_one_portion(self):
        pass

    def stop(self):
        self.out_pin.off()

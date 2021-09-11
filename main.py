from waage import Waage
import utime

waage = Waage()

if __name__ == '__main__':
    while True:
        print(waage.read())
        utime.sleep_ms(2000)
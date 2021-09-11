from machine import RTC


class STimer:

    def __init__(self, is_on, period=60, offset=0):
        '''

        :param is_on: is the Timer on on Start
        :param period: minutes what is a period between runs - 1h, 2h etc
        :param offset: minutes when not to even hour - 12:15, 12: 30
        '''

        self.is_on = is_on
        self.period = period
        self.offset = offset
        self.rtc = RTC()
        self.next_time_to_start = None

    def get_status(self):
        return self.is_on

    def set_status(self, status: bool):
        self.is_on = status

    def get_period(self):
        return self.period

    def set_period(self, period: int):
        self.period = period

    def get_offset(self):
        return self.offset

    def set_offset(self, offset: int):
        self.offset = offset

    def get_time(self):
        return self.rtc.datetime()

    def set_time(self, datetime: str):
        self.rtc.datetime(datetime)
        self.next_time_to_start = self.rtc.datetime() # + period

    def set_next_time(self):
        year, month, day, hour, minute, second, msecond, usecond = self.rtc.datetime()



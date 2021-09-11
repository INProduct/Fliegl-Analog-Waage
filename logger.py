from enum import Enum
import os

class LogCategory(Enum):
    ERROR = 1
    WARNING = 2
    INFO = 3


class Logger:

    def __init__(self):
        self.path_to_log = '/var/log/logfile.log'

    def log_error(self, message, who, datetime):
        self._logg(LogCategory.ERROR, message, who, datetime)

    def log_warning(self, message, who, datetime):
        self._logg(LogCategory.ERROR, message, who, datetime)

    def log_info(self, message, who, datetime):
        self._logg(LogCategory.ERROR, message, who, datetime)

    def _logg(self, category: LogCategory, message, who, datetime):
        with os.open(self.path_to_log, 'a') as logfile:
            logfile.write('Hello')



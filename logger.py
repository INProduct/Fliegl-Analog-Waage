import json


class LogCategory:
    ERROR = 1
    WARNING = 2
    INFO = 3


path_to_log = '/var/logfile.log'


class Logger:

    @classmethod
    def log_error(cls, message, who, datetime):
        cls._logg(LogCategory.ERROR, message, who, datetime)

    @classmethod
    def log_warning(cls, message, who, datetime):
        cls._logg(LogCategory.ERROR, message, who, datetime)

    @classmethod
    def log_info(cls, message, who, datetime):
        cls._logg(LogCategory.ERROR, message, who, datetime)

    @classmethod
    def _logg(cls, category: LogCategory, message, who, datetime):
        with open(path_to_log, 'a') as logfile:
            logfile.write(str(category) + ',' + message + ',' + str(who) + ',' + str(datetime) + ';\n')



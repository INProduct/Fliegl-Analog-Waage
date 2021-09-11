import os

log_path = '/var/log'
config_path = '/etc'

# Create directories

if not log_path in os.listdir():
    os.mkdir(log_path)

if not config_path in os.listdir():
    os.mkdir(config_path)

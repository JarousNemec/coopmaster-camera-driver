import os

host = "127.0.0.1"
port = 9001
hello_message = "Hello from camera driver"

log_file_name = "camera_driver.log"

def get_log_directory():
    return "./logs/"

def get_log_filename():
    return log_file_name
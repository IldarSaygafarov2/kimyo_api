import multiprocessing

bind = "127.0.0.1:8008"
user = "root"
workers = multiprocessing.cpu_count() + 1
timeout = 120

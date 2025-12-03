import multiprocessing

bind = "127.0.0.1:8008"
user = "ildar"
workers = multiprocessing.cpu_count() + 1
timeout = 120

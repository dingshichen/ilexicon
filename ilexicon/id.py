from time import time
from random import randint


def generate_unique_id():
    timestamp = int(time() * 1000)  # 毫秒级时间戳
    random_part = randint(1000, 9999)  # 随机部分
    return int(f"{timestamp}{random_part}")
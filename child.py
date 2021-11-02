#11-901 Нурмухаметов Ринат Рафаэлевич
import os
import time
import argparse
import random
import sys
parser = argparse.ArgumentParser()
parser.add_argument('integer', type = int, help='an integer for the accumulator')
s = parser.parse_args().integer
print('«Запущена программа Child в процессе с PID ',os.getpid(),'с аргументом ', s,'»')
time.sleep(s)
print('«Завершился процесс с PID »', os.getpid(),'»')
sys.exit(random.randint(0,1));
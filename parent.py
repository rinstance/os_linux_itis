#11-901 Нурмухаметов Ринат Рафаэлевич
import os
import argparse
import random
parser = argparse.ArgumentParser()
parser.add_argument("--num_children", help="the number of children, from 1")
args = parser.parse_args()
n = int(args.num_children)
child = 1
for i in range(0, n):
        if child > 0:
                child = os.fork()
        if child == 0:
                argss = ['child',str(random.randint(5, 10))]
                os.execv('child',argss)
for i in range(0, n):
        ret = os.wait()
        print('«Дочерний процесс с PID {} завершился. Статус завершения {}.»'.format(ret[0],os.WEXITSTATUS(ret[1])))
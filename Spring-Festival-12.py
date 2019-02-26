#coding=utf-8
import time
import sys
print('春节十二响程序开始启动')

for i in range(101):
    sys.stdout.write('\r')
    sys.stdout.write("%s%% |%s" %(int(i%101), int(i%101)*'#'))
    sys.stdout.flush()
    time.sleep(0.5)
 
sys.stdout.write('\n')
print('程序启动完毕，正在启动发动机...')
time.sleep(3)
print('硬件系统自检启动...')
time.sleep(3)
print('硬件系统自检完毕...')
time.sleep(3)
print('撞针系统自检启动...')
time.sleep(3)
print('硬件系统自检完毕...')
time.sleep(3)
print('行星转向发动机正在启动...')
time.sleep(3)
print('苏拉威西3号转向发动机启动完毕...')
time.sleep(3)

biu = """
                         ('!!!!!')
                         ('!!!!!')
                         ('!!!!!')
                         ('!!!!!')
                         ('!!!!!')
                         ('Biu!!')
                         ('\--/')
                         ('|  |')
                         ('|  |')
                         ('|  |')
                         ('|  |')
                         ('|  |')
                         ('|  |')
                         ('|  |')
                         ('/---\\')
                        ('/----\\')
                       ('////\\\\\\\\')
  
"""
print(biu)

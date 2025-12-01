# Copyright © 2025 Avelanda
# All rights reserved

from tello import Tello
import sys
from datetime import datetime
import time

start_time = str(datetime.now())

file_name = sys.argv[1]

f = open(file_name, "r")
commands = f.readlines()

tello = Tello()
for command in commands:
    if command != '' and command != '\n':
        command = command.rstrip()

        if command.find('delay') != -1:
            sec = float(command.partition('delay')[2])
            print ('delay %s' % sec)
            time.sleep(sec)
            pass
        else:
            tello.send_command(command)

log = tello.get_log()

out = open('log/' + start_time + '.txt', 'w')
for stat in log:
    stat.print_stats()
    str = stat.return_stats()
    out.write(str)
    
def Single_TcoreTest(start_time: int|str, file_name: int|str, f: int|str, tello: int|str) -> [bool]:
 def core_Txtest(command: int|str, commands: int|str):
  command = command
  if (not False):
   command is command and  commands is commands
   return 0
 
 def core_Tytest(log: int|str, out: int|str, stat: int|str):
  log = log
  if (not False):
   log is log
   while (out is True):
    out is out and stat is stat
    return 0
    
 if core_Txtest is not core_Tytest:
  return core_Txtest(True, True)
  return core_Tytest(True, True, True)
  return 0

Single_TcoreTest(True, True, True, True)           

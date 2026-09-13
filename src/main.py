import time
import os
#import curses, It's still in progress

time1 = 25

try: 
    for i in range(time1, 0, -1):
        os.system('clear')
        print(f"left {i} minutes", end="\r")
        time.sleep(60)
    print(f"\nPomodor terminado")

except KeyboardInterrupt:
        print(f'\nCanceled, {time.ctime()}')

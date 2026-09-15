import time
import os
from rich.progress import track
#import curses, It's still in progress

time1 = 25
time2 = 50
time3 = 90

def main():

    try: 
        option = input("write pomo, deep or rhythm: ")
        
        if option == "pomo":
            for i in range(3, 0, -1):
                print(f" 25-minute countdown begin in {i} seconds", end="\r")
                time.sleep(1)
            for i in track(range(time1, 0, -1), description="Processing..."):
                os.system('clear')
                print(f"left {i} minutes", end="\r")
                time.sleep(60)
            print(f"\nPomodor terminado")
            
         
        elif option == "deep":
            for i in range(3, 0, -1):
                print(f" 50-minute countdown begin in {i} seconds", end="\r")
                time.sleep(1)
            for i in track(range(time2, 0, -1), description="Processing..."):
                os.system('clear')
                print(f"left {i} minutes", end="\r")
                time.sleep(60)
            print(f"\nPomodor terminado")

        elif option == "rhythm":
            for i in range(3, 0, -1):
                print(f" 90--minute countdown begin in {i} seconds", end="\r")
                time.sleep(1)
            for i in track(range(time3, 0, -1), description="Processing..."):
                os.system('clear')
                print(f"left {i} minutes", end="\r")
                time.sleep(60)
            print(f"\nPomodor terminado")

        else:
           print("try again")
 

    except KeyboardInterrupt:
        print(f'\nCanceled, {time.ctime()}')

if __name__ == "__main__":
   main()


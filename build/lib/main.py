import os
import subprocess
import time
from rich.progress import track
# import curses, It's still in progress

time1 = 25
time2 = 50
time3 = 90

def main():

    try:
        option = input("write pomo, deep ,rhythm or countdown: ")

        if option == "pomo":
            for i in range(3, 0, -1):
                print(f" 25-minute countdown begin in {i} seconds", end="\r")
                time.sleep(1)
            
            for pomo in range(int(input("\nEnter pomos' number: "))):

                for e in track(range(time1, 0, -1), description="Processing..."):
                    os.system("clear")
                    print(f"{e} minutes left", end="\r")
                    time.sleep(60)
                print("\nFinished")

                for noti in range(10):
                    time.sleep(0.1)
                    print("\a" , end="\r")

                for a in track(range(5, 0, -1), description="break..."):
                    os.system("clear")
                    print(f"{a} minutes left", end="\r")
                    time.sleep(60)
                print("\nFinished")

                for noti in range(10):
                    time.sleep(0.1)
                    print("\a" , end="\r")

            def notification(title, message):
                subprocess.run(["notify-send", title, message], check=True)
            notification("Blootimer", "Your pomos have finished executing")


        elif option == "deep":
            for i in range(3, 0, -1):
                print(f" 50-10 minute countdown begin in {i} seconds", end="\r")
                time.sleep(1)

            for deep in range(int(input("\nEnter deeps' number: "))):
                for e in track(range(time2, 0, -1), description="Processing..."):
                    os.system("clear")
                    print(f"left {e} minutes", end="\r")
                    time.sleep(60)
                print("\nfinished")

                for noti in range(10):
                    time.sleep(0.1)
                    print("\a" , end="\r")

                for a in track(range(10, 0, -1), description="break"):
                    os.system("clear")
                    print(f"left {a} minutes", end="\r")
                    time.sleep(60)
                print("\nfinished")

                for noti in range(10):
                    time.sleep(0.1)
                    print("\a" , end="\r")

            def notification(title, message):
                subprocess.run(["notify-send", title, message], check=True)
            notification("Blootimer", "Your deeps have finished executing")


  
        elif option == "rhythm":
            for i in range(3, 0, -1):
                print(f" 90-20 minute countdown begin in {i} seconds", end="\r")
                time.sleep(1)

            for rhythm in range(int(input("\nEnter rhythms' number: "))):
                for e in track(range(time3, 0, -1), description="Processing..."):
                    os.system("clear")
                    print(f"left {e} minutes", end="\r")
                    time.sleep(60)
                print("\nfinished")

                for noti in range(10):
                    time.sleep(0.1)
                    print("\a" , end="\r")
 
                for a in track(range(20, 0, -1), description="Break"):
                    os.system("clear")
                    print(f" {a} minute rest ", end="\r")
                    time.sleep(60)

                for noti in range(10):
                    time.sleep(0.1)
                    print("\a" , end="\r")

                    
            def notification(title, message):
                subprocess.run(["notify-send", title, message], check=True)
            notification("Blootimer", "Your rhythm have finished executing")


        elif option == "countdown":
            for i in range(3, 0, -1):
                print(f"  countdown begin in {i} seconds", end="\r")
                time.sleep(1)

            x =  int(input("Enter a number of minutes to the countdown: "))
            for rhythm in range(int(input("\nEnter countdowns' number: "))):
            
                for e in track(range(x, 0, -1), description="Processing..."):
                    os.system("clear")
                    print(f"left {e} minutes", end="\r")
                    time.sleep(60)
                print("\nfinished")

                for noti in range(10):
                    time.sleep(0.1)
                    print("\a" , end="\r",)

            def notification(title, message):
                subprocess.run(["notify-send", title, message], check=True)
            notification("Blootimer", "Your countdown has finished executing")


        else:
            print("try again")

    except KeyboardInterrupt:
        print(f"\nCanceled, {time.ctime()}")


if __name__ == "__main__":
    main()

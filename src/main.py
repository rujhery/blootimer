import os
import time
from rich.progress import track
# import curses, It's still in progress

time1 = 25
time2 = 50
time3 = 90


def main():

    try:
        option = input("write pomo, deep or rhythm: ")

        if option == "pomo":
            # for i in range(3, 0, -1):
            #     print(f" 25-minute countdown begin in {i} seconds", end="\r")
            #     time.sleep(1)

            for e in track(range(time1, 0, -1), description="Processing..."):
                os.system("clear")
                print(f"{e} minutes left", end="\r")
                time.sleep(60)
            print("\nFinished")

            for a in track(range(5, 0, -1), description="break..."):
                os.system("clear")
                print(f"{a} minutes left", end="\r")
                time.sleep(60)
            print("\nFinished")

        elif option == "deep":
            for i in range(3, 0, -1):
                print(f" 50-10 minute countdown begin in {i} seconds", end="\r")
                time.sleep(1)

            for e in track(range(time2, 0, -1), description="Processing..."):
                os.system("clear")
                print(f"left {e} minutes", end="\r")
                time.sleep(60)
            print("\nfinished")

            for a in track(range(10, 0, -1), description="break"):
                os.system("clear")
                print(f"left {a} minutes", end="\r")
                time.sleep(60)
            print("\nfinished")

        elif option == "rhythm":
            for i in range(3, 0, -1):
                print(f" 90-20 minute countdown begin in {i} seconds", end="\r")
                time.sleep(1)

            for e in track(range(time3, 0, -1), description="Processing..."):
                os.system("clear")
                print(f"left {e} minutes", end="\r")
                time.sleep(60)
            print("\nfinished")

            for a in track(range(20, 0, -1), description="Break"):
                os.system("clear")
                print(f" {a} minute rest ", end="\r")
                time.sleep(60)
        else:
            print("try again")

    except KeyboardInterrupt:
        print(f"\nCanceled, {time.ctime()}")


if __name__ == "__main__":
    main()

import time

def countDown():
    minutes = int(input("Enter the number of minutes to count down: "))
    seconds = int(input("Enter the number of seconds to count down: "))

    print(f"Counting down from {minutes} minutes and {seconds} seconds...\n")

    total_seconds = minutes * 60 + seconds  
    for remaining_seconds in range(total_seconds, -1, -1):
        minute = remaining_seconds // 60 
        second = remaining_seconds % 60  
        print(f"{minute:02}:{second:02}", end='\r')  
        time.sleep(1)

    print("\nCountdown finished!")

if __name__ == "__main__":
    countDown()

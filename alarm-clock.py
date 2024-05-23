import datetime
import time
from playsound import playsound

def get_alarm_time():
    while True:
        alarm_time = input("Enter the alarm time (HH:MM:SS): ")
        try:
            alarm_hour, alarm_minute, alarm_second = map(int, alarm_time.split(':'))
            return datetime.time(alarm_hour, alarm_minute, alarm_second)
        except ValueError:
            print("Invalid time format. Please try again.")

def alarm_clock(alarm_time):
    print(f"Alarm set for {alarm_time}")

    while True:
        # Get the current time
        now = datetime.datetime.now().time()

        # Check if current time matches the alarm time
        if now.hour == alarm_time.hour and now.minute == alarm_time.minute and now.second == alarm_time.second:
            print("Time to wake up!")
            playsound('alarm_sound.mp3')  # Make sure you have an alarm sound file named 'alarm_sound.mp3'
            break

        # Sleep 
        time.sleep(1)

if __name__ == "__main__":
    alarm_time = get_alarm_time()
    alarm_clock(alarm_time)
import datetime
import time
from playsound import playsound

def get_alarm_times():
    alarm_times = []
    while True:
        alarm_time = input("Enter the alarm time (HH:MM:SS) or 'done' to finish: ")
        if alarm_time.lower() == 'done':
            break
        try:
            alarm_hour, alarm_minute, alarm_second = map(int, alarm_time.split(':'))
            alarm_times.append(datetime.time(alarm_hour, alarm_minute, alarm_second))
        except ValueError:
            print("Invalid time format. Please try again.")
    return alarm_times

def alarm_clock(alarm_times):
    print(f"Alarms set for: {', '.join(map(str, alarm_times))}")

    while True:
        # Get the current time
        now = datetime.datetime.now().time()

        # Check if current time matches any alarm time
        for alarm_time in alarm_times:
            if now.hour == alarm_time.hour and now.minute == alarm_time.minute and now.second == alarm_time.second:
                print(f"Alarm for {alarm_time} - Time to wake up!")
                playsound('alarm_sound.mp3')  # Make sure you have an alarm sound file named 'alarm_sound.mp3'
                alarm_times.remove(alarm_time)
                break

        # Sleep
        time.sleep(1)

if __name__ == "__main__":
    alarm_times = get_alarm_times()
    alarm_clock(alarm_times)
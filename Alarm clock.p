import datetime
import time

def set_alarm(hour, minute):
    while True:
        now = datetime.datetime.now()
        if now.hour == hour and now.minute == minute:
            print("Wake up!")
            break
        time.sleep(60)  # Check every minute

def snooze(minutes):
    time.sleep(minutes * 60)
    print("Time to wake up again!")

# Set an alarm for 7:30 AM
set_alarm(7, 30)

# Snooze for 5 minutes
snooze(5)

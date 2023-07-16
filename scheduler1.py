import schedule
import time
import os.path

def CheckCPU():
    status = 'good'
    print("CPU status is "+status)


def CheckCalendar():
    print("You currently have nothing to do today")


def WeekendTime():
    print("The weekend has started.")

def scheduler():
    schedule.every(1).seconds.do(CheckCPU)
    schedule.every(1).seconds.do(CheckCalendar)
    schedule.every(1).seconds.do(WeekendTime)

    while True:
        schedule.run_pending()
        time.sleep(1)

scheduler()
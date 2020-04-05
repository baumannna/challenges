from datetime import datetime
from datetime import timedelta
import winsound

set_timer = int(input('How long do you want to stay focused? (Minutes) '))


def pomodoro (timer):
    start = datetime.today()
    end = start + timedelta(seconds=timer*60)

    print('Timer started at:', start, "and was set to", timer, 'Minute(s).')

    count = 0

    while True:
        now = datetime.now()
        if now <= end:
            continue
        elif now >= end:
            count = count + 1
            i = 0
            print('Alarm!')
            winsound.Beep(4000, 100)
            print('Timer stopped at', datetime.now())
            print('Great! You have done', count, 'iteration(s) of', set_timer, 'Minute(s).')
            again = input('Do another one? (yes = y, no = n) ')
            if again == 'y':
                print("New iteration started at", datetime.now())
                end = datetime.now() + timedelta(seconds=timer * 60)
                continue
            elif again == 'n':
                break
            else:
                print('Please enter only y for yes or n for n.')
                break


pomodoro(set_timer)


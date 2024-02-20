
"""
https://stackoverflow.com/questions/12435211/threading-timer-repeat-function-every-n-seconds
"""
import threading
from datetime import datetime

class SomeClassThatNeedsATimer:
    def __init__(self):
        self.timer = threading.Timer(5.0, self.on_timer)
        self.timer.start()

    def on_timer(self):
        #print('On timer')
        print(datetime.now().strftime('%Y-%m-%d_%H:%M:%S') + ' On timer')
        print('hello world again.')
        self.timer.run()


def main():
    print('hello world.')
    a = SomeClassThatNeedsATimer()
    print('hello end of the world.')

if __name__ == '__main__':
    main()
# How to schedule tasks in python
import schedule # do pip install schedule when connected to internet
import time 
def example():
    print('Hey you will be successful one day')

schedule.every(7).seconds.do(example)

while True:
    schedule.run_pending()
    time.sleep(1)
    
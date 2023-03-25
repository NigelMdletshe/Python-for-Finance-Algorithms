#How to get Epoch Time in pyhton
#Fancy wat to get time upto seconds

from datetime import datetime
import time

now = datetime.now()
epochtime = int(time.time())
print(epochtime)

new_epochtime = epochtime + (30*60)
print(new_epochtime)
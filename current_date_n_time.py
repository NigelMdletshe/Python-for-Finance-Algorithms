# Time in Python
from datetime import datetime
import time

now = datetime.now()
print('------------------------')
print(now)

#month and day
month_date = now.strftime("%m/ %d")
print('------------------------')
print(month_date)

# hour and minute
hour_min = now.strftime("%H:%M")
print('------------------------')
print(hour_min)

# Day string
dstring = now.strftime("%d/%m/%Y  %H:%M:%S")
print('------------------------')
print(dstring)

#epochtime outputs seconds
epoch = float(time.time())
print('------------------------')
print(epoch)

e2 = epoch + 2500
print('------------------------')
print(f'epoch:{epoch} e2: {e2}')

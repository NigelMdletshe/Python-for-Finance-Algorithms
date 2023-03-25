#Time in python

import time
from datetime import datetime
import nice_funcs as n
n.space()
now = datetime.now()
n.space()
Value = 100000000.34
dollar_value = "${:,}".format(Value)
print(dollar_value)






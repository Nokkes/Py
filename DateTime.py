from __future__ import print_function # Print function compatibility with 2.x
from datetime import datetime

now = datetime.now()

print('%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second))
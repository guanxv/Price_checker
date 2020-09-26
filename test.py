import re

'''

from datetime import datetime

date_str = "Jul 2020"

date_obj = datetime.strptime(date_str, '%b %Y' )

timedelta = (datetime.now() - date_obj)



numDay = timedelta.days

print(numDay)'''

import re


a = '\n        110kW @ 6000rpm\n'

pattern =re.compile(r'([0-9]{2,3})kW')

power = int(pattern.search(a).group(1))

b = "\n        380Nm @ 1800-5100rpm\n"    

engTorquePattern =re.compile(r'([0-9]{3})Nm')

torque = engTorquePattern.search(b).group(1)

print(torque)


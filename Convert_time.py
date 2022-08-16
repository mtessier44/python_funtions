import datetime
import dateutil.parser as parser

text = '1/2/2021 00:00'
#date = parser.parse(text)
date = parser.parse(text, dayfirst=True)

#Addition of one day
date += datetime.timedelta(days=1)
print(date.isoformat())
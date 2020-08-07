from datetime import datetime
import calendar
print(datetime.today().month)
print(calendar.monthrange(datetime.today().year, datetime.today().month)[1])
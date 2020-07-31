from datetime import datetime
import calendar
print(calendar.monthrange(datetime.today().year, datetime.today().month)[1])
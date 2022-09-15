import datetime
import calendar
import pytz

class PyCronos:
    def __init__(self):
        self.value = None
        self.timestamp = None

    def create(self, year, month=None, day=None, hour=0, minute=0, second=0, microsecond=0, tzinfo=None):
        ''' Construct a datetime object '''
        self.value = datetime.datetime(
            year=year,
            month=month,
            day=day,
            hour=hour,
            minute=minute,
            second=second,
            microsecond=microsecond,
            tzinfo=pytz.timezone(tzinfo) if tzinfo != None else tzinfo
        )

        self.timestamp = datetime.datetime.timestamp(self.value)

        return self

    def format(self, format=None):
        ''' Format a datetime from datetime.strftime(); optional format info; default iso format'''
        self.value = self.value.strftime(format) if format != None else self.value.isoformat()
        return self

    def parse(self, date_to_parse, format, tz=None):
        ''' Construct a datetime using a datetime string '''
        self.value = datetime.datetime.strptime(date_to_parse, format).astimezone(tz=None if tz == None else pytz.timezone(tz))

        self.timestamp = datetime.datetime.timestamp(self.value)

        return self

    def now(self, tz=None):
        ''' Construct a now datetime from datetime.now(); optional timezone info'''
        self.value = datetime.datetime.now(tz=None if tz == None else pytz.timezone(tz))

        self.timestamp = datetime.datetime.timestamp(self.value)

        return self

    def add(self, num, type):
        ''' Construct a new datetime adding a number in a attribute (type)'''
        match type:
            case 'day':
                self.value = self.value.replace(day=self.value.day + num)
            case 'month':
                self.value = self.value.replace(month=self.value.month + num)
            case 'year':
                self.value = self.value.replace(year=self.value.year + num)
            case 'hour':
                self.value = self.value.replace(hour=self.value.hour + num)
            case 'minute':
                self.value = self.value.replace(minute=self.value.minute + num)
            case 'second':
                self.value = self.value.replace(second=self.value.second + num)
            case 'microsecond':
                self.value = self.value.replace(microsecond=self.value.microsecond + num)

        self.timestamp = datetime.datetime.timestamp(self.value)

        return self

    def set(self, type, num):
        ''' Construct a new datetime changing a attribute (type)'''
        match type:
            case 'day':
                self.value = self.value.replace(day=num)
            case 'month':
                self.value = self.value.replace(month=num)
            case 'year':
                self.value = self.value.replace(year=num)
            case 'hour':
                self.value = self.value.replace(hour=num)
            case 'minute':
                self.value = self.value.replace(minute=num)
            case 'second':
                self.value = self.value.replace(second=num)
            case 'microsecond':
                self.value = self.value.replace(microsecond=num)

        self.timestamp = datetime.datetime.timestamp(self.value)

        return self
    
    def get(self, type):
        ''' Return a datetime attribute '''
        return getattr(self.value, type) 

    def setTimestamp(self, timestamp):
        ''' Contruct a new datetime from a timestamp '''
        self.timestamp = timestamp
        self.value = datetime.datetime.fromtimestamp(self.timestamp)

        return self

    def lastDayOfWeek(self):
        ''' Return last day of week datetime from PyCronos value '''

        day_of_week = self.value

        if day_of_week.strftime('%A') == 'Saturday':
            return self.value
        else:
            day_of_week = day_of_week + datetime.timedelta(days=1)

            while day_of_week.strftime('%A') != 'Saturday':
                day_of_week = day_of_week + datetime.timedelta(days=1)

            return day_of_week

    def firstDayOfWeek(self):
        ''' Return first day of week datetime from PyCronos value '''

        day_of_week = self.value

        if day_of_week.strftime('%A') == 'Sunday':
            return self.value
        else:
            day_of_week = day_of_week - datetime.timedelta(days=1)

            while day_of_week.strftime('%A') != 'Sunday':
                day_of_week = day_of_week - datetime.timedelta(days=1)

            return day_of_week

    def endOfMonth(self):
        ''' Return end of month datetime'''
        endOfMonth = self.value
        return endOfMonth.replace(day=calendar.monthrange(endOfMonth.year, endOfMonth.month)[1], hour=23, minute=59, second=59, microsecond=999999)
import datetime
import pytz

class PyCronos:
    def __init__(self):
        self.value = None

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

        return self

    def format(self, format=None):
        ''' Format a datetime from datetime.strftime(); optional format info; default iso format'''
        self.value = self.value.strftime(format) if format != None else self.value.isoformat()
        return self

    def parse(self, date_to_parse, format, tz=None):
        ''' Construct a datetime using a datetime string '''
        self.value = datetime.datetime.strptime(date_to_parse, format).astimezone(tz=None if tz == None else pytz.timezone(tz))
        return self

    def now(self, tz=None):
        ''' Construct a now datetime from datetime.now(); optional timezone info'''
        self.value = datetime.datetime.now(tz=None if tz == None else pytz.timezone(tz))
        return self

    def add(self, num, type):
        match type:
            case 'day':
                self.value = self.value.replace(day=self.value.day + num)
            case 'month':
                self.value = self.value.replace(month=self.value.month + num)
            case 'year':
                self.value = self.value.replace(year=self.value.year + num)
            case 'hour':
                self.value = self.value.replace(hour=self.value.year + num)
            case 'minute':
                self.value = self.value.replace(minute=self.value.year + num)
            case 'second':
                self.value = self.value.replace(second=self.value.year + num)
            case 'microsecond':
                self.value = self.value.replace(microsecond=self.value.year + num)

        return self
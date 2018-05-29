#   class to store a starting date, starting time, end date and end time for specific events
#   for easy comparison the 'start' and 'end' attributes give an integer presentation of the
#   start and end datetimes respectively

import datetime


class Interval:
    def __init__(self, startDate: str, startTime: str, endDate: str, endTime: str):

        if startDate == '':
            splitDate = ['0000', '00', '00']
        else:
            #   separate year, month and day
            splitDate = startDate.split('-')

        if startTime == '':
            splitTime = ['00', '00', '00']
        else:
            #   separate hours, minutes and seconds
            splitTime = startTime.split(':')

        #   create an integer with the following format: yyyymmddHHMMSS
        self.start = int(splitDate[2] + splitDate[1] + splitDate[0] + splitTime[0] + splitTime[1] + splitTime[2])

        #   repeat above process for 'end' variable
        if endDate == '':
            splitDate = ['0000', '00', '00']
        else:
            #   separate year, month and day
            splitDate = endDate.split('-')

        if endTime == '':
            splitTime = ['00', '00', '00']
        else:
            #   separate hours, minutes and seconds
            splitTime = endTime.split(':')

        self.end = int(splitDate[2] + splitDate[1] + splitDate[0] + splitTime[0] + splitTime[1] + splitTime[2])

        self.startDate = startDate
        self.endDate = endDate
        self.startTime = startTime
        self.endTime = endTime

    @classmethod
    def hourly(cls, date: str, hour: str):
        #   load the supplied date and hourly period into a datetime object
        #   in the KNMI dataset, if the hourly period is set to 2 it means
        #   from 01:00:00 to 02:00:00
        #   therefore hour-1 is loaded into the datetime object to get the
        #   startDateTime
        startDateTime = datetime.datetime(int(date[:4]), int(date[4:6]), int(date[-2:]), int(hour) - 1, 0, 0)

        #   the function strftime simply formats the information in the
        #   datetime object to a specific layout in this case e.g.
        #   yyyy-mm-dd for a date and HH:MM:SS for time
        startDate = startDateTime.strftime("%y-%m-%d")
        startTime = startDateTime.strftime("%H:%M:%S")

        #   datetime object to a specific layout in this case e.g.
        #   yyyy-mm-dd for a date and HH:MM:SS for time
        startDateTime += datetime.timedelta(hours=1)

        endDate = startDateTime.strftime("%y-%m-%d")
        endTime = startDateTime.strftime("%H:%M:%S")

        #   pass the created variables to the constructor
        return cls(startDate, startTime, endDate, endTime)

    def __str__(self):
        return str(self.startDate) + ', ' + str(self.startTime) + ', ' + str(self.endDate) + ', ' + str(self.endTime)

    def format(self) -> str:
        return 'startDate, ' + str(self.startDate) + ', startTime, ' + str(self.startTime) + ', endDate, ' + str(
            self.endDate) + ', endTime, ' + str(self.endTime)

    def overlap(self, other):
        if other.start <= self.start < other.end:
            print("'vo")
        return other.start <= self.start < other.end

    def outer_interval(self, other):
        minstart = min(self.start, other.start)
        maxend = max(self.end, other.end)
        if self.start == minstart and self.end == maxend:
            return self
        elif other.start == minstart and other.end == maxend:
            return other
        elif self.start == minstart and other.end == maxend:
            return Interval(self.startDate, self.startTime, other.endDate, other.endTime)
        elif other.start == minstart and self.end == maxend:
            return Interval(other.startDate, other.startTime, self.endDate, self.endTime)

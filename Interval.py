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
        startDateTime = datetime.datetime(int(date[:4]), int(date[4:6]), int(date[-2:]), int(hour) - 1, 0, 0)

        startDate = startDateTime.strftime("%y-%m-%d")
        startTime = startDateTime.strftime("%H:%M:%S")

        startDateTime += datetime.timedelta(hours=1)

        endDate = startDateTime.strftime("%y-%m-%d")
        endTime = startDateTime.strftime("%H:%M:%S")

        return cls(startDate, startTime, endDate, endTime)

    def __str__(self):
        return '(' + str(self.startDate) + ' ' + str(self.startTime) + ', ' + str(self.endDate) + ' ' + str(
            self.endTime) + ')'

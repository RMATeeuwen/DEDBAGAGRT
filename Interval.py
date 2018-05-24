#   class to store a starting date, starting time, end date and end time for specific events
#   if needed an integer representation of date and time can be added for easy comparison
class Interval:
    def __init__(self, startDate, startTime, endDate, endTime):
        self.startDate = startDate
        self.endDate = endDate
        self.startTime = startTime
        self.endTime = endTime

    def __str__(self):
        return '(' + str(self.startDate) + ' ' + str(self.startTime) + ', ' + str(self.endDate) + ' ' + str(
            self.endTime) + ')'

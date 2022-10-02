class Dates:
    def __init__(self, date):
        self.date = date
        
    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")


dates = Dates('22-12-2022')
datewithme = '22/12/2022'
dame = Dates.toDashDate(datewithme)
if dates.getDate() == dame:
    print('equal')
else:
    print('not equal') 
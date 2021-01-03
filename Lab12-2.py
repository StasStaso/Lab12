class TTime:
    def __init__(self, time):
        self.__hours = int(time[0:2])
        self.__minutes = int(time[3::])

    def add_hours(self, hours):
        self.__hours += hours
        if self.__hours > 23:
            self.__hours = self.__hours % 24

    def add_minutes(self, minutes):
        self.__minutes += minutes
        if self.__minutes > 59:
            self.__hours+=self.__minutes//60
            self.__minutes = self.__minutes%60
        if self.__hours > 23:
            self.__hours = self.__hours // 24

    def ToString(self):
        return f"{int(self.__hours)}:{int(self.__minutes)}"

d = TTime("21:17")
print(d.ToString())
d.add_hours(3)
print(d.ToString())
d.add_minutes(70)
print(d.ToString())




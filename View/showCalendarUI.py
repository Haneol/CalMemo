# -*- coding: euc-kr -*-
class ShowCalendarUI:
    def __init__(self, showCalendar):
        self.__showCalendar = showCalendar

    def showCal(self, date):
        year = date[:4]
        month = date[4:6]

        print("\n--------[달력 보기]--------")
        print(f">> {year}년 {month}월")
        print(self.__showCalendar.showCal(date))
        print("---------------------------")
        print("0. 뒤로가기")
        print("1. 재입력 후 달력 보기")
        print("2. 이전 달 달력 보기")
        print("3. 다음 달 달력 보기")

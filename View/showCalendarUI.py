# -*- coding: euc-kr -*-
class ShowCalendarUI:
    def __init__(self, showCalendar):
        self.__showCalendar = showCalendar

    def showCal(self, date):
        year = date[:4]
        month = date[4:6]

        print("\n--------[�޷� ����]--------")
        print(f">> {year}�� {month}��")
        print(self.__showCalendar.showCal(date))
        print("---------------------------")
        print("0. �ڷΰ���")
        print("1. ���Է� �� �޷� ����")
        print("2. ���� �� �޷� ����")
        print("3. ���� �� �޷� ����")

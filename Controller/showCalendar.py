# -*- coding: euc-kr -*-

import utils
from View.showCalendarUI import ShowCalendarUI as UI
from Model.memoList import MemoList as Model


class ShowCalendar:
    def __init__(self):
        self.__showCalendarUI: UI = UI(self)

    def showCal(self, date):
        day = utils.dateToDay(date)
        lastDate = utils.lastDate(date)
        
        memo = Model()
        memoByMonth = memo.getMemoByMonth(date)
        memoByMonth.sort()

        calander = "일\t월\t화\t수\t목\t금\t토\n"

        dd = 1
        j = 0
        for i in range(42):
            if i < day:
                calander = calander + "\t"
            else:
                if j < len(memoByMonth) and int(memoByMonth[j][6:8]) == dd:
                    calander = calander + f"{dd}*\t"
                    j += 1
                else:
                    calander = calander + f"{dd}\t"
            
                if (i+1) % 7 == 0:
                    calander = calander + "\n"
                
                dd += 1
                if dd > lastDate:
                    break
            
        return calander

    def getUI(self) -> UI:
        return self.__showCalendarUI

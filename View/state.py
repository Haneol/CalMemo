# -*- coding: euc-kr -*-

from enum import Enum
import utils
from Model.memoList import MemoList as Model
from Controller.showCalendar import ShowCalendar
from Controller.loadMemo import LoadMemo
from Controller.saveMemo import SaveMemo
from Controller.deleteMemo import DeleteMemo
from Controller.resetMemo import ResetMemo


class State(Enum):
    INIT = 0
    CALENDAR = 1
    LOAD = 2
    SAVE = 3
    DELETE = 4
    RESET = 5
    R_QUIT = 6
    QUIT = 7


class Event(Enum):
    MENU_CALENDAR = 1
    RE_ACTION = 1
    MENU_LOAD = 2
    MENU_SAVE = 3
    MENU_DELETE = 4
    MENU_RESET = 5
    MENU_QUIT = 6
    BACK = 0
    PREV_MON = 2
    NEXT_MON = 3
    CONFIRM = 9


class EventActionTable:
    def __init__(self, curState, event, nextState, action):
        self.curState = curState
        self.event = event
        self.nextState = nextState
        self.action = action

    def run_action(self):
        if self.action is not None:
            self.action()


class StateMachine:
    __curDate: str

    def __init__(self):
        self.__curState = State.INIT
        self.__eventActionTable = [
            EventActionTable(
                State.INIT, Event.MENU_QUIT, State.R_QUIT, self.quitAction
            ),
            EventActionTable(State.R_QUIT, Event.BACK, State.INIT, self.initAction),
            EventActionTable(
                State.R_QUIT, Event.CONFIRM, State.QUIT, self.qquitAction
            ),
            EventActionTable(
                State.INIT, Event.MENU_CALENDAR, State.CALENDAR, self.calendarAction
            ),
            EventActionTable(State.CALENDAR, Event.BACK, State.INIT, self.initAction),
            EventActionTable(
                State.CALENDAR, Event.MENU_CALENDAR, State.CALENDAR, self.calendarAction
            ),
            EventActionTable(
                State.CALENDAR,
                Event.PREV_MON,
                State.CALENDAR,
                self.calendarActionPrev,
            ),
            EventActionTable(
                State.CALENDAR,
                Event.NEXT_MON,
                State.CALENDAR,
                self.calendarActionNext,
            ),
            EventActionTable(
                State.INIT,
                Event.MENU_LOAD,
                State.LOAD,
                self.loadAction,
            ),
            EventActionTable(
                State.LOAD,
                Event.RE_ACTION,
                State.LOAD,
                self.loadAction,
            ),
            EventActionTable(
                State.LOAD,
                Event.BACK,
                State.INIT,
                self.initAction,
            ),
            EventActionTable(
                State.INIT,
                Event.MENU_SAVE,
                State.SAVE,
                self.saveAction,
            ),
            EventActionTable(
                State.SAVE,
                Event.RE_ACTION,
                State.SAVE,
                self.saveAction,
            ),
            EventActionTable(
                State.SAVE,
                Event.BACK,
                State.INIT,
                self.initAction,
            ),
            EventActionTable(
                State.INIT,
                Event.MENU_DELETE,
                State.DELETE,
                self.deleteAction,
            ),
            EventActionTable(
                State.DELETE,
                Event.RE_ACTION,
                State.DELETE,
                self.deleteAction,
            ),
            EventActionTable(
                State.DELETE,
                Event.BACK,
                State.INIT,
                self.initAction,
            ),
            EventActionTable(
                State.INIT,
                Event.MENU_RESET,
                State.RESET,
                self.resetAction,
            ),
            EventActionTable(
                State.RESET,
                Event.BACK,
                State.INIT,
                self.initAction,
            ),
        ]

        self.initAction()

    def run(self):
        while self.__curState != State.QUIT:
            curEvent = self.getNextEvent()

            for table in self.__eventActionTable:
                if self.__curState == table.curState and curEvent == table.event.value:
                    table.run_action()
                    self.__curState = table.nextState
                    break

    def getNextEvent(self):
        event = input()

        if event.isdigit():
            event = int(event)
        else:
            event = 10

        return event

    # Action
    def initAction(self):
        print("\n--------[전체 메뉴]--------")
        print("메뉴 번호를 입력하세요.")
        print("1. 달력보기")
        print("2. 메모 읽기")
        print("3. 메모 저장")
        print("4. 메모 삭제")
        print("5. 메모 초기화")
        print("6. 프로그램 종료")

    def calendarAction(self):
        con = ShowCalendar()
        ui = con.getUI()

        self.__curDate = utils.inputMonth() # 20230601
        ui.showCal(self.__curDate)

    def calendarActionPrev(self):
        con = ShowCalendar()
        ui = con.getUI()

        year = self.__curDate[:4]
        month = self.__curDate[4:6]

        if int(month) == 1:
            year = str(int(year) - 1)
            month = "12"
        else:
            month = str(int(month) - 1)

        self.__curDate = year + ("0" + month if len(month) == 1 else month) + "01"

        ui.showCal(self.__curDate)

    def calendarActionNext(self):
        con = ShowCalendar()
        ui = con.getUI()

        year = self.__curDate[:4]
        month = self.__curDate[4:6]

        if int(month) == 12:
            year = str(int(year) + 1)
            month = "1"
        else:
            month = str(int(month) + 1)

        self.__curDate = year + ("0" + month if len(month) == 1 else month) + "01"

        ui.showCal(self.__curDate)

    def loadAction(self):
        con = LoadMemo()
        ui = con.getUI()
      
        ui.loadMemo(utils.inputDate())

    def saveAction(self):
        con = SaveMemo()
        ui = con.getUI()

        ui.saveMemo(utils.inputDate())

    def deleteAction(self):
        con = DeleteMemo()
        ui = con.getUI()

        ui.deleteMemo(utils.inputDate())

    def resetAction(self):
        con = ResetMemo()
        ui = con.getUI()

        ui.resetMemo()

    def quitAction(self):
        print("\n--------[종료 확인]--------")
        print("프로그램을 종료하시겠습니까?")
        print("0. 취소")
        print("9. 프로그램 종료")

    def qquitAction(self):
        memo = Model()
        memo.saveMemo()
        print("\n------[프로그램 종료]------")
        print("프로그램을 종료합니다")

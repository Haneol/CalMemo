# -*- coding: euc-kr -*-

from View.saveMemoUI import SaveMemoUI as UI
from Model.memoList import MemoList as Model


class SaveMemo:
    def __init__(self):
        self.__saveMemoUI: UI = UI(self)

    def saveMemo(self, date, memo):
        memoList = Model()

        memoList.addMemo(date, memo)

    def getUI(self):
        return self.__saveMemoUI

# -*- coding: euc-kr -*-

from View.loadMemoUI import LoadMemoUI as UI
from Model.memoList import MemoList as Model


class LoadMemo:
    def __init__(self):
        self.__loadMemoUI: UI = UI(self)

    def loadMemoList(self, date):
        memo = Model()

        memoShort = memo.getMemoShort(date)
        return memoShort

    def selectMemo(self, date, num):
        memo = Model()

        selectedMemo = memo.getMemo(date, num)
        return selectedMemo

    def getUI(self):
        return self.__loadMemoUI

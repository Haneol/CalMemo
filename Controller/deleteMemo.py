# -*- coding: euc-kr -*-

from View.deleteMemoUI import DeleteMemoUI as UI
from Model.memoList import MemoList as Model


class DeleteMemo:
    def __init__(self):
        self.__deleteMemo: UI = UI(self)

    def deleteMemo(self, date):
        memo = Model()
        memo.delMemo(date)

    def getUI(self):
        return self.__deleteMemo

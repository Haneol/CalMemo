# -*- coding: euc-kr -*-

from View.resetMemoUI import ResetMemoUI as UI
from Model.memoList import MemoList as Model


class ResetMemo:
    def __init__(self):
        self.__resetMemo: UI = UI(self)

    def resetMemo(self):
        memo = Model()
        memo.resetMemo()

    def getUI(self):
        return self.__resetMemo

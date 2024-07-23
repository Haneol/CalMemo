# -*- coding: euc-kr -*-

import os
import pickle
from collections import defaultdict


class MemoList:
    __instance = None
    __memoList = defaultdict(list)

    # SingleTon
    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
            cls.__instance.readMemo()
        return cls.__instance

    def readMemo(self):
        if os.path.exists("memo.pkl"):
            with open("memo.pkl", "rb") as f:
                self.__memoList = pickle.load(f)

    def saveMemo(self):
        with open("memo.pkl", "wb") as f:
            pickle.dump(self.__memoList, f)

    def getMemo(self, date, num):
        val = self.__getMemoList(date)
        if val is not None:
            if len(val) > num:
                return val[num]
            else:
                return None
        else:
            return None

    def getMemoShort(self, date):
        val = self.__getMemoList(date)
        if val is not None:
            memoShort = []
            for i in range(len(val)):
                memoShort.append(val[i])
            return memoShort
        else:
            return None

    def __getMemoList(self, date):
        if date in self.__memoList:
            return self.__memoList[date]
        else:
            return None

    def addMemo(self, date, memo):
        if date not in self.__memoList:
            self.__memoList[date] = [memo]
        else:
            self.__memoList[date].append(memo)

    def delMemo(self, date):
        if date in self.__memoList:
            del self.__memoList[date]

    def resetMemo(self):
        del self.__memoList

    def getMemoByMonth(self, date):
        dates = list(self.__memoList.keys())

        memoByMonth = []
        for d in dates:
            if d[:6] == date[:6]:
                memoByMonth.append(d)

        return memoByMonth

# -*- coding: euc-kr -*-
class SaveMemoUI:
    def __init__(self, saveMemo):
        self.__saveMemo = saveMemo

    def saveMemo(self, date):

        memo = input("추가할 메모 : \n")

        print("\n--------[메모 추가]--------")
        print("메모를 추가하시겠습니까?")
        print("---------------------------")
        print("0. 취소")
        print("1. 메모 추가")
        
        num = input()
        
        if num.isdigit() and int(num) == 1:
            self.__saveMemo.saveMemo(date, memo)
            print("\n--------[메모 추가]--------")
            print("메모가 추가되었습니다!")
            print("---------------------------")
            print("0. 뒤로가기")
            print("1. 다른 메모 추가")
        else:
            print("\n--------[메모 추가]--------")
            print("취소되었습니다!")
            print("---------------------------")
            print("0. 뒤로가기")
            print("1. 다른 메모 추가")
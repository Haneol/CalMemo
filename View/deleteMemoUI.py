# -*- coding: euc-kr -*-
class DeleteMemoUI:
    def __init__(self, deleteMemo):
        self.__deleteMemo = deleteMemo

    def deleteMemo(self, date):
        yy = date[:4]
        mm = date[4:6]
        dd = date[6:8]
        
        print("\n--------[메모 삭제]--------")
        print(f">> {yy}년 {mm}월 {dd}일의 모든 메모를 삭제하시겠습니까?")
        print("---------------------------")
        print("0. 취소")
        print("1. 메모 삭제")

        num = input()
        if num.isdigit() and int(num) == 1:
            self.__deleteMemo.deleteMemo(date)
            print("\n--------[메모 삭제]--------")
            print("해당 날짜의 모든 메모가 삭제되었습니다!")
            print("---------------------------")
            print("0. 뒤로가기")
            print("1. 다른 메모 삭제")
        else:
            print("\n--------[메모 삭제]--------")
            print("취소되었습니다!")
            print("---------------------------")
            print("0. 뒤로가기")
            print("1. 다른 메모 삭제")
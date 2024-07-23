# -*- coding: euc-kr -*-
class ResetMemoUI:
    def __init__(self, resetMemo):
        self.__resetMemo = resetMemo

    def resetMemo(self):
            print("\n--------[메모 초기화]--------")
            print(f">> 모든 메모를 삭제하시겠습니까?")
            print("---------------------------")
            print("0. 취소")
            print("1. 메모 초기화")

            num = input()
            if num.isdigit() and int(num) == 1:
                self.__resetMemo.resetMemo()
                print("\n--------[메모 초기화]--------")
                print("메모가 초기화 되었습니다!")
                print("---------------------------")
                print("0. 뒤로가기")
            else:
                print("\n--------[메모 초기화]--------")
                print("취소되었습니다!")
                print("---------------------------")
                print("0. 뒤로가기")
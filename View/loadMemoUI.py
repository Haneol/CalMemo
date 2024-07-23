# -*- coding: euc-kr -*-
class LoadMemoUI:
    def __init__(self, loadMemo):
        self.__loadMemo = loadMemo

    def loadMemo(self, date):
        yy = date[:4]
        mm = date[4:6]
        dd = date[6:8]

        print("\n--------[메모 보기]--------")
        print(f">> {yy}년 {mm}월 {dd}일")
        memoList = self.__loadMemo.loadMemoList(date)

        if memoList is None:
            print("!! 메모가 존재하지 않습니다. !!")
        else:
            for i in range(len(memoList)):
                print(str(i+1) + ". " + (memoList[i] if len(memoList[i]) <= 10 else memoList[i][:10] + "..."), sep="")

        print("---------------------------")
        print("0. 뒤로가기")
        
        if memoList is not None:
            if len(memoList) == 1:
                print(f"1. 메모 보기")
            elif len(memoList) > 1:
                print(f"1~{len(memoList)}. 메모 보기")

            # 메모 선택
            num = input()
            if num.isdigit() and int(num) == 0:
                print("\n--------[메모 보기]--------")
                print("0. 뒤로가기")
                print("1. 다른 메모 검색")
            elif num.isdigit() and int(num) <= len(memoList) and int(num) > 0:
                self.selectMemo(date, int(num))
            else:
                print("\n--------[메모 보기]--------")
                print(f">> {yy}년 {mm}월 {dd}일")
                print("!! 메모가 존재하지 않습니다. !!")
                print("---------------------------")
                print("0. 뒤로가기")
                print("1. 다른 메모 검색")
            
    
    def selectMemo(self, date, num):
        yy = date[:4]
        mm = date[4:6]
        dd = date[6:8]

        print("\n--------[메모 보기]--------")
        print(f">> {yy}년 {mm}월 {dd}일 {num}번 Memo")
        print(self.__loadMemo.selectMemo(date, num-1))
        print("---------------------------")
        print("0. 뒤로가기")
        print("1. 다른 메모 검색")
# -*- coding: euc-kr -*-
class LoadMemoUI:
    def __init__(self, loadMemo):
        self.__loadMemo = loadMemo

    def loadMemo(self, date):
        yy = date[:4]
        mm = date[4:6]
        dd = date[6:8]

        print("\n--------[�޸� ����]--------")
        print(f">> {yy}�� {mm}�� {dd}��")
        memoList = self.__loadMemo.loadMemoList(date)

        if memoList is None:
            print("!! �޸� �������� �ʽ��ϴ�. !!")
        else:
            for i in range(len(memoList)):
                print(str(i+1) + ". " + (memoList[i] if len(memoList[i]) <= 10 else memoList[i][:10] + "..."), sep="")

        print("---------------------------")
        print("0. �ڷΰ���")
        
        if memoList is not None:
            if len(memoList) == 1:
                print(f"1. �޸� ����")
            elif len(memoList) > 1:
                print(f"1~{len(memoList)}. �޸� ����")

            # �޸� ����
            num = input()
            if num.isdigit() and int(num) == 0:
                print("\n--------[�޸� ����]--------")
                print("0. �ڷΰ���")
                print("1. �ٸ� �޸� �˻�")
            elif num.isdigit() and int(num) <= len(memoList) and int(num) > 0:
                self.selectMemo(date, int(num))
            else:
                print("\n--------[�޸� ����]--------")
                print(f">> {yy}�� {mm}�� {dd}��")
                print("!! �޸� �������� �ʽ��ϴ�. !!")
                print("---------------------------")
                print("0. �ڷΰ���")
                print("1. �ٸ� �޸� �˻�")
            
    
    def selectMemo(self, date, num):
        yy = date[:4]
        mm = date[4:6]
        dd = date[6:8]

        print("\n--------[�޸� ����]--------")
        print(f">> {yy}�� {mm}�� {dd}�� {num}�� Memo")
        print(self.__loadMemo.selectMemo(date, num-1))
        print("---------------------------")
        print("0. �ڷΰ���")
        print("1. �ٸ� �޸� �˻�")
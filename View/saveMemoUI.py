# -*- coding: euc-kr -*-
class SaveMemoUI:
    def __init__(self, saveMemo):
        self.__saveMemo = saveMemo

    def saveMemo(self, date):

        memo = input("�߰��� �޸� : \n")

        print("\n--------[�޸� �߰�]--------")
        print("�޸� �߰��Ͻðڽ��ϱ�?")
        print("---------------------------")
        print("0. ���")
        print("1. �޸� �߰�")
        
        num = input()
        
        if num.isdigit() and int(num) == 1:
            self.__saveMemo.saveMemo(date, memo)
            print("\n--------[�޸� �߰�]--------")
            print("�޸� �߰��Ǿ����ϴ�!")
            print("---------------------------")
            print("0. �ڷΰ���")
            print("1. �ٸ� �޸� �߰�")
        else:
            print("\n--------[�޸� �߰�]--------")
            print("��ҵǾ����ϴ�!")
            print("---------------------------")
            print("0. �ڷΰ���")
            print("1. �ٸ� �޸� �߰�")
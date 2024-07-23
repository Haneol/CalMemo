# -*- coding: euc-kr -*-
class DeleteMemoUI:
    def __init__(self, deleteMemo):
        self.__deleteMemo = deleteMemo

    def deleteMemo(self, date):
        yy = date[:4]
        mm = date[4:6]
        dd = date[6:8]
        
        print("\n--------[�޸� ����]--------")
        print(f">> {yy}�� {mm}�� {dd}���� ��� �޸� �����Ͻðڽ��ϱ�?")
        print("---------------------------")
        print("0. ���")
        print("1. �޸� ����")

        num = input()
        if num.isdigit() and int(num) == 1:
            self.__deleteMemo.deleteMemo(date)
            print("\n--------[�޸� ����]--------")
            print("�ش� ��¥�� ��� �޸� �����Ǿ����ϴ�!")
            print("---------------------------")
            print("0. �ڷΰ���")
            print("1. �ٸ� �޸� ����")
        else:
            print("\n--------[�޸� ����]--------")
            print("��ҵǾ����ϴ�!")
            print("---------------------------")
            print("0. �ڷΰ���")
            print("1. �ٸ� �޸� ����")
# -*- coding: euc-kr -*-
class ResetMemoUI:
    def __init__(self, resetMemo):
        self.__resetMemo = resetMemo

    def resetMemo(self):
            print("\n--------[�޸� �ʱ�ȭ]--------")
            print(f">> ��� �޸� �����Ͻðڽ��ϱ�?")
            print("---------------------------")
            print("0. ���")
            print("1. �޸� �ʱ�ȭ")

            num = input()
            if num.isdigit() and int(num) == 1:
                self.__resetMemo.resetMemo()
                print("\n--------[�޸� �ʱ�ȭ]--------")
                print("�޸� �ʱ�ȭ �Ǿ����ϴ�!")
                print("---------------------------")
                print("0. �ڷΰ���")
            else:
                print("\n--------[�޸� �ʱ�ȭ]--------")
                print("��ҵǾ����ϴ�!")
                print("---------------------------")
                print("0. �ڷΰ���")
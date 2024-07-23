# -*- coding: euc-kr -*-

month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
yoon_month_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# ���� üũ �Լ�
def is_yoon(year):
    year = int(year)
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def lastDate(date):
    year = date[:4]
    month = date[4:6]
    return month_list[int(month)-1] if not is_yoon(year) else yoon_month_list[int(month)-1]


# ��/�� �Է� �޴� �Լ�
def inputMonth():
    print("\n--------[��¥ �Է�]--------")
    while True:
        year = input("�⵵�� �Է��ϼ��� : ")

        ### ����ó�� ###
        if (not year.isdigit()) or len(year) != 4:
            print("!! ������ 4�ڸ��� ���ڿ��� �մϴ� !!")
        else:
            break

    while True:
        month = input("���� �Է��ϼ��� : ")

        ### ����ó�� ###
        if (not month.isdigit()) or (int(month) > 12 or int(month) < 1):
            print("!! ���� 1~12�� ���ڿ��� �մϴ� !!")
        else:
            break

    return year + ("0" + month if len(month) == 1 else month) + "01"


# ��/��/�� �Է� �޴� �Լ�
def inputDate():
    print("\n--------[��¥ �Է�]--------")
    while True:
        year = input("�⵵�� �Է��ϼ��� : ")

        ### ����ó�� ###
        if (not year.isdigit()) or len(year) != 4:
            print("!! ������ 4�ڸ��� ���ڿ��� �մϴ� !!")
        else:
            break

    while True:
        month = input("���� �Է��ϼ��� : ")

        ### ����ó�� ###
        if (not month.isdigit()) or (int(month) > 12 or int(month) < 1):
            print("!! ���� 1~12�� ���ڿ��� �մϴ� !!")
        else:
            break

    while True:
        date = input("���� �Է��ϼ��� : ")

        ### ����ó�� ###
        if (not date.isdigit()) or (
            int(date)
            > (
                month_list[int(month) - 1]
                if not is_yoon(year)
                else yoon_month_list[int(month) - 1]
            )
            or int(date) < 0
        ):
            print("!! �����ϴ� ���� ���ڷ� ����մϴ� !!")
        else:
            break

    return (
        year
        + ("0" + month if len(month) == 1 else month)
        + ("0" + date if len(date) == 1 else date)
    )

def dateToDay(date):
    sum_of_date = 0

    yy = int(date[:4])
    mm = int(date[4:6])
    dd = int(date[6:8])

    # add year
    sum_of_date += (
        (yy - 1) * 365
        + ((yy - 1) // 4)
        - ((yy - 1) // 100)
        + ((yy - 1) // 400)
    )

    # add month
    if mm != 1:
        if not is_yoon(yy):
            sum_of_date += sum(month_list[0 : mm - 1])
        else:
            sum_of_date += sum(yoon_month_list[0 : mm - 1])

    # add date
    sum_of_date += dd

    return sum_of_date % 7

# -*- coding: euc-kr -*-

month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
yoon_month_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# 윤년 체크 함수
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


# 년/월 입력 받는 함수
def inputMonth():
    print("\n--------[날짜 입력]--------")
    while True:
        year = input("년도를 입력하세요 : ")

        ### 예외처리 ###
        if (not year.isdigit()) or len(year) != 4:
            print("!! 연도는 4자리의 숫자여야 합니다 !!")
        else:
            break

    while True:
        month = input("월을 입력하세요 : ")

        ### 예외처리 ###
        if (not month.isdigit()) or (int(month) > 12 or int(month) < 1):
            print("!! 월은 1~12의 숫자여야 합니다 !!")
        else:
            break

    return year + ("0" + month if len(month) == 1 else month) + "01"


# 년/월/일 입력 받는 함수
def inputDate():
    print("\n--------[날짜 입력]--------")
    while True:
        year = input("년도를 입력하세요 : ")

        ### 예외처리 ###
        if (not year.isdigit()) or len(year) != 4:
            print("!! 연도는 4자리의 숫자여야 합니다 !!")
        else:
            break

    while True:
        month = input("월을 입력하세요 : ")

        ### 예외처리 ###
        if (not month.isdigit()) or (int(month) > 12 or int(month) < 1):
            print("!! 월은 1~12의 숫자여야 합니다 !!")
        else:
            break

    while True:
        date = input("일을 입력하세요 : ")

        ### 예외처리 ###
        if (not date.isdigit()) or (
            int(date)
            > (
                month_list[int(month) - 1]
                if not is_yoon(year)
                else yoon_month_list[int(month) - 1]
            )
            or int(date) < 0
        ):
            print("!! 존재하는 일을 숫자로 써야합니다 !!")
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

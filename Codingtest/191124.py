# 정수 배열(int array)이 주어지면 두번째로 큰 값을 프린트하시오.
#
# 예제)
# Input: [10, 5, 4, 3, -1]
# Output: 5
#
# Input: [3, 3, 3]
# Output: Does not exist.


def ret_second(lst):
    lst = list(set(lst))  # set 함수로 중복 제거
    lst.sort(reverse=True)  # sort 함수로 정렬, 내림차순
    if len(lst) < 2:  # 두번쨰로 큰 함수가 존재하지 않으면
        print("Does not exist")
    else:
        print(lst[1])


if __name__ == "__main__":
    a = [10, 5, 4, 3, -1]
    b = [3, 3, 3]
    ret_second(a)
    ret_second(b)

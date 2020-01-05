# 정수 배열(int array)이 주어지면 0이 아닌 정수 순서를 유지하며 모든 0을 배열 오른쪽 끝으로 옮기시오. 단, 시간복잡도는 O(n), 공간복잡도는 O(1)여야 합니다.
#
# Input: [0, 5, 0, 3, -1]
#
# Output: [5, 3, -1, 0, 0]
#
# Input: [3, 0, 3]
#
# Output: [3, 3, 0]


def shift_zero(lst):
    for i in range(len(lst)):
        if lst[i] == 0:
            del lst[i]
            lst.append(0)


if __name__ == "__main__":
    a = [0, 5, 0, 3, -1]
    print(a)
    shift_zero(a)
    print(a)

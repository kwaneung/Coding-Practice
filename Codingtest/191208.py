# String이 주어지면, 중복된 char가 없는 가장 긴 서브스트링(substring) 의 길이를 찾으시오.
#
# 예제)
# Input: “aabcbcbc”
# Output: 3 // “abc”
#
# Input: “aaaaaaaa”
# Output: 1 // “a”
#
# Input: “abbbcedd”
# Output: 4 // “bced”


def len_overlap(s):
    visited = {}
    for i in range(len(s)):
        visited[s[i]] = 0
    curL = 1
    maxL = 1

    for i in range(len(s)):
        prev_index = visited[s[i]]

        if prev_index == -1 or i - curL > prev_index:
            curL = curL + 1
        else:
            if curL > maxL:
                maxL = curL

            curL = i - prev_index
        visited[s[i]] = i

    if curL > maxL:
        maxL = curL
    return maxL


if __name__ == "__main__":
    a = "abbbcedd"
    print(len_overlap(a))

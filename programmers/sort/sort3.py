
def solution(citations):
    citations.sort(reverse=True)
    t = enumerate(citations, start=1)
    a = map(min, t)
    answer = max(a)
    return answer


c = [3, 0, 6, 1, 5]
ans = solution(c)
print(ans)
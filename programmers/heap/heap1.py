# from queue import PriorityQueue
#
# def solution(scoville, K):
#     answer = 0
#     pq = PriorityQueue()
#     for s in scoville:        # O(nlgn)
#         pq.put(s)
#     while True:               # O(n)
#         if pq.qsize() == 1:
#             return -1
#         answer += 1
#         tmp = pq.get() * 1    # O(lgn)
#         tmp += pq.get() * 2   # O(lgn)
#         pq.put(tmp)
#         check = pq.get()
#         if check >= K:
#             break
#         else:
#             pq.put(check)
#     return answer


# def solution(scoville, K):
#     answer = 0
#     scoville.sort()
#     while scoville[0] < K:
#         if len(scoville) == 1:
#             return -1
#         answer += 1
#         tmp = scoville[0] + scoville[1]*2
#         scoville.pop(0)
#         scoville.pop(0)
#         if len(scoville) == 0:
#             if tmp < K:
#                 return -1
#             else:
#                 return answer
#         if tmp >= scoville[-1]:
#             scoville.append(tmp)
#         else:
#             for i in range(0, len(scoville)):
#                 if scoville[i] > tmp:
#                     scoville.insert(i, tmp)
#                     break
#     return answer


# def find_min(_list, K):
#     _list.sort()
#     if _list[0][0] >= K:
#         return -1
#     elif _list[0][1] == 2 or _list[1][1] == 2: # tmp selected
#         return 1
#     else:   # tmp not selected
#         return 2


def solution(scoville, K):
    scoville.sort()
    if scoville[0] >= K:    # already satisfied
        return 0
    pivot = 0
    answer = 0
    tmp = 1000001
    while pivot < len(scoville):
        if pivot == len(scoville)-1:
            tmp = min(scoville[pivot], tmp) + max(scoville[pivot], tmp) * 2
            if
        _min = min(scoville[pivot+1], tmp)
        if _min == tmp:
            tmp = min(scoville[pivot], tmp) + max(scoville[pivot], tmp)*2
            pivot += 1
        else:
            tmp = scoville[pivot] + scoville[pivot+1]
            pivot += 2
        answer += 1
        if scoville[pivot] >= K and tmp >= K:
            return answer
    if tmp < K:
        return -1
    return answer


s = [1, 2, 3, 9, 10, 12]
s = [1,2]
ans = solution(s, 7)
print(ans)

# delta_p = find_min([[scoville[pivot], 0], [scoville[pivot + 1], 1], [tmp, 2]], K)
# if delta_p == -1:
#     return answer
# elif delta_p == 2:
#     tmp = tmp
#
# else:
#     tmp =
# pivot += delta_p
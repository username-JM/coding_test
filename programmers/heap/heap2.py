from queue import PriorityQueue
def solution(jobs):
    answer = 0
    time = 0
    ps_list = sorted(jobs, key=lambda x : (x[0], x[1]))
    waiting_ps = PriorityQueue()

    while len(ps_list) > 0 or not waiting_ps.empty():
        if waiting_ps.empty():
            ps = ps_list.pop(0)
            time = ps[0] + ps[1]
        else:
            ps = waiting_ps.get()
            ps = (ps[1], ps[0])
            time += ps[1]

        answer += time - ps[0]
        print("time : " + str(time) + "  (" + str(ps[0]) + "," + str(ps[1]) + ")")

        while len(ps_list) > 0:
            if time > ps_list[0][0]:
                tmp = ps_list.pop(0)
                waiting_ps.put((tmp[1], tmp[0]))
            else:
                break

    return answer//len(jobs)


p = [[0, 3], [1, 9], [2, 6], [5, 3]]
# p = [[1, 4]]
ans = solution(p)
print(ans)


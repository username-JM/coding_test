def solution(operations):
    _list = []
    for cmd in operations:
        tmp = cmd.split(' ')
        if tmp[0] == 'I':
            _list.append((int)(tmp[1]))
        elif tmp[1] == '1' and len(_list) > 0:
            _list.remove(max(_list))
        else:
            if len(_list) > 0:
                _list.remove(min(_list))
    if len(_list) > 0:
        return [max(_list), min(_list)]
    return [0,0]


op = ["I 7","I 5","I -5","D -1"]
op2 = ["I 16","D 1"]
op3 = ["I -45","I 653","D 1","I -642","I 45", "I 97", "D 1","D -1", "I 333"]
ans = solution(op3)
print(ans)
N = int(input())
people = [tuple(map(int, input().split(' '))) for _ in range(N)]
tribes = [set(), set()]
for first, second in people:
    for tribe in tribes:
        if not tribe:
            tribe.add(first)
            tribe.add(second)
            break
        elif first in tribe:
            tribe.add(second)
            break
        elif second in tribe:
            tribe.add(first)
            break
boys = [len({p for p in t if p%2}) for t in tribes]
girls = [len({p for p in t if not p%2}) for t in tribes]
print(boys[0]*girls[1]+boys[1]*girls[0])

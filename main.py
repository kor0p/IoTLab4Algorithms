def wedding(N, people, p):
    if p:
        print(N, *people)
    tribes = [set()]
    for first, second in people: # iter inputs
        o = 0                    # and add them to first free tribe
        for tribe in tribes:     # or if someone is in tribe —
            o = 0                # — add another
            if not tribe:        #
                tribe.add(first) #
                tribe.add(second)#
            elif first in tribe: #
                tribe.add(second)#
            elif second in tribe:#
                tribe.add(first) #
            else:                #
                o = 1            #
            if not o:            # break if already add to tribe
                break            #
        if o:                    # then add new tribe if no free tribe
            tribes.append(set((first, second)))
    boys = [len({p for p in t if p%2}) for t in tribes]
    girls = [len({p for p in t if not p%2}) for t in tribes]
    # res = sum((boys[i]*(sum(girls)-girls[i]) for i in range(len(tribes))))
    # mathematically is the same, but faster
    return sum(boys)*sum(girls)-sum((b*g for b,g in zip(boys, girls)))
print('Example 1:'); print(wedding(3, ((1,2), (2,4), (3,5)),1),'\n')
print('Example 2:'); print(wedding(5, ((1,2), (2,4), (1,3), (3,5), (8,10)),1),'\n')
print('My example:');print(wedding(4, ((1,2), (2,4), (3,5), (8,10)),1),'\n')

in_N = int(input())
in_people = [tuple(map(int, input().split(' '))) for _ in range(N)]
print(wedding(in_N, in_people))

def flatten(seq):
    arr = []
    for el in seq:
        if isinstance(el, tuple) or isinstance(el,list):
            arr += flatten(el)
        else:
            arr.append(el)

    return arr


print(flatten([1,(2,3),[],[4,(5,6,7)],8,[9]]))



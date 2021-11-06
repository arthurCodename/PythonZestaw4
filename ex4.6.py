def sum_seq(sequence):
    sum1 = []
    for el in sequence:
        sum2 = 0
        if len(el) == 0:
            sum1.append(0)
        else:
            for x in range(len(el)):
                sum2 = sum2 + el[x]
            sum1.append(sum2)
    return sum(sum1)

print(sum_seq([[],[4],(1,2),[3,4],(5,6,7)]))
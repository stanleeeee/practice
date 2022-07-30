def fbc(n):
    num = 0
    array =[]
    for i in range(n):
        array.append(num)
        if len(array) > 1:
            num += array[i-1]
        else:
            num += 1
    return array

print(fbc(5))

def kaprekar(low,high):
    output = []
    for i in xrange(low, high + 1):

        if len(str(i ** 2)) == 1:
            if i == 1:
                output.append(i)
                
        else:
            if int(str(i ** 2)[ : len(str(i ** 2))/2]) + int(str(i ** 2)[len(str(i ** 2))/2 : ]) == i:
                output.append(i)
                
    if output == []:
        return "INVALID RANGE"
    else:
        return ' '.join(map(str,output))

l = int(raw_input().strip())
h = int(raw_input().strip())

print kaprekar(l,h)
    

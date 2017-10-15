times=0
one=0
two=0
three=0
mnk = [int(x) for x in input().split(";")]
rate = [0]*mnk[0]
B = [[0] * mnk[1]]*mnk[0]

for i in range(0,mnk[0]):
    B[i] = [int(x) for x in input().split(",")]
    for j in range(0, mnk[1]):
        if B[i][j]!=0:
            times+=1
    rate[i]=sum(B[i])-times*mnk[2]
    times=0
    if rate[i]>=rate[one]:
        three = two
        two = one
        one=i+1
    if rate[i] == rate[two-1]:
        three=i+1

print(rate,one,two,three)

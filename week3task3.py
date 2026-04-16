def smallest(n:float, m:float) -> float:
    if n<m:
        return n  #for which calls below is this statement evaluated? neither
    else:
        return m

first = smallest(3,2) #what is the value of first? 2
second = smallest(2,2) #what is the value of second? is this a reasonable result? why or why not?
# second = 2, this is reasonable because 2 is not less than 2 so it skips to else and returns m = 2
print()

def function2(a:int, b:int, c:int) -> int:
    if a>b and a>c:
        return a-b #in general, when will a call to this function evaluate this statement? when a>b and a>c
    elif b>c:
        return b+c #in general, when will a call to this function evaluate this statement? when a<b or a<c and b>c
    else: return 2*c #in general, when will a call to this function evaluate this statement? when a<b or a<c and b<c

answer1 = function2(3,2,1) #what is the value of answer1? 1
answer2 = function2(2,3,1) #what is the value of answer2? 4
answer3 = function2(2,1,3) #what is the value of answer3? 6
print()

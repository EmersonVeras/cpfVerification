CPF = '16899535009'

FIRSTCALC = [10, 9, 8, 7, 6, 5, 4, 3, 2]
SECONDCALC = [11, 10, 9, 8, 7, 6, 5, 4, 3]
CONSTANT = 11
REMNANTCONSTANT = 2

def solution(number):
    list = []
    vector = []
    appendVectorFirst = []
    appendVectorSecond = []

    for i in range(len(number)):
        list.append(number[i])

    for j in range(len(list)):
        listInt = int(list[j])
        vector.append(listInt)
    
    vector.pop()
    vector.pop()

    for k in range(len(vector)):
        firstNumbers = FIRSTCALC[k]
        secondNumbers = SECONDCALC[k]
        vectorValues = vector[k]
        appendVectorFirst.append(firstNumbers*vectorValues) 
        appendVectorSecond.append(secondNumbers*vectorValues)
    
    sumVectorFirst = sum(appendVectorFirst)
    sumVectorSecond = sum(appendVectorSecond)

    # FIRST DIGIT LOGIC
    remnantVectorFirst = CONSTANT - (sumVectorFirst % CONSTANT)
    if remnantVectorFirst > 9:
        firstType = 0   
    else:
        firstType = remnantVectorFirst

    # SECOND DIGIT LOGIC
    remnantFirstType = firstType * REMNANTCONSTANT
    remnantVectorSecond = CONSTANT - ((sumVectorSecond + remnantFirstType) % CONSTANT)
    
    if remnantVectorSecond > 9:
        secondType = 0
    else:
        secondType = remnantVectorSecond
    
    # VERIFICATION TYPE
    if firstType == int(CPF[9]) and secondType == int(CPF[10]):
        print(f"CPF is right!: First Type -> {firstType} and Second Type -> {secondType}")
    else:
        print(f"CPF is wrong!: First Type -> {firstType} and Second Type -> {secondType}")
    
    return firstType, secondType

solution(CPF)
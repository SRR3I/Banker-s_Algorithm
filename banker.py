def system_in_safe(allocation, max, available):
    process_number = len(allocation)
    resources = len(available)
    sequence = []
    work = available
    need = [[0]*resources for _ in range(process_number)]
    finsh = [False]*process_number
    for i in range(process_number):
        for j in range(resources):
            need[i][j] = max[i][j] - allocation[i][j]
    PasibaleSafeSequence = True
    while not all(finsh) and PasibaleSafeSequence:
        PasibaleSafeSequence = False
        for i in range(process_number):
            needLessThenWork = [False]*resources
            for j in range(resources):
                if need[i][j] <= work[j]:
                    needLessThenWork[j] = True
                else:
                    break
            if all(needLessThenWork) and not finsh[i]:
                print(work)
                for j in range(resources):
                    work[j] += allocation[i][j]
                finsh[i] = True
                sequence.append(f'P{i}')
                PasibaleSafeSequence = True

    if all(finsh):
        print("The system is in a safe state with the sequence ", sequence)
    else:
        print("The system is Not in a safe state ")


Allocation = [
    [0,1,0],
    [2,0,0],
    [3,0,2],
    [2,1,1],
    [0,2,2]
]

Max = [
    [7,5,3],
    [3,2,2],
    [9,0,2],
    [2,2,2],
    [4,3,3],
]

Available = [3,3,2]

system_in_safe(Allocation, Max, Available)

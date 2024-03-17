def CalculateNeed(Max, Allocation):
    resources = len(Allocation[0])
    processes = len(Allocation)
    need = [[0]*resources for _ in range(processes)]
    for i in range(processes):
        for j in range(resources):
            need[i][j] = Max[i][j] - Allocation[i][j]

    return need


def Resource_Request(requist, process, Need, avail, alloca):
    for i in range(len(requist)):
        if requist[i] > Need[process][i]:
            print(f'Error condition, the system must wait, since Need {Need[process]} of P{process} < Request {requist}')
            return False, False, False
        if requist[i] > avail[i]:
            print(f'Error condition, the system must wait, since Available {avail} of P{process} < Request {requist}')
            return False, False, False

        avail[i] -= requist[i]
        alloca[process][i] += requist[i]
        Need[process][i] -= requist[i]

    return avail, alloca, Need


def system_in_safe(allocation, need, available):
    process_number = len(allocation)
    resources = len(available)
    sequence = []
    finsh = [False]*process_number
    work = available
    pasibaleSafeSequence = True
    while not all(finsh) and pasibaleSafeSequence:
        pasibaleSafeSequence = False
        for i in range(process_number):
            needLessThenWork = all(need[i][j] <= work[j] for j in range(resources))
            if needLessThenWork and not finsh[i]:
                for j in range(resources):
                    work[j] += allocation[i][j]
                finsh[i] = True
                sequence.append(f'P{i}')
                pasibaleSafeSequence = True

    if all(finsh):
        print("The system is in a safe state with the sequence ", sequence)
    else:
        print("The system is Not in a safe state")


Allocation = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]

Max = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]

Available = [3, 3, 2]


Need = CalculateNeed(Max, Allocation)

Available, Allocation, Need = Resource_Request(
    [1, 0, 2], 1, Need, Available, Allocation)

if Available != False:
    system_in_safe(Allocation, Need, Available)

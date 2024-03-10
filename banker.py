from fomate import tabulate
Proseses = int(input('processes : '))
resourse = int(input('resourse : '))
table = [[0]*5 for _ in range(Proseses)]

waiting = []
sequence = []
need = []
for i in range(5):
    for j in range(Proseses):
        if i == 0:
            table[j][i] = input(f'prosess {j} : ')
        elif i == 1:
            table[j][i] = input(f'allccation {j} : ')
        elif i == 2:
            table[j][i] = input(f'max {j} : ')
        elif i == 3 and j == 0:
            table[j][i] = input(f'available {j}: ')
        elif i == 4:
            # calculate need
            table[j][i] = ''
            for res in range(resourse):
                table[j][i] += str(int(table[j][2][res]) -
                                   int(table[j][1][res]))
            need.append(table[j][i])

# check if in safe sequence

currnt_value = table[0][3]
# i=0;
# while need and waiting:
#     LessThenCurrntValue = False
#     for res in range(resourse):
#         if table[i][4][res] <= currnt_value[res]:
#             LessThenCurrntValue = True
#         else:
#             LessThenCurrntValue = False
#             waiting.append(i)
#             break
#     if LessThenCurrntValue:
#         table[i][3] = ''
#         for res in range(resourse):
#             table[i][3] += str(int(currnt_value[res])+int(table[i][1][res]))
#         currnt_value = table[i][3]
#         sequence.append(table[i][0])
i = 0
while i < Proseses or waiting:
    LessThenCurrntValue = False
    for res in range(resourse):
        if table[i][4][res] <= currnt_value[res]:
            LessThenCurrntValue = True
        else:
            LessThenCurrntValue = False
            waiting.append(i)
            break
    if LessThenCurrntValue:
        table[i][3] = ''
        for res in range(resourse):
            table[i][3] += str(int(currnt_value[res])+int(table[i][1][res]))
        currnt_value = table[i][3]
        sequence.append(table[i][0])
    i += 1


for i in table:
    print(i)

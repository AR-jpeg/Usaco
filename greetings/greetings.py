with open('greetings.in') as f:
    lines = f.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')


lineNumber = 0

bessieLineNumber, elsieLineNumber = lines[lineNumber].split()
differece = bessieLineNumber

lines.pop(0)

bessieInstructions = lines[:int(bessieLineNumber)]
lines = lines[int(bessieLineNumber):]
elsieInstructions = lines[:]
nTimesMet = 0

oldbPos, oldePos = 0, 0
bPos, ePos = 0, 0

if len(elsieInstructions) > len(bessieInstructions):
    for _ in range(len(elsieInstructions) - len(bessieInstructions)):
        bessieInstructions.append("0 R")

if len(bessieInstructions) > len(elsieInstructions):
    for _ in range(len(bessieInstructions) - len(elsieInstructions)):
        elsieInstructions.append("0 R")


def intersect(bPos, ePos, oldbPos, oldePos):
    if ePos == bPos:
        return True

    if oldbPos > oldePos:
        smallerCow = 'elsie'
    else:
        smallerCow = 'bessie'
    if bPos > ePos:
        biggerCow = 'bessie'
    else:
        biggerCow = 'elsie'

    # print(smallerCow, biggerCow)
    if smallerCow == 'elsie' and biggerCow == 'elsie':
        return True
    elif smallerCow == 'bessie' and biggerCow == 'bessie':
        return True

    return


for bInstruction, eInstruction in zip(bessieInstructions, elsieInstructions):
    if bInstruction[-1] == 'R':
        bPos += int(bInstruction.split()[0])
    elif bInstruction[-1] == 'L':
        bPos -= int(bInstruction.split()[0])

    if eInstruction[-1] == 'R':
        ePos += int(eInstruction.split()[0])
    elif eInstruction[-1] == 'L':
        ePos -= int(eInstruction.split()[0])

    if intersect(bPos, ePos, oldbPos, oldePos) == True:
        print(bPos, ePos, oldbPos, oldePos, 'intersected')
        nTimesMet += 1

    # print(bPos, ePos)
    oldbPos, oldePos = bPos, ePos

with open('greetings.out', 'w') as f:
    f.write(str(nTimesMet))

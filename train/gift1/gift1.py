"""
ID: araoudu1
LANG: PYTHON3
TASK: gift1
"""

with open('gift1.in', 'r') as f:
    lines = f.read().split('\n')

# Global Variables
current_line = 0
amount_of_people = int(lines[0])
people = {}

names = lines[1:amount_of_people+1]
for name in names:
    people[name] = 0


current_line = amount_of_people+1


def money(amount_to_give, amount_of_people_to_give_to):
    return (amount_to_give % amount_of_people_to_give_to) - amount_to_give


def block(current_line):
    cp = lines[current_line]
    current_line += 1

    temp = lines[current_line].split()
    amount_to_give = int(temp[0])
    amount_of_people_to_give_to = int(temp[1])
    current_line += 1

    if amount_to_give == 0 or amount_of_people_to_give_to == 0:
        return current_line + amount_of_people_to_give_to

    people[cp] += money(amount_to_give, amount_of_people_to_give_to)

    for _ in range(amount_of_people_to_give_to):
        people[lines[current_line]] += amount_to_give // amount_of_people_to_give_to
        current_line += 1

    return current_line


for i, person in zip(range(amount_of_people), people):
    current_line = block(current_line)

with open('gift1.out', 'w') as f:
    for person in people:
        f.write(person + " " + str(people[person]) + '\n')

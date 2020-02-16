import sys
num = []
turn = 'X'

for i in range(1, 10):
    num.append(i)

print('WELCOME TO TIC TAC TOE ')
#----------------------------FUNTION DEFINITION-------------------------------------------
def disp():
    print("""
        1|2|3
        -----
        4|5|6
        -----
        7|8|9""")

    print(num[0], '|', num[1], '|', num[2])
    print(" ----- ")
    print(num[3], '|', num[4], '|', num[5])
    print(" ----- ")
    print(num[6], '|', num[7], '|', num[8])
    print()

def forRows():
    for a in range(0, 7, 3):
        if num[a] == num[a+1] and num[a] == num[a+2]:
            print('Player ',turn,"won !")
            sys.exit()

def forColumns():
    for a in range(0, 4, 1):
        if num[a] == num[a+3] and num[a] == num[a+6]:
            print('Player ',turn,"won !")
            sys.exit()

def forDiagonal():
    if (num[0] == num[4] and num[0] == num[8]):
        print("Player "+ turn + ' won !')
        sys.exit()
    if (num[2] == num[4] and num[0] == num[6]):
        print("Player "+ turn +' won !')
        sys.exit()

for c in range(9):
    try :
        choice = int(input('Where do you want to insert ' + turn + '?...'))
        if num[choice - 1] == 'X' or num[choice - 1] == 'Y':
            print("You cannot place values there ..Enter the position again..")
            disp()
            continue
    except :
        print('Plzz enter the valid position')
        continue
    num[choice - 1] = turn
    disp()
    forRows()
    forColumns()
    forDiagonal()

    if turn is 'X':
        turn = 'O'
    else:
        turn = 'X'

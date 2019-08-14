#约瑟夫环问题
def main():
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while count < 15:
        if persons[index]:
            number += 1
            if(number == 9):
                person[index] = False
                count += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非', end='')

if _name_ == '_main_':
    main()
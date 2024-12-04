Prompt = input('Введите строку для поиска')
a = []
with open("text.txt", "r") as file:
    for line in file:
        if Prompt in line:
            print(line)
            a.extend(line)
    b = ''.join(a)
    list = b.split('\n')
    list.sort()
    print(list)

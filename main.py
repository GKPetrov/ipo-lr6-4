prompt=input('Введите строку для поиска')
strings_list=[]
with open("text.txt", "r") as file:
    for line in file:
        if prompt in line:
            print(line)
            strings_list.extend(line)
    string_of_strings=''.join(strings_list)
    sorted_strings=sorted(string_of_strings.split('\n'))
    for strings in sorted_strings:
        print(strings)
    

Prompt=input('Введите строку для поиска')
strings_list=[]
with open("text.txt", "r") as file:
    for line in file:
        if Prompt in line:
            print(line)
            strings_list.extend(line)
    string_of_strings=''.join(strings_list)
    sorted_strings=sorted(string_of_strings.split('\n'))
    for i in range(len(sorted_strings)):
        print(sorted_strings[i])
    

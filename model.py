
def run_contact (name):
    
    with open('data.txt', 'r', encoding='utf-8') as file:
        line = file.read().split('\n')
    k = 0
    for i in range(len(line)):
        if name in line[i]:
            name = line[i]
        else:
            k +=1
    if k == len(line):
       name = 'Нет такокого контакта'
    return name



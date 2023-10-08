list = []
while (True):
    line = input("Введите строку (или просто ВВОД для выхода):")
    if (line):
        line = line + "\n"
        list.append(line)
    else:
        break
with open("F1.txt", "a+") as file1:
    file1.writelines(list)
    file1.seek(0)
    cont1 = file1.readlines()
    print("F1: ", cont1)
with open("F2.txt", "a+") as file2:
    for i in list:
        if (i.startswith("A")):
            file2.write(i)
    file2.seek(0)
    cont2 = file2.readlines()
    print("F2: ", cont2)
print("\tКоличество строк в F2: ", len(cont2))
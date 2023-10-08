list = []
while (True):
    line = input("Введите строку (или просто ВВОД для выхода):")
    if (line):
        line = line + "\n"
        list.append(line)
    else:
        break
while True:
    try:
        k = int(input("Введите К: "))
        break
    except ValueError:
        print("\tВведено нечисловое значение")
with open("F1.2.txt", "w+") as f1, open("F2.1.txt", "w+") as f2:
    f1.writelines(list)
    f1.seek(0)
    lines = f1.readlines()
    try:
        for i in range(k - 1, k + 4):
            f2.write(lines[i])
    except IndexError:
        print("Недостаточно записей")
    else:
        f1.seek(0)
        f2.seek(0)
        cont1 = f1.readlines()
        cont2 = f2.readlines()
        print("F1.1: ", cont1)
        print("F2.2: ", cont2)
        count = 0
        vowels = 'aeioyuуеаоэюия'
        for line in cont2:
            line = str(line).lower()
            for i in line:
                if i in vowels:
                    count += 1
        print("\tКоличество гласных: ", count)
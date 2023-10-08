import json

dict1 = {}
dict2 = {}
number_of_firms = 0
average_profit = 0
with open("Фирмы.txt", "r",encoding='utf-8') as file:
    for line in file:
        firm = line.split(" ")
        firm[0] = str(firm[0])
        income = int(firm[2]) - int(firm[3])
        dict1[firm[0]] = income
        if (income > 0):
            number_of_firms += 1
            average_profit += income
try:
    dict2["average_profit"] = int(average_profit / number_of_firms)
except ZeroDivisionError:
    print("Нет прибыльных фирм")
    exit(0)
list = [dict1, dict2]
print(list)
with open("Фирмы.json", "w+") as file:
    json.dump(list, file,ensure_ascii=False)
    file.seek(0)
    print(*file)

with open("Цветы.txt", "r",encoding='utf-8') as file:
    sum=0
    num_of_flowers=0
    for line in file:
        flower=line.split(" ")
        cost=int(flower[1])
        if(cost>10):
            print(str(flower[0]),": ",cost)
        sum+=cost
        num_of_flowers+=1
print("\nСредняя стоимость: ", sum/num_of_flowers)
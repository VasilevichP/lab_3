with open("Занятия.txt", "r",encoding='utf-8') as file:
    results = []
    for line in file:
        subject=line.split(" ")
        for ind,val in enumerate(subject):
            if(ind==0):
                subject[ind]=str(val[:len(val) - 1])
            else:
                num=''
                subject[ind] = str(val)
                for i in subject[ind]:
                    if(i.isdigit()):
                        num+=i
                    else:
                        break
                subject[ind]=int(num)
        sum=0
        for i in subject:
            if(isinstance(i,int)):
                sum += i
        del subject[1:]
        subject.append(sum)
        results.append(subject)
    di={i[0]:i[1] for i in results}
    print(di)
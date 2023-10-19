a = list(map(int,input().split(" ")))

count = len(list(filter(lambda x: x >=80 , a)))

if count >= 3:
    print("Mamma mia!")
elif 1 <= count <= 2:
    print("Mamma mia!!")
else : print("Mamma mia!!!")
import os 

with open("teste.txt","r", encoding="UTF-8") as cursor:
    for row  in cursor:
        print(row)
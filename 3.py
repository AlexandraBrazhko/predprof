#3
fin=open('vacancy.csv', 'r', encoding='utf-8')
title=fin.readline()
vacancy=[x.strip() for x in fin]
fin.close()

for x in vacancy:
    a=input()
    x=x.split()
    if a!='None':
        if x[4]==a:
            print('В {x[4]} найдена вакансия: {x[1]}. З/п составит: {x[0]}')
        else:
            print('К сожалению, ничего не удалось найти')

    else:
        break
        
    

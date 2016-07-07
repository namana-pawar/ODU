import random
dice=random.randrange(1, 6)
col=1
row=1
decision=True
val=0
diff=[]
nr=eval(input("enter row"))
nc=eval(input("enter column"))
entry=nc-1
count=0
while count<nc-1:
    if count<(nc//2)-1:
        diff.append(entry)
       
        if count!=(nc//2)-1:
            entry=entry-2
       
    
    else: 
        diff.append(-entry)
        
        entry=entry+2
        
    count+=1
diff.insert(nc//2,1)
print(diff)

while decision:
    print (dice)
    if row!=nc:
        if row%2!=0:
             col+=dice
             if col>nc:
                row+=1
                col-=nc
                col=col+diff[(col%nc)-1]
        else:
             col-=dice
             if col<1:
                row+=1
                col+=nc
                col=col+diff[(col%nc)-1]
               
            
    else:
        if 1<=(col-dice):
            col-=dice
    
    print('Pon is in position',row,col)
    if row==nr and col==1:
        print('you won')
        break
    dec=input('Do you want to roll the dice? enter Yes or No')
    if dec=="y":
        decision=True
    else:
        decision=False
    dice=random.randrange(1, 6)

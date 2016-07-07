import random
dice=random.randrange(1, 6)
col=1
row=1
decision=True
c=1
val=0
diff=[7,5,3,1,-1,-3,-5,-7]
while decision:
    print (dice)
    if row!=8:
        if row%2!=0:
             col+=dice
             if col>8:
                row+=1
                col-=8
                col=col+diff[(col%8)-1]
        else:
             col-=dice
             if col<1:
                row+=1
                col+=8
                col=col+diff[(col%8)-1]
               
            
    else:
        if 8>=(col+dice):
            col+=dice
        
            
    
    
    c+=1
    
    print('Pon is in position',row,col)
    if row==8 and col==8:
        print('you won')
        break
    dec=input('Do you want to roll the dice? enter Yes or No')
    if dec=="yes":
        decision=True
    else:
        decision=False
    dice=random.randrange(1, 6)

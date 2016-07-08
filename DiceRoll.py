import random
import os

def play(dice,decision,diff,nc,nr,mark):
    
    
    num=0
    
    col=0
    row=1
    while decision:
        os.system('clear') 
        print ("dice value is",dice)
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
            if 1>=(col-dice):
                rollback=-1*(col-dice)+1
                play(rollback,decision,diff,nc,nr,mark)
            else:
                col-=dice
        
        mark[row-1][col-1]='x'
        print('Pawn is in position..',row,col)
        
        for i in range(nr):
            print mark[i][0:nc]
            print
        
        
        for i in range(0,nr):
            DoneR=0
            DoneC=0
            for j in range(0,nc):
                
                if mark[i][j]=='x':
                    DoneC+=1
                elif mark[j][i]=='x':
                    DoneR+=1
            if DoneC==nc or DoneR==nr: 
                print("you won")
                decision=False
                break
            
        dec=raw_input('Do you want to roll the dice? enter Yes or No')
        if dec=="yes":
            decision=True
        else:
            decision=False
        dice=random.randrange(1, 6)
           
            
        
def main():

    dice=random.randrange(1, 6)
    
    decision=True
    diff=[]
    
    
    count=0
    nr=int(input("enter row"))
    nc=int(input("enter column"))
    mark = [[0 for x in range(nr)] for y in range(nc)] 
    entry=nc-1
    while count<nc-1:
        if count<(nc//2)-1:
            diff.append(entry)

            if count!=(nc//2)-1:
                entry=entry-2


        else:
            diff.append(-entry)

            entry=entry+2

        count+=1
    diff.insert((nc//2)-1,1)
    print(diff)
    play(dice,decision,diff,nc,nr,mark)
main()


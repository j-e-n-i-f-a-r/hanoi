# creating blocks 1,2,3  and stands st1,st2,st3

st1 = [3,2,1]
fs = [3,2,1]
print(fs)
st2 = []
st3 = []
print(st1,st2,st3)
print("\n\nLARGE BLOCK IS 3\nMEDIUM BLOCK IS 2\nSMALL BLOCK IS 1")
l =8
print("\n\n")

#getting block input from user

def blck():
    b=int(input("which block:"))
    if b>3:
        print("\n---INVALID BLOCK---\n")
        b=int(input("which block:"))
    i=1
    s,s1=std()
    if s==1:
        fr =st1
    elif s==2:
        fr = st2
    elif s==3:
        fr = st3
    if b not in fr :    # checking given (input) block in the from string
        print("\n---INVALID MOVE---\n")
        s,s1=std()
    while i!=0:
        if s==1:
            k=st1.index(b)
            try:
                if st1[k]>st1[k+1]:   # checking whether it is small or big block
                    print("\n---Invalid move---\n")   
                    return blck()
            except:
                pass
        elif s==2:
            k=st2.index(b)
            try:
                if st2[k]>st2[k+1]:     # checking whether it is small or big block
                    print("\n---Invalid move---\n")
                    return blck()
            except:
                pass
        elif s==3:
            k=st3.index(b)
            try:
                if st3[k]>st3[k+1]:         # checking whether it is small or big block
                    print("\n---Invalid move---\n")
                    return blck()
            except:
                pass
        if b in [1,2,3]:
            i=0
            return b,s,s1
        else:
            print("\n----three blocks only available----\n")
            b=int(input("which block:"))
def std():
    s=int(input("from stand:"))
    s1=int(input("to stand:"))
    if s>3 or s1>3:
        if s>3:
            print("\n---INVALID FROM STAND---\n")
        elif s1>3:
            print("\n---INVALID TO STAND---\n")
        s=int(input("from stand:"))
        s1=int(input("to stand:"))
    i=1
    while i!=0:
        if s==s1:
            print("\n---invalid stand---\n")
            s=int(input("from stand:"))
            s1=int(input("to stand:"))
        else:
            i=0
            return s,s1
def hanoi(i):
    while i >0:
        print(f"----you have {i-1} chances left----")
        b,s,s1=blck()
        if s1==1:
                if st1==[]:
                    st1.append(b)
                else:
                    ik =len(st1)
                    if st1[ik-1]<b:
                        print("\n---INVALID MOVE---\n")
                        hanoi(i)   
                    elif st1[ik-1]>b:
                        st1.append(b)
        elif s1==2:
                if st2==[]:
                    st2.append(b)
                else:
                    ik =len(st2)
                    if st2[ik-1]<b:
                        print("\n---INVALID MOVE---\n")
                        hanoi(i)
                    elif st2[ik-1]>b:
                        st2.append(b)
        elif s1==3:
                if st3==[]:
                    st3.append(b)
                else:
                    ik =len(st3)
                    if st3[ik-1]<b:
                        print("\n---INVALID MOVE---\n")
                        hanoi(i)
                    elif st3[ik-1]>b:
                        st3.append(b)
        i-=1
        if i == 1:
            break
        if s==1:
           st1.remove(b)
        elif s==2:
           st2.remove(b)
        elif s==3:
           st3.remove(b)
        print(st1,st2,st3)
        if [3,2,1] == st3:
            print("---YOU WON---")
            break;
        else:
            pass
i=9
hanoi(i)
if fs != st3:
    print("SORRY YOU LOST")


    


      

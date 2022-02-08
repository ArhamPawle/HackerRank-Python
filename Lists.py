if __name__ == '__main__':
    list1=[]
    N = int(input())
    for i in range(N):
        S=input()
        if S[0:3]=="ins":
            last_char=int(S.split(" ")[-1])
            last_char3=int(S.split(" ")[-2])
            list1.insert(last_char3,last_char)
            
        elif S[0:3]=="pri":
            print(list1)
            
        elif S[0:3]=="rem":
            last_char=int(S.split(" ")[-1])
            list1.remove(last_char)
            
        elif S[0:3]=="app":
            last_char=int(S.split(" ")[-1])
            list1.append(last_char)
            
        elif S[0:3]=="sor":
            list1.sort()
            
        elif S[0:3]=="pop":
            list1.pop()
            
        elif S[0:3]=="rev":
            list1.reverse()
            
        
            
            
        
            

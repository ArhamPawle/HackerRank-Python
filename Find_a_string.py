def count_substring(string, sub_string):
    idx=0
    lastidx=0
    count=0
    while idx != -1:
       idx=string.find(sub_string,lastidx) 
       if idx!=-1:
           lastidx=idx+1
           count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

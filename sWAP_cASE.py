def swap_case(s):
    length=len(s)
    copy=""
    for i in range(length):
        if s[i].isupper():
            copy=copy+s[i].lower()
        else:
            copy=copy+s[i].upper()
    
    return copy

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

'''In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.
Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string. '''

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

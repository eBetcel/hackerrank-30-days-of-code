import sys

class Solution:
    # Write your code here
    def __init__(self):
        self.my_stack = []
        self.my_queue = []
    
    def pushCharacter(self, ch):
        self.my_stack.append(ch)
    
    def popCharacter(self):
        return self.my_stack.pop()
        
    def enqueueCharacter(self, ch):
        self.my_queue.append(ch)
    
    def dequeueCharacter(self):
        char = self.my_queue[0]
        self.my_queue = self.my_queue[1:]
        return char
        
        
# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    
#LeetCode: 412 FizzBuzz
#Johnny 12/14/16

class Solution:
    def fizzBuzz(self,n):
        myList = []
        for i in range(1,n+1,1):
            if i%3==0 and i%5!= 0:
                myList.append ("Fizz")
            elif i%3!=0 and i%5== 0:
                myList.append("Buzz")
            elif i%3==0 and i%5== 0:
                myList.append("FizzBuzz")
            else:
                myList.append(str(i))
        return myList

x = Solution()
print x.fizzBuzz(15)
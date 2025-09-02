### Завдання
# Дано ціле число x, повернути, true якщо x це паліндром (перевернуте), та false інакше.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0 and x == int(str(x)[::-1]):
        	palindrom = True
        else:
        	palindrom = False
        return palindrom
        
        
cat = Solution()

print(cat.isPalindrome(121))


#Розвязок від  GPT

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return x >= 0 and x == int(str(x)[::-1])


cat = Solution()
print(cat.isPalindrome(12345))  # False
print(cat.isPalindrome(121))    # True
"""for i in range(1,6):
    for j in range(i):
        print("*", end=" ")
    print()"""
"""lst=[1,2,3,4,2,5,5,6,"a","b","c"]
lst.pop()
print(lst)
lst.append("apple")
print(lst)
lst.insert(2,"banana")
print(lst)
lst.remove(2)
print(lst)
index=lst.index("banana")
print(index)
count=lst.count(5)
print(count)
lst2=[8,4,3,16]
lst2.sort()
print(lst2)
lst2.reverse()
print(lst2)

"""
"""lst1=[10,7,24,15,1]
lst1.sort()
print(lst1)
lst2=lst1[::-1]
print(lst2)"""
"""st1=[1,2,3,4,5]
lst2=lst1[0:4:2]
print(lst2)"""
"""def is_palindrome(s):
    return s==s[::-1]
string="vansh"
if is_palindrome(string):
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")"""
"""def is_prime(n):
    if n<1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=15
if is_prime(n):
    print(f"{n} is a prime number.")
else :
    print(f"{n} is not prime")"""
"""def fibonacci(n):
    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
    print()
fibonacci(10)"""
def sumofdigits(n):
    total=0
    while n>0:
        total+=n%10
        n=n//10
    return total
sum=sumofdigits(123)
print(sum)
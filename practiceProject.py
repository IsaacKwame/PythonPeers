#Thjs program implements the collatz sequence



num = int(input('please enter any integer: '))

#Creating the collatz sequence function
def collatz(n):
    print(n)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            yield(n)
        else:
            n = n * 3 + 1
            yield(n)

#calling the function
print(list(collatz(num)))

  


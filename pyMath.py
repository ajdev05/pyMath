import random
@Method_class
class Math():

    def help(self):
        return"""
        --Methods--
        
        .add(num1,num2) adds 2 numbers

        .divide(num1, num2) divides 2 numbers

        .mul(num1, num2) multiplies 2 numbers

        .sub(num1, num2) subtracts 2 numbers

        .square2(num1) squares a number 2^2

        .squareX(num1, num2) 2^3 or any exponent square root 

        .rand(num1,num2) returns random number from num1 to num2. 2 to 10

        .sqrt(num1) Square root of a number

        .mod(num1,num2) Remander of two numbers

        .isPrime(num1) checks if the number is prime

        mini(num1) returns minimum of a number list

        maxi(num1) returns maximum of a number list


        """

        
    def add(self, num1, num2):
        return num1 + num2

    def divide(self,  num1, num2):
        return num1 / num2

    def mul(self, num1, num2):
        return num1 * num2

    def sub(self,  num1, num2):
        return num1 - num2
    
    def square2(self,num1):
        return num1 *num1

    def squareX(self,num1, num2):
        return num1**num2
    
    def rand(self, num1,num2):
        return random.randrange(num1,num2)

    def sqrt(self, num1):
        return num1 ** .5

    def mod(self,num1,num2):
        return num1 % num2

    def isPrime(self, num1):
        if num1 % 2 ==0:
            return f"Yes, {num1} is Prime"

        else:
            return f"No, {num1} is not Prime"

    def mini(self, num1):
        return min(num1)
    
    def maxi(self,num1):
        return max(num1)
    



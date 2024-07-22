# Multiply Numbers
def multiply_nums(multiplicand, multiplier):
    product = multiplicand * multiplier
    return product
#Divide Numbers
def divide_nums(divident,divisor):
    quotient = divident/divisor
    return quotient

#prompt and take input

print("Part 2 - Multiply and Divide")
prompt = "Enter Number:"
num1 = int(input(prompt))
num2 = int(input(prompt))
print("Performing calculations on", num1,"and", num2)
print("Product of",num1,"and",num2,"is",multiply_nums(num1,num2))
print("Quotient of",num1,"and",num2,"is",divide_nums(num1,num2))

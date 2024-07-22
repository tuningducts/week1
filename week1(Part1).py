#add numbers
def add_nums(addend1, addend2):
    sum= addend1 + addend2
    return sum
#subtract numbers
def subtract_nums(minuend,subtrahend):
    difference = minuend - subtrahend
    return difference

#prompt and take user input
prompt = "Enter Number:"
print("Part 1 - Add and Subtract")
num1 = int(input(prompt))
num2 = int(input(prompt))

#print sum and difference of user input
print("Sum of",num1,"and",num2,"is",add_nums(num1,num2))
print("Difference of",num1,"and",num2,"is",subtract_nums(num1,num2))

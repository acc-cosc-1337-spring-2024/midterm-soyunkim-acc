import question_c

option = "y"

while option != "n":
    num = int(input("Enter a number for its sum of evens: "))
    sum = question_c.get_sum_of_evens(num)
        
    print(sum)

    option = input("Get sum of evens again? (y/n): ")
    
print("Bye!")         
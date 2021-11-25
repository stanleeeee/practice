import math

def get_function():
    func_value = input("Please input the function in the form of ax^n + bx^n + c: ")
    func_list = func_value.split(" ")
    return(func_list)

true_func_list = get_function()
actual_function = []
signs = []
for i in range(len(true_func_list)):
    if i % 2 == 0:
        actual_function.append(true_func_list[i])
        print(actual_function)
    else:
        signs.append(true_func_list[i])

range_0 = int(input("Please input range X0: "))
range_n = int(input("Please input range Xn: "))
intervals = int(input("Please input the NUMBER of intervals: "))

equation = 0

def calculate_y(x_value):
    calculation_total = 0
    for i in range(len(actual_function)):
        temp_term = actual_function[i]
        temp_term_list = temp_term.split("x")
        print(temp_term_list)
        if len(temp_term_list) > 1:
            if temp_term_list[1] != "":
                temp_power_list = temp_term_list[1].split("^")
                print(temp_power_list)
                power = x_value ** int(temp_power_list[1])
                total = power * int(temp_term_list[0])
                calculation_total += total
        if len(temp_term_list) == 1:
            calculation_total += int(temp_term_list[0])
                
    print(calculation_total)
        
    

    
        
        
    

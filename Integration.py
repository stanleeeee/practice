def get_function():
    func_value = input("Please input the function in the form of ax^n + bx^n + c: ")
    func_list = func_value.split(" ")
    return(func_list)

def calculate_y(x_value):
    calculation_total = 0
    for i in range(len(actual_function)):
        temp_term = actual_function[i]
        temp_term_list = temp_term.split("x")
        if len(temp_term_list) > 1 and temp_term_list[0] != "":
            if temp_term_list[1] != "":
                temp_power_list = temp_term_list[1].split("^")
                power = x_value ** int(temp_power_list[1])
                total = power * int(temp_term_list[0])
            else:
                total = x_value * int(temp_term_list[0])
        elif len(temp_term_list) > 1 and temp_term_list[0] == "":
            if temp_term_list[1] != "":
                temp_power_list = temp_term_list[1].split("^")
                total = x_value ** int(temp_power_list[1])
            else:
                total = x_value
        elif len(temp_term_list) == 1:
            total = int(temp_term_list[0])
        if i != 0:
            if signs[i-1] == "+":
                calculation_total += total
            elif signs[i-1] == "-":
                calculation_total -= total
        elif i == 0:
            calculation_total = total
    return calculation_total


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

x_value_list = []
y_value_list = []
for i in range(intervals + 1):
    height = (range_n - range_0)/intervals
    x_values = range_0 + height * i
    x_value_list.append(x_values)

for i in range(len(x_value_list)):
    y_values = calculate_y(x_value_list[i])
    y_value_list.append(y_values)

middle_area = 0
for i in range(len(y_value_list)-1):
    middle_area += y_value_list[i]


total_area = 0.5 * height * ((y_value_list[0] + y_value_list[len(y_value_list)-1]) + 2 * middle_area)
print(total_area)


    
    
    



    
        
    

    
        
        
    

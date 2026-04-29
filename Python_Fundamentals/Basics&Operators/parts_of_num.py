# seperate the integer & Fractional part
num = float(input("Enter the num : "))
fract_part = num - int(num)
int_part = num-fract_part
print("Integer part=",int_part, ", fractionl part=",fract_part)
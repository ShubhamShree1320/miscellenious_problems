def decimal_to_binary(n):
    if n == 0:
        return 0
    else:
        return (n % 2) + 10 * decimal_to_binary(n // 2)



# XOR operation on binary number

number=10 # 1010  #number=1011
number1=11 # 1011 #number1=1010
# print(decimal_to_binary(number))
# print(decimal_to_binary(number^number))

bin_number=decimal_to_binary(number)
bin_number1=decimal_to_binary(number1)
bin_number=bin_number^bin_number1 # ist XOR
bin_number1=bin_number^bin_number1 #2nd XOR
bin_number=bin_number^bin_number1 #3rd XOR

print(f"Swapped Numbers are {bin_number} and {bin_number1}")

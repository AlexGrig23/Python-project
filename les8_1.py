try:
    digit = float(input("Enter digit: "))
    conv_digit = int(digit)
    print(conv_digit)
except ValueError as error:
    print(error)
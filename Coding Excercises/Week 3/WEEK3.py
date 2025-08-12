# WEEK 3
# ISBN Language reader
# Abby wants the code to determine language by ISBN
# ISBN comes in 10 digits and 13 digits, subtract 9780000000000 in order to convert 13 digit to 10 digit, otherwise dont
# ISBN 0 to 1999999999 ouput English
# ISBN 2000000000 to 2999999999 output French
# ISBN 3000000000 to 3999999999 output German
# ISBN 4000000000 or Higher output Unknown

ISBN_value = int(input("ISBN : "))
if ISBN_value >= 9780000000000 and ISBN_value <= 9789999999999  :
    ISBN_value = ISBN_value - 9780000000000
    if ISBN_value >= 0 and ISBN_value <= 1999999999             :
        print('English')
    elif ISBN_value >= 2000000000 and ISBN_value <= 2999999999  :
        print('French')
    elif ISBN_value >= 3000000000 and ISBN_value <= 3999999999  :
        print('German')
    elif ISBN_value >= 400000000                                :
        print('Unknown')
else:
    if ISBN_value >= 0 and ISBN_value <= 1999999999             :
        print('English')
    elif ISBN_value >= 2000000000 and ISBN_value <= 2999999999  :
        print('French')
    elif ISBN_value >= 3000000000 and ISBN_value <= 3999999999  :
        print('German')
    elif ISBN_value >= 400000000                                :
        print('Unknown')
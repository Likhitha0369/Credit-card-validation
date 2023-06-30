# Credit card validator program using python
# steps:
# 1. Remove any '-' or ' '
# 2. Add all digits in the odd places from right to left
# 3. Double every even place digit from right to left
#      (If result is a two digit number, add the two digit number together to get single digit)
# 4. Sum the totals of step 2 and 3
# 5. If mod of result is 0, then the credit card is valid

sum_odd_digits = 0
sum_even_digits = 0
total = 0

# step1
card_number = input("Enter a credit card #:")
card_number = card_number.replace("-","")
card_number = card_number.replace(" ","")
card_number = card_number[::-1]

# step2
for x in card_number[::2]:
    sum_odd_digits += int(x)

# step3
for x in card_number[1::2]:
    x=int(x) * 2
    if x>=10:
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += x

# step4
total = sum_odd_digits + sum_even_digits

# step5
if total % 10 == 0:
    print("VALID")
else:
    print("INVALID")

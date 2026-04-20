digits = input("Enter a decimal: ")
n = float(digits)

# Seperates from decimal.
if "." in digits:
    exponent = len(digits.split(".")[1])
else:
    exponent = 0

numerator = int(round(n * 10**exponent))
denominator = 10**exponent

# Start from the smaller of the two and count down to 1/
limit = min(numerator, denominator)
factor = 1

# Only goes to the smaller of two, bc higher then that is redundant.
for test_factor in range(limit, 0, -1):
    if numerator % test_factor == 0 and denominator % test_factor == 0:
        factor = test_factor
        # Exit immediately when GCF is found.
        break

num = numerator // factor
den = denominator // factor

print(f"The fraction is {num} / {den}")
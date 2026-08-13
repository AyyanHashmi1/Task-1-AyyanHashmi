import string

password = input("Enter your password: ")

length = len(password)
has_number = any(char.isdigit() for char in password)
has_uppercase = any(char.isupper() for char in password)
has_symbol = any(char in string.punctuation for char in password)

score = 0

if length >= 8:
    score += 1

if has_number:
    score += 1

if has_uppercase:
    score += 1

if has_symbol:
    score += 1

if score <= 1:
    strength = "Weak"
elif score == 2 or score == 3:
    strength = "Medium"
else:
    strength = "Strong"

print("\nPassword Strength:", strength)

print("\nDetails:")
print("Length:", length)
print("Contains number:", has_number)
print("Contains uppercase letter:", has_uppercase)
print("Contains symbol:", has_symbol)
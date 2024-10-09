import re


def normalize_phone(phone_number):
    number_cleared = "".join(re.findall(r"[\+\d]", phone_number))
    pattern = r"(\+)?(38)?(\d+)"
    match = re.match(pattern, number_cleared)

    if match:
        plus_sign = match.group(1)
        ua_code = match.group(2)

        if plus_sign and ua_code:
            return number_cleared
        elif ua_code:
            return f"+{number_cleared}"
        else:
            return f"+38{number_cleared}"


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:")
for num in sanitized_numbers:
    print(num)


# print(normalize_phone("(050)8889900"))

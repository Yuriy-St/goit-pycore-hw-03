import random

def get_numbers_ticket(min, max, quantity):
    try:
        if min < 1:
            raise Exception("'min' must be greater or equal to 1")
        if max <= min:
            raise Exception("'max' must be greater than 'min'")
        if quantity < min or max < quantity:
            raise Exception("'quantity' must lay in the (min, max) range")

        result = random.sample(range(min,max + 1), quantity)
        return sorted(result)
    except Exception as e:
        print(e)

print(get_numbers_ticket(1, 39, 6))

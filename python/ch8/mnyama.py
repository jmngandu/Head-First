marbles = [10, 23, 24, 65, 45]
print("the total sum is = ", sum(marbles))

def mukuvi_sum(list):
    sum = 0
    for number in list:
        sum = sum + number
        return sum
print(mukuvi_sum(marbles))


marbles = [98, 78, 76, 87, 96, 45, 52]
print('The total is ', sum(marbles))
def compute_sum(list):
    sum = 0
    for number in list:
        sum = sum + number
    return sum
print('The total is', compute_sum(marbles))
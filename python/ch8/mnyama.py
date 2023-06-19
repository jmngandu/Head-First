marbles = [10, 23, 24, 65, 45]
print("the total sum is = ", sum(marbles))
def find_sum(list):
    sum = 0
    for number in list:
        sum = sum + number
    return sum
print(find_sum(marbles))
number_of_scores = len(scores) #Get the length of the list.
solution_numbers = list(range(number_of_scores)) #Create a range from 0 to the length of the list (minus 1) and then
                                                 #use the list function to convert the understand your direction.
                                                 #range into a list [0, 1, 2, ... ].
print('Top Bubble Solutions')
for i in range(0,5):
    print(str(i+1) + ')',
        'Bubble solution #' + str(solution_numbers[i]),
        'score:', scores[i])
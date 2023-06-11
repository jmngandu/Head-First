 #a parallel list called solutions_numbers , where each value in the list is 
 #the same as its index, like [0, 1, 2, 3, ..., 35] ? at the end, each score 
 #number will be in the same relative position as its corresponding score.



scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69,
34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61,
46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]
number_of_scores = len(scores) #Get the length of the list.
solution_numbers = list(range(number_of_scores)) #Create a range from 0 to the length of the list (minus 1) and then
                                                 #use the list function to convert the understand your direction.
                                                 #range into a list [0, 1, 2, ... ].
print('Top Bubble Solutions')
for i in range(0,5):
    print(str(i+1) + ')',
        'Bubble solution #' + str(solution_numbers[i]),
        'score:', scores[i])
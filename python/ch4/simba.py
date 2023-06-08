high_score = 0
length = len(scores)
for i in range(length):
print('Bubble solution #' + str(i), 'score:', scores[i])
if scores[i] > high_score:
high_score = scores[i]
print('Bubbles tests:', length)
print('Highest bubble score:', high_score)
best_solutions = []
for i in range(length):
if high_score == scores[i]:
best_solutions.append(i)
print('Solutions with the highest score:'
scores = [60, 50, 60, 58, 54, 54,58, 50, 52, 54, 48, 69,
34, 55, 51, 52, 44, 51,69, 64, 66, 55, 52, 61,
46, 31, 57, 52, 44, 18,41, 53, 55, 61, 51, 44]
high_score = 69
i = 0 
length = len(scores)
for i in range(length):
    if high_score == scores[i]:
        print(high_score)
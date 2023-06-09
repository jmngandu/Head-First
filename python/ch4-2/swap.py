def bubble_sort(scores):
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, len(scores)-1):
            if scores[i] > scores[i+1]:
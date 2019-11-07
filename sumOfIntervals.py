def sum_of_intervals(intervals):
    sort(intervals, 0, len(intervals) - 1)
    sum = 0
    for i in range(len(intervals) - 1):
        if intervals[i + 1][0] <= intervals[i][1]:
            if not intervals[i + 1][1] < intervals[i][1]:
                sum += intervals[i + 1][1] - intervals[i][0]
                intervals[i + 1] = (intervals[i][0], intervals[i + 1][1])
            else:
                intervals[i + 1] = (intervals[i][0], intervals[i][1])
        else:
            if sum is 0:
                int1 = intervals[i + 1][1] - intervals[i + 1][0]
                int2 = intervals[i][1] - intervals[i][0]
                sum += int1 + int2
            else:
                sum += intervals[i + 1][1] - intervals[i + 1][0]

    return sum


def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high][0]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j][0] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index

# Function to do Quick sort
def sort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        sort(arr, low, pi - 1)
        sort(arr, pi + 1, high)


if __name__ == '__main__':
    arr = sum_of_intervals([
        (1, 4), (7, 10), (3, 5)
] )

    print(arr)
#
# [
#    [1,2],
#    [6, 10],
#    [11, 15]
# ]

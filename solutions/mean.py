number = int(input("How many numbers would you like to input?: "))


def create_list(nm):
    values = []
    while nm != 0:
        values.append(int(input("Enter a value: ")))
        nm -= 1
    return values


def sum_arr(arr):
    sum = 0
    for i in arr:
        sum += arr[i]
    return sum


def mean(dividend, divisor):
    return float(dividend)/divisor


values = create_list(number)
print("Values of list: " + str(values))

sumt = sum_arr(values)
print("Sum of list: " + str(sumt))

mean = mean(sumt, number)
print("Mean of list: " + str(mean))

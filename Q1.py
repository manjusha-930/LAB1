numbers = [2, 7, 4, 1, 3, 6]
# Variable to count the pairs
count_pair = 0
# Loop to find pairs
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == 10:
            count_pair += 1
print("Number of pairs with sum equal to 10:", count_pair)

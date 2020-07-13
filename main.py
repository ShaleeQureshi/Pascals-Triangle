rowNum = int(input("What row would you like to go up to?\n")) # Getting the amount of rows that the user would like to view

list = []  # Declaring an empty list

# for loop to iterate through each row
for row in range(rowNum):
    list2 = []  # list2 acts as a temporary list
    
    # for loop to iterate through each column
    for col in range(row + 1):
        # if the column is at index 0 or at the final index the value will be 1
        if (col == 0 or col == row):
            list2.append(1)  # Adding 1 to the list
        # if the column index is not 0 or the end the values will be determined by adding the two above
        else:
            list2.append(list[row - 1][col - 1] + list[row - 1][col]) # Adding the values to the list
    list.append(list2) # Adding the temp-list values to the list

# for loop to iterate through each row   
for row in range(rowNum):
    # for loop to iterate through each column and add a space accordingly (row 1 will have 4 spaces from the left, row 2 will have 3, etc)
    for col in range(rowNum - row - 1):
        print(" ", end="")
    for col in range(row + 1):
        print(list[row][col], end=" ")
    print()

print("\nThank you for using Shahrukh Qureshi's Pascal's Triangle Program!")
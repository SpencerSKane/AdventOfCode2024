# Initialize three empty lists
# Two for columns and one for distances
column1 = []
column2 = []
distanceList = []

# Open the txt file
with open('input_1.txt', 'r') as file:
    for line in file:
        # Split the line into two parts based on spaces (taking into account the 3 spaces)
        parts = line.split('   ')  # Split by 3 spaces
        if len(parts) == 2:
            # Append the values to the respective lists, cast to an int
            column1.append(int(parts[0].strip()))  # Remove any leading/trailing whitespace
            column2.append(int(parts[1].strip()))
            
# sort() will sort from least to greatest
# this method sorts in-place (modifies the original list directly)
column1.sort()
column2.sort()

# with zip we can iterate along both columns
for i,j in zip(column1, column2):
    distanceList.append(abs(i - j))

# Print the lists to check the output
print(column1[:10])  # Print first 10 elements for checking
print(column2[:10])  # Print first 10 elements for checking
print(distanceList[:10])  # Print first 10 elements for checking

print(sum(distanceList))  # Print the solution to Day 1's Challenge


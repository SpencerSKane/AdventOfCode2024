# Initialize three empty lists
column1 = []  # list for column
column2 = []  # list for column
distanceList = []  # list of all distances

similarityScore = 0
count = 0

# Open the txt file
with open('input_1.txt', 'r') as file:
    for line in file:
        # Split the line into two parts based on spaces (taking into account the 3 spaces)
        parts = line.split('   ')  # Split by 3 spaces
        if len(parts) == 2:
            # Append the values to the respective lists, cast to an int
            column1.append(parts[0].strip())  # Remove any leading/trailing whitespace
            column2.append(parts[1].strip())
            
# sort() will sort from least to greatest
# this method sorts in-place (modifies the original list directly)
column1.sort()
column2.sort()

# zip is used to iterate along both columns
for x,y in zip(column1, column2):
    dist = int(x) - int(y)
    distanceList.append(abs(dist))

# below could be optimized with a hash map
for i in column1:
    count = 0
    for j in column2:
        if i == j:
            count += 1
    similarityScore += count * int(i)

# Print the lists to check the output
print(column1[:10])  # Print first 10 elements
print(column2[:10])  
print(distanceList[:10])  

# sum and print solutions
print(sum(distanceList))  
print(similarityScore) 

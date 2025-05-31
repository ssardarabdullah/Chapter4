cubes = []  # Empty list to store cubes

for number in range(1, 11):  # Loop from 1 to 10
    cube = number ** 3       # Calculate the cube
    cubes.append(cube)       # Add the cube to the list

print(cubes)
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
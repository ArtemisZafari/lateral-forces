# ENTER ALL INPUTS BELOW
# Note: for all inputs that describe multiple floors, always input the data
# from the top floor down. Similarily, all inputs related to shearwall layers
# should be inputted left to right (Y-Y direction) and top to bottom (X-X direction)

# Enter the name for the project (this will be the Word title)
project_name = 'Sinner'

# Enter the file location for the report to be saved
save_location = 'C:\\Users\\artyp\\Desktop\\Lateral Script\\'

# Use styling below for Ubuntu (don't forget to comment-out the Windows version)
# save_location = '/home/artemis/Documents/'

# Enter the roof pitch of the house in units of degrees
# (if there are multiple, choose the steepest one)
roof_pitch = 23

# Enter the number of floors
floors = 2

# Enter the lengths of the floor for both direction faces
floor_lengths_x = [48, 58]

floor_lengths_y = [37, 37]

# Enter the areas of A, B, C, and D for each floor in each direction
floor_areas_x = [60, 65, 330, 9,
               212, 0, 374, 0]

floor_areas_y = [77, 144, 134, 206,
               140, 0, 230, 0]

# Enter the Kzt value (default is 1.2)
kzt = 1.2

# Enter the wind speed in units of mph (default is 110)
wind_speed = 110

# Enter the wind exposure lambda factor (default is 1.0)
wind_exposure = 1.0

# Enter the area of each floor
floor_areas = [1831,
               2270]

# Enter the height of each floor plate
floor_plates = [21,
               12]

# Enter the minimum wall and roof factors in units of psf (default is 16 and 8)
min_wall = 16
min_roof = 8

# Enter the values of each dead load
roof_DL = 13
floor_DL = 13
wall_DL = 8

# Enter the value of rho
rho = 1.3

# Enter the value of Cs
cs = 0.16

# Enter the load factor
quake_factor = 0.7

# Enter the floor heights
floor_heights = [8, 10]

# Enter the number of shear wall layers in each floor in both directions
shear_layers_x = [2, 4]

shear_layers_y = [2, 2]

# Enter the distances between the shear wall layers
# for each floor in both directions (if either edge layer has
# "overhang" distance, that will be taken care of in the next input)
distances_x = [[41], [10, 30, 11]]

distances_y = [[37], [37]]

# Enter the "overhang" distance for the first
# and last layer (in that order) of each floor in both directions
# (note that the default is zero, i.e. no "overhang" distance).
# Overhang distance is when there is some length that needs to be considered
# beyond the first or last shear layer, such as when a fireplace sticks out
# 2 feet from the wall of a house.
overhang_dist_x = [[0, 7], [0, 7]]

overhang_dist_y = [[0, 0], [0, 0]]

# Enter offset distances (the value for the top floor, or first list item, should always be zero).
# Offset distance is defined as the distance between the first shear layer of a floor 
# and the first shear layer of the floor above it. This is measured positive to the right
# (Y-Y direction) and positive downwards (X-X direction)
offset_dist_x = [[0], [-10]]

offset_dist_y = [[0], [0]]

# Enter the lengths of all the shear wall segments
# within the shear wall layers for each floor in both directions
shear_layer_lengths_x = [[[7, 6.66], [8, 5.5, 3, 3]],
                         [[4], [6.75, 2.66], [9], [5, 3.5, 3.75, 3.75]]]

shear_layer_lengths_y = [[[9.66, 13.5], [8, 7.5, 3.66]],
                         [[7.5, 16], [12, 5.66, 6.5, 13]]]

# END OF INPUT ENTRY
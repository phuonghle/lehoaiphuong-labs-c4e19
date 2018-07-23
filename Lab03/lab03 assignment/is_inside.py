#  Write a function named is_inside that checks if a point is inside a rectangle, 
# takes 2 parameters, the first is a list with 2 elements respectively represents x and y coordinates of the given point, 
# the second is a list with 4 elements respectively represents x, y coordinates and width height of the given rectangle




def is_inside(point, rec):
    if point[0] in range(rec[0], rec[0] + rec[2]):
        if point[1] in range(rec[1], rec[1] + rec[3]):
            return True 
    else:
        return False


print(is_inside([100, 120], [140, 60, 100, 200]))
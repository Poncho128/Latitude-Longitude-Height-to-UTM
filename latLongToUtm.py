import utm
import sys

#Should receive the lat_long_height checkpoints file as the first parameter, the output file as the second parameter and the height offset as a third parameter

file_object = open(sys.argv[1])

fh = open(sys.argv[2],'w')
    

my_list = file_object.read().split(',')

list_length = len(my_list)

for x in range(0, list_length/3):
    print(utm.from_latlon(float(my_list[(x*3)]), float(my_list[(x*3)+1])))
    print(float(my_list[(x*3)+2])-float(sys.argv[3]))

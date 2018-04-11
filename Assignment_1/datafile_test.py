######################################
#
# Name: Intro to Python Assignment
#
# Created by: John Ocker
#
# Assisted by: Documentation on Canvas
#
# Purpose: Reads in a data set from a .txt
#       file, then outputs various attributes
#       of the data. Requires a data file to be
#       read. User can change the value to be
#       found in the data by changing the
#       variable 'value' in the code.
#
######################################

# System requirements
from collections import Counter

# Reads in the file and stores data in 'b'
with open('datafile.txt','r') as f:
    b = eval(f.read())
f.close

# variable to be found in the data
value = 38 #ADJUSTABLE

#####################################
# Finds the maximum value in the data
#####################################
maximum = max(b)
print "Maximum: ", maximum, '\n'

#####################################
# Finds the minimum value in the data
#####################################
minimum = min(b)
print "Minimum: ", minimum, '\n'

#####################################
#Attempts to find the specified value inside the value.
#####################################
try:
    # If the value is found, return the index
    location = b.index(value)
    print "The index of the value", value, " is ", location, '\n'
except:
    # If value is not found, inform the user.
    print "Entered value is not in data.\n"
    
#####################################
# Creates a list of the most common elements in that data
#####################################
most_common_decending= Counter(b).most_common()
i = most_common_decending[0][1]
print "Most common element(s):"
# Iterates through most_common_decending until it reaches
# a element that repeated less times than the maximum,
# printing each as it goes to the terminal.
for a in most_common_decending:
    if a[1] < i:
        break
    else:
        print "   ", a[0]
print "Number of times repeated: ", i, '\n'

#####################################
# Sorts the list numerically
#####################################
print "Sorted List: "
sorted_list = sorted(b)
print sorted_list, '\n'

#####################################
# Creates a new list of all the even elements
# in the original list.
#####################################
print "List of Even Numbers: "
even_nums = []
for a in sorted_list:
    if a%2 == 0: #and a not in even_nums:
        even_nums.append(a)
print even_nums

# End

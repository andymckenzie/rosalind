#initial progression give n = 5, offspring_ratio = 3
#1
#1
#4
#7
#19

#the number of offspring in any month is equal to the number of rabbits that were alive two months prior
number_of_months = 5
offspring_ratio = 3

#assume zero rabbits in month 0
number_of_rabbits_list = [0]
current_number_of_rabbits = 1 
for i in xrange(0, number_of_months):
    new_rabbits = number_of_rabbits_list[i-1] * 3
    print new_rabbits
    current_number_of_rabbits += new_rabbits
    number_of_rabbits_list.append(current_number_of_rabbits)
    
print number_of_rabbits_list
print current_number_of_rabbits
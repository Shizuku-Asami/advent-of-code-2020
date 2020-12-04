from pprint import pprint
import re

f = open("input2.txt", "r")
r = f.readlines()
#print(r)
data = [i.split() for i in r]
#pprint(data)

true_array = []
false_array = []
array = []
log = []

true_array_2 = []
false_array_2 = []
array_2 = []

def validate_2(low, high, must_contain, password):
    if (password[low-1] == must_contain) & (not (password[high-1] == must_contain)):
        return True
    elif (not (password[low-1] == must_contain)) & (password[high-1] == must_contain):
        return True
    else:
        return False


for i in r:
    m = re.search('\d-\d', i.split()[0])
    x = re.sub('-', ' ', m.string)
    #print(x)
    num_pol = x.split()
    #print(num_pol)
    lowest_number = int(num_pol[0])
    highest_number = int(num_pol[1])
    #print(highest_number)
    found_text = re.findall(i.split()[1], i.split()[2])
    #print(found_text)
    if (lowest_number <= len(found_text) <= highest_number ):
            true_array.append(True)
            array.append(True)
    else:
        false_array.append(False)
        array.append(False)

    if validate_2(lowest_number, highest_number, i.split()[1], i.split()[2]):
        true_array_2.append(True)
        array_2.append(True)
    else:
        false_array_2.append(False)
        array_2.append(False)



# print(array)

#print(len(data))
#print(len(true_array))
#print(len(false_array))
#print(len(true_array)+len(false_array))
#print(len(data) - len(array))


print(len(true_array_2))
print(len(array_2))
print(array_2)

# print(data[-6])
# print(re.findall(data[-6][1], data[-6][2]))
# print(2 <= len(re.findall(data[-6][1], data[-6][2])) <= 7)

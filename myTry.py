# attempt to write selection sort algorithm

def select_sort(arr):
    for i in range (0,len(arr)):
        cur_min=i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[cur_min]:
                cur_min = j

        arr[cur_min],arr[i] = arr[i] ,arr[cur_min]
    

# my function

def my_idea_with_min(arr):
    temp = []
    while len(arr)>0:
        temp.append(min(arr))
        arr.remove(min(arr))
    return temp

# for fun - god knows why

def find_max(arr):
    max_num = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
    return max_num

# examples ----------------------------

arr1 = [450,12,43,654,76,43,567,978,534,567,987,345,567895,3645,253,34]
arr2 = [45,56,56,3,2,1,45,415,48,57,44,5,89,58,6,546,84,83,5,5686,458,5,4521]
arr3 = ["x","f","h","l","a","d","c","b"]

# WHY it returns [] when called like 1st, but when called as assign to var it is ok
# probable answer - IMMUTABLE vs MUTABLE types
select_sort(arr1)               # works fine
my_idea_with_min(arr2)          # returns []
arr3 = my_idea_with_min(arr3)   # works fine

print(arr1)
print(arr2)
print(arr3)
print(find_max(arr1))

# catch index and object from list at the same time
for i ,j in enumerate(arr1):
    print(f"{i} and {j}") # prints 0 and 12 ; 1 and 34 ....


# optional parameters should be defined in function;
# if youassigne value it will be use as default if not given

def my_function(x, y = 0):
    print(x+y)

my_function(1) # prints 1
my_function(1, 4) # prints 5


# *ARGS allows function to take as many parameters as we want
# and stores them in tuple
def my_function2(x, y, *args):
    print(x,y, args)

my_function2(1,2,3,4,5,6,7,8,9) 
# prints 1 2 (3, 4, 5, 6, 7, 8, 9)

# **KWARGS allows function to take as many keyword parameters as we want
# and stores them in dictionary
def my_function3(**kwargs):
    print(kwargs)
    print(kwargs["x"])

my_function3(x = 1, y ="Bobby" , z = True) 
# prints {'x': 1, 'y': 'Bobby', 'z': True} ; 1


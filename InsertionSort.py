#https://www.youtube.com/watch?v=R_wDA-PmGE4&list=PLliXbzY3XhUSJy3izXH-0ojiT3Uup8xbu
#Insertion Sort In Python - FelixTechTips

def insertion_sort(arr):
    for i in range(1,len(arr)):
        j=i
        while arr[j-1] > arr[j] and j>0:
            arr[j-1], arr[j] = arr[j],arr[j-1]
            j -= 1
    return arr    

arr1 = [2,6,7,1,12,4,8,9]
arr2 = [245,36,75,71,1992,44,83,92]
arr3 = ["x","f","h","l","a","d","c","b"]
arr4 = ["Hubert","Alina","Weronika","Bartosz","Igor","Wojciech","Celina"]

print(insertion_sort(arr1))
print(insertion_sort(arr2))
print(insertion_sort(arr3))
print(insertion_sort(arr4))
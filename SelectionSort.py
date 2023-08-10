#https://www.youtube.com/watch?v=ee80YmiaSVQ&list=PLliXbzY3XhUSJy3izXH-0ojiT3Uup8xbu&index=2
#Selection Sort In Python - FelixTechTips

def selection_sort(arr):
    for i in range(0,len(arr)-1):
        cur_min_inx = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[cur_min_inx]:
                cur_min_inx = j
        
        arr[i] , arr[cur_min_inx] = arr[cur_min_inx] , arr[i]   #swap
    return arr


arr1 = [4,6,8,3,15,2,1,9,22]
arr2 = [245,36,75,71,1992,44,83,92]
arr3 = ["x","f","h","l","a","d","c","b"]
arr4 = ["Hubert","Alina","Weronika","Bartosz","Igor","Wojciech","Celina"]

print(selection_sort(arr1))
print(selection_sort(arr2))
print(selection_sort(arr3))
print(selection_sort(arr4))

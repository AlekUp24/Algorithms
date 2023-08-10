#https://www.youtube.com/watch?v=cVZMah9kEjI&list=PLliXbzY3XhUSJy3izXH-0ojiT3Uup8xbu&index=3
#Merge Sort In Python - FelixTechTips

# HINT : COMPLICATED - WILL GET BACK TO IT SOON

def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge
        i = 0 # left_arr idx
        j = 0 # right_arr idx
        k = 0 # merged array idx
        
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k +=1
        
        # when left has only one element left
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        # when right has only one element left
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    return arr

arr1 = [1,5,6,23,5,78,9,67,121,3,4,5,6]

print(merge_sort(arr1))

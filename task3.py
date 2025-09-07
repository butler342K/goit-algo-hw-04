import pandas as pd
import kagglehub
import timeit

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


# шлях до датасету з масивом даних
path = kagglehub.dataset_download("iamsouravbanerjee/house-rent-prediction-dataset")
df = pd.read_csv(path + "/House_Rent_Dataset.csv")

#Isertion sort
insertion_sort_time = timeit.timeit("insertion_sort(df['Rent'].tolist())", globals=globals(), number=10)
print(f"Insertion sort  10 times: {insertion_sort_time} seconds")

#Merge sort
merge_sort_time = timeit.timeit("merge_sort(df['Rent'].tolist())", globals=globals(), number=10) 
print(f"Merge sort  10 times:     {merge_sort_time} seconds")

#Tim sort
tim_sort_time = timeit.timeit("sorted(df['Rent'].tolist())", globals=globals(), number=10)
print(f"Tim sort  10 times:       {tim_sort_time} seconds")


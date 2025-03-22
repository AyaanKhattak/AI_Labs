def bubble(arr):
    arr=arr.copy()
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def selection(arr):
    arr=arr.copy()
    for i in range(len(arr)):
        min_idx=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr

def insertion(arr):
    arr = arr.copy()
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
            arr[j+1]=key
    return arr

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result

def merge_sort(arr):
    arr = arr.copy()
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

if __name__ == "__main__":
    original_list = ['P', 'Y', 'T', 'H', 'O', 'N']

    bubble_result=bubble(original_list)
    print("Bubble Sort Result:   ", bubble_result)

    selection_result = selection(original_list)
    print("Selection Sort Result:", selection_result)

    insertion_result = insertion(original_list)
    print("Insertion Sort Result:", insertion_result)

    merge_result = merge_sort(original_list)
    print("Merge Sort Result:    ", merge_result)

    print("\nOriginal list remains unchanged:", original_list)

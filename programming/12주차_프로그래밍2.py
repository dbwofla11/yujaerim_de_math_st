def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for k in range(0 , n-i-1):
            if lst[k] > lst[k+1]:
                lst[k] , lst[k+1] = lst[k+1] , lst[k]

lst = [64,34,25,12,22,11,90]
print("오리지널 리스트 : %s" % lst)

bubble_sort(lst)
print("정렬된 리스트 <버블정렬> : ")
print(lst)
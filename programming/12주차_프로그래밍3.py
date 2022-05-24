#알고리즘 기초 <탐색과 정렬> - inserting sort
def insert_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        k = i - 1 

        while k >= 0 and key < lst[k]:
            lst[k + 1] = lst[k]
            k -= 1 
        lst[k+1] = key

lst=[12,11,13,5,6]
print("오리지널 리스트 : %s" % lst)
insert_sort(lst)
print("정렬된 리스트 : ")
print(lst)
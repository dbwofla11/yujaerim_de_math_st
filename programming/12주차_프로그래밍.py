#알고리즘 기초 <탐색과 정렬>

def select_sort(lst):
    for i in range(len(lst)):
        min_idx = i
        for k in range(i+1 , len(lst)):
            if lst[min_idx] > lst[k]:
                min_idx = k
        lst[i] , lst[min_idx] = lst[min_idx] , lst[i]

lst = [64,25,12,22,11]
print("오리지널 리스트는 : %s" % lst)

select_sort(lst)
print("정렬된 리스트 출력")
print(lst)        
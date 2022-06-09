# 선택정렬
def select(list):
    for i in range(len(list)):
        max_idx = i
        for k in range(i + 1 , len(list)):
            if list[max_idx] < list[k]:
                max_idx = k #  max인덱스 동기화 
            list[k] , list[max_idx] = list[max_idx] , list[k]
# 선택정렬은 최대 인덱스나 최소인덱스를 기본값 i로 잡은다음에 이를 갱신해주는 식으로 비교하고 스와핑 
# 이거는 내림차순 정렬 물론 list = sorted(list , reverse = True) # 이렇게 지정해도 내림차순이 됨 

# 버블정렬 
def bubble(list):
    for i in range(len(list)):
        for k in range(0 , len(list) - 1 - i ) # 이것역시 속도를 빠르게 하기위해서 이렇게 지정해줌
            if list[k] > list[k+1]:
                list[k] , list[k+1] = list[k+1] , list[k]  # 이러면 오름차순으로 리스트가 정렬됨 # 만약에 같은 숫자가 리스트에 있더라도 무시하고 지나감
# 버블정렬은 필터가 리스트위를 다닌다고 생각하고 필터에 따라 거품이 올라오는 식으로 정렬된다는 것을 알고 있자 

# 퀵정렬 
def quick(list):
    if len(list) <= 1: return list
    left , middle , right = [x for x in list if x < list[-1]] , [x for x in list if x == list[-1]] , [x for x in list if x > list[-1]]
    return quick(left) + middle + quick(right)


xs = [3,1,2]
xs[2] = "문자열" # 리스트 내에서는 다른 자료형도 같이 들어가는것이 가능 

i = xs.index(3) # 리스트내의 요소를 안에 입력하면 인덱스를 반환함 / 출력 0 
print(i)

xs.count(3) # 리스트내의 요소가 몇번 나오는지 체크 count

nums = [int(x) for x in range(5)] # range로 리스트는 0부터 시작함 
print(nums)

nums2 = [int(i) for i in range(1,5)] # 1~5  # 1부터 "5전" 까지 생성 
print(nums2)

x = [1,2,3,4,5]
num3 = [int(i) for i in x if (i % 2 != 1)] # 이렇게 if문도 안에 넣어서 생성가능 


dic = { "k1":"v1" , "k2":"v2" , "k3":"v3" }
print(dic.values())   # values()를 하면 딕셔너리 내의 value값이 다 나옴 
print(dic.keys())  # keys()를 사용하면 딕셔너리 내의 key값이 다 나옴 


# 파일 열기 
with open("파일이름" , "r") as f:
    print(f.read())
# 이런식으로 with를 써서 파일을 열 수 있다. 읽을 때는 read()를 사용한다. 


# try except문 복습하기 
try:
    print("try")
except TypeError:
    print("타입에러")


# 예외가 발생하지 않았을때 else를 써서 코드를 실행시킴 
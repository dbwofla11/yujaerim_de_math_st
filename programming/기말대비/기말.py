#문자열 
sentence = "나는 소년입니다"
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)

jumin = "990120-1234567"


print("성별 : ", jumin[7:8])
print("년도 : ", jumin[0:2])
print("월   : ", jumin[2:4])
print("일   : ", jumin[4:6])
print("생년월일:" , jumin[:6]) # 처음부터 6직전까지 가져오는거 

print("뒤 7자리 : " , jumin[7:]) # 7부터 끝까지 슬라이싱 
print("뒤 7자리 : (뒤에서 부터)" , jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지 1234567 

# 주의
print("실험 " , jumin[:-7] ) # 그냥 0부터 7자리까지 나옴 (이런경우 그냥 -7이 정수처리)



# 문자열 처리 함수 
a = "Python is Amazing"
print(a.lower())
print(a[0].isupper()) # 문자열의 첫번째 요소가 대문자인가?
print(len(a))
print(a.replace("Python", "Java"))

i = a.index("n")
print(i)
i = a.index("n" , i + 1) # 앞의 n을 찾고 그 뒤에있는 n을 찾는거  # 뒤에 있는 n의 인덱스가 나옴 
print(i)

print(a.find("n"))   # 원하는 값이 없으면 -1 index는 오류가 뜬다. 

print(a.count("n")) # 몇번 나오는지 확인하는거 



# 문자열 포맷 
print("a" + "b")
print("a","b") # 콤마를 써서 한 칸 뛰어서 나온다.

print("나는 {1}과 {0}를 좋아해요" .format("빨강" , "파랑")) # {}안에 인덱스를 넣으면 그 인덱스 대로 출력된다. 

s = [10,20,30]
s1 = ["red","blue","yellow"]
print(s)

print(s.index(20))

#print(s.find("red")) # find 함수는 문자열만 가능하다 
print(s1.index("red")) # 얘는 됨 



#딕셔너리 연습 

a = {1:"유재석" , 2:"김태호" , 3:"강우빈"}
print(a.get(2)) # 사전의 2번을 출력 

print(a.get(4, "사용가능")) # 4번 방이 사전에 없으면 여기에 메시지가 뜸 / 그렇다고 딕셔너리에 추가되는건 아님 

del a[1] # 1번 방을 없앰 
a


# 리스트 함축 
s_list = [int(x) for x in range(1,10)]
print(s_list)
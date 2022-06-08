import matplotlib as plt 
import numpy as np 

x = np.arange(0 , 3*np.pi , 0.1) ## 단순 배열이 아닌 np내 range로 설정해 x를 설정  
y = np.sin(x)   # np내에 pi랑 sin , cos 이 내장되있는걸 확인할 수 있다. 

plt.plot(x,y)
# plt는 일반 파이썬에서는 작동을 안함 그래서 jupyter_notebook에서 해야함 

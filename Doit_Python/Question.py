#Q1
# a:b:c:d ->a#b#c#d
a="a:b:c:d"
b=a.split(':')[0]+'#'+a.split(':')[1]+'#'+a.split(':')[2]+'#'+a.split(':')[3]+'#'
print(b)

# 다른 풀이
bb=a.split(":")
>>> bb=a.split(":")
>>> bb
['a', 'b', 'c', 'd']
>>> c="#".join(bb)
>>> c
'a#b#c#d'

#Q2
a={'A':90, 'B':80}
a.get('C', 70) #딕셔너리의 get 함수를 사용하면 해당 key가 없을 경우에는 두 번째 매개변수로 전달된 default 값을 대신 돌려준다.

#Q3
다음과 같은 리스트 a가 있다.

>>> a = [1, 2, 3]
리스트 a에 [4, 5]를 + 기호를 사용하여 더한 결과는 다음과 같다.

>>> a = [1, 2, 3]
>>> a = a + [4,5]
>>> a
[1, 2, 3, 4, 5]
리스트 a에 [4,5]를 extend를 사용하여 더한 결과는 다음과 같다.

>>> a = [1, 2, 3]
>>> a.extend([4, 5])
>>> a
[1, 2, 3, 4, 5]
+ 기호를 사용하여 더한 것과 extend한 것의 차이점이 있을까? 있다면 그 차이점을 설명하시오.

>>> a = [1, 2, 3]
>>> id(a)
2560847313984
>>> a = a + [4,5]
>>> id(a)
2560843584512
>>> a = [1, 2, 3]
>>> id(a)
2560853004480
>>> a.extend([4, 5])
>>> id(a)
2560853004480

# Q4. A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25] 합 구하기

A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

result = 0
while A:                # A 리스트에 값이 있는 동안
    mark = A.pop()      # A리스트의 가장 마지막 항목을 하나씩 뽑아냄
    if mark >= 50:      # 50점 이상의 점수만 더함
        result += mark

print(result)           # 481 출력



#Q5 피보나치 수열
def fibo(n) :
    if n==1 :
        return 1
    if n==0 :
        return 0
    return fibo(n-1)+fibo(n-2)

for i in range(11):
    print(i, fibo(i))


#Q6 한줄 구구단
user_input = input("구구단을 출력할 숫자를 입력하세요(2~9):")
dan = int(input("구구단을 출력할 숫자를 입력하세요(2~9):"))       # 입력 문자열을 숫자로 변환

for i in range(1, 10):
    print(i*dan, end= ' ')  # 한 줄로 출력하기 위해 줄 바꿈 문자 대신 공백 문자를 마지막에 출력한다.


#Q7
C\\Users\\AwesomeMars\\python


#readline
f=open('C:\\Users\\AwesomeMars\\python\\ABC.txt', 'r')
while(True):
    line=f.readline().strip() # 줄문자 제거
    if not line: break
    print(line)
f.close()


f=open('C:\\Users\\AwesomeMars\\python\\ABC.txt', 'r')
#readlines
lines=f.readlines()
print(lines)
f.close()

new_f=open('C:\\Users\\AwesomeMars\\python\\CBA.txt', 'w')
for line in lines:
    line=line.strip()  # strip 을 안하면?
    new_f.write(line)
    new_f.write('\n')
new_f.close()



while(True):
    lines=f.readlines().strip() # 줄문자 제거
    if not line: break
    print(line)
f.close()



C:\Users\AwesomeMars\python\ABC.txt

f = open("C:\\Users\\AwesomeMars\\python\\ABC.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

f = open('C:\\Users\\AwesomeMars\\python\\ABC.txt', 'r')
lines = f.readlines()    # 모든 라인을 읽음
for line in lines:  #확인
    print(line)
f.close()

lines.reverse()          # 읽은 라인을 역순으로 정렬

f = open('C:\\Users\\AwesomeMars\\python\\ABC.txt', 'w')
for line in lines:
    line = line.strip()  # 포함되어 있는 줄 바꿈 문자 제거
    f.write(line)
    f.write('\n')        # 줄 바꿈 문자 삽입
f.close()


#https://velog.io/@janeljs/python-for-coding-test-4

# https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline
#맨 첫줄 Test case를 입력받을 때는 input()을 사용해도 무방합니다.
import sys
T = int(input()) #Test case
for i in range(T):
 a,b = map(int, sys.stdin.readline().split())
 print(a+b)

#한 개의 정수를 입력받을 때
import sys
a = int(sys.stdin.readline()) #개행문자, 형변환 제거

#정해진 개수의 정수를 한줄에 입력받을 때  -> IDE에서는 안됨
import sys
a,b,c = map(int,sys.stdin.readline().split())

#임의의 개수의 정수를 한줄에 입력받아 리스트에 저장할 때(',' 로 구분할 때)
import sys
data = list(map(int,sys.stdin.readline().split(',')))

#임의의 개수의 정수를 n줄 입력받아 2차원 리스트에 저장할 때
n = int(sys.stdin.readline())
for i in range(n):
#    a, b = map(int, sys.stdin.readline().split())
    arr = sys.stdin.readline().split()
    print(int(arr[0]) + int(arr[1]))

#문자열 n줄을 입력받아 리스트에 저장할 때
import sys
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]


#한 줄씩 읽고 한 줄씩 출력
f=open('test.txt', 'r')
line = f.readlines()
for i in range(len(line)):
    print(line[i], end=' ')



#https://www.python2.net/questions-310445.htm
some data
ý[þ»¢5åÆ¢Nde¼Èó!`Å6^
blah
blah2

import sys
with open(sys.argv[1], 'r', encoding = 'utf-8') as fh:
    # One way to read the lines.
    lines = []
    for line in fh:
        lines.append(line)
    # Another.
    # lines = list(fh)
    # And another.
    # lines = fh.readlines()
print(lines)



# 자이썬 완벽 안내서!
#파이썬 책
https://jythonbook-ko.readthedocs.io/en/latest/InputOutput.html
예제 5-1. sys.stdin 사용하기

# 명령행에서 값을 얻어 변수에 저장
>>> import sys
>>> fav_team = sys.stdin.readline()
Cubs
>>> sys.stdout.write("My favorite team is: %s" % fav_team)
My favorite team is: Cubs

예제 5-3. 시스템 환경 변수를 얻고 변경하기

>>> import os
>>> os.environ["HOME"]
'/Users/juneau'
# 파이썬 세션을 위한 홈 디렉토리 바꾸기
>>> os.environ["HOME"] = "/newhome"
>>> os.environ["HOME"]
'/newhome'

예제 5-4. sys.argv 사용하기

# sysargv_print.py – 명령줄에서 제공한 인수를 모두 출력
import sys
for sys.args in sys.argv:
    print sys.args
# 사용법
>>> jython sysargv_print.py test test2 "test three"
sysargv_print.py
test
test2
test three


# 파일에 행을 쓰고 flush하고 닫기
>>> my_file = open('mynewfile.txt','w')
>>> my_file.write('This is the first line of text.\n')
>>> my_file.write('This is the second line of text.\n')
>>> my_file.write('This is the last line of text.\n')
# 선택사항으로서, 파일을 닫을 것이라면 전혀 불필요하지만, 버퍼를 정리하는 데에는 유용하다.
>>> my_file.flush()
>>> my_file.close()
# 읽기모드로 파일열기
>>> my_file = open('mynewfile.txt','r')
>>> my_file.read()
'This is the first line of text.\nThis is the second line of text.\nThis is the last line of text.\n'
# 만일 다시 읽으면, 커서가 파일의 끝에 있기 때문에 결과는 ''이다.
>>> my_file.read()
''
# 파일의 시작점을 다시 찾아서 읽기
>>> my_file.seek(0)
>>> my_file.read()
'This is the first line of text.This is the second line of text.This is the last line of text.'
# 파일의 시작점을 다시 찾아서 readline() 수행
>>> my_file.seek(0)
>>> my_file.readline()
'This is the first line of text.\n'
>>> my_file.readline()
'This is the second line of text.\n'
>>> my_file.readline()
'This is the last line of text.\n'
>>> my_file.readline()
''
# 현재 커서 위치를 표시하기위해 tell() 사용하기
>>> my_file.tell()
93L
>>> my_file.seek(0)
>>> my_file.tell()
0L
# 파일의 행에 대하여 되풀이
>>> for line in my_file:
...     print (line)     #print(line.strip())
...
This is the first line of text.
This is the second line of text.
This is the last line of text.


#while readline
while True:
    line = my_file.readline().strip()
    if not line: break
    print(line)

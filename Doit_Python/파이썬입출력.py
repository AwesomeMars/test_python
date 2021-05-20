import sys

# T = int(input()) #Test case
# for i in range(T):
#     a,b = map(int, sys.stdin.readline().split())
#     print(a+b)



n = int(sys.stdin.readline())

for i in range(n):
#    a, b = map(int, sys.stdin.readline().split())
    arr = sys.stdin.readline().split()
    print(int(arr[0]) + int(arr[1]))


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
...     print line
...
This is the first line of text.
This is the second line of text.
This is the last line of text.



https://jythonbook-ko.readthedocs.io/en/latest/InputOutput.html

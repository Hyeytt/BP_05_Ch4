import turtle                 # 라이브러리에서 turtle 함수를 불러오기

t = turtle.Turtle()           # 변수 t가 turtle 함수임을 선언

t.shape("turtle")             # 커서의 모양을 거북이로 설정

x1 = int(input("x1 = "))     # input함수로 x1 값을 입력받은 후 int함수로 정수처리
y1 = int(input("y1 = "))     # input함수로 y1 값을 입력받은 후 int함수로 정수처리
x2 = int(input("x2 = "))     # input함수로 x2 값을 입력받은 후 int함수로 정수처리
y2 = int(input("y2 = "))     # input함수로 y2 값을 입력받은 후 int함수로 정수처리
x3 = int(input("x3 = "))     # input함수로 x3 값을 입력받은 후 int함수로 정수처리
y3 = int(input("y3 = "))     # input함수로 y3 값을 입력받은 후 int함수로 정수처리

p1 = [x1, y1]              # p1의 좌표를 입력받은 x1, y1으로 설정
p2 = [x2, y2]              # p2의 좌표를 입력받은 x2, y2으로 설정
p3 = [x3,  y3]              # p3의 좌표를 입력받은 x3, y3으로 설정

t.goto(p1)  # p1 좌표로 이동
t.goto(p2)  # p2 좌표로 이동
t.goto(p3)  # p3 좌표로 이동
t. _screen.exitonclick()      # 클릭하여 사라지게 하기

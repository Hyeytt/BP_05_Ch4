import turtle                 # 라이브러리에서 turtle 함수를 불러오기

t = turtle.Turtle()           # 변수 t가 turtle 함수임을 선언

t.shape("turtle")             # 커서의 모양을 거북이로 설정

color = []                   # color 가 리스트임을 선언


color1 = input(" 색상 #1을 입력하시오 : ")  # input 함수를 통해 변수 color1의   값을 물어봄

color.append(color1)                     # color1을 append 함수를 활용해 color 리스트에 추가

color2 = input(" 색상 #2을 입력하시오 : ")  # input 함수를 통해 변수 color2의   값을 물어봄

color.append(color2)                    # color2를 append 함수를 활용해 color 리스트에 추가


color3 = input(" 색상 #3을 입력하시오 : ")  # input 함수를 통해 변수 color3의   값을 물어봄

color.append(color3)  # color3을 append 함수를 활용해 color 리스트에 추가


# 펜을 입력받은 color1의 색상으로 변화시킨다 , 리스트에서 요소를 셀때에는 0에서부터 시작을한다
t.fillcolor(color[0])

t.begin_fill()  # 색 채우기를 시작한다

t.circle(50)  # 원의 크기를 50으로 정한다

t.end_fill()  # 색채우기를 끝낸다

t.up()     # 펜을 든다

t.goto(100, 0)  # 펜의 좌표를 (200,0)으로 이동시킨다

t.down()  # 펜을 내린다

t.fillcolor(color[1])   # 펜을 입력받은 color2의 색상으로 변화시킨다

t.begin_fill()             # 색 채우기를 시작한다

t.circle(50)                 # 원의 크기를 50으로 정한다

t.end_fill()                    # 색채우기를 끝낸다

t.up()               # 펜을 든다

t.goto(200, 0)        # 펜의 좌표를 (200,0)으로 이동시킨다

t.down()  # 펜을 내린다


t.fillcolor(color[2])  # 펜을 입력받은 color3의 색상으로 변화시킨다

t.begin_fill()      # 색 채우기를 시작한다

t.circle(50)            # 원의 크기를 50으로 정한다

t.end_fill()            # 색채우기를 끝낸다
t. _screen.exitonclick()  # 클릭하여 사라지게 하기

import turtle
A=turtle.Turtle()
B=turtle.Screen()
B.title("Turtle Ders 1")
B.setup(width=720,height=420)
B.bgcolor("red")

# ilk daire
A.up()
A.goto(-100,-100)
A.color("white")
A.begin_fill()
A.circle(120)
A.end_fill()
# ikinci daire
A.goto(-70,-80)
A.color("red")
A.begin_fill()
A.circle(100)
A.end_fill()
#yıldız hazırlık
A.goto(0,35)
A.fillcolor("white")
A.begin_fill()
#yıldız için tekrar eden üççgen çizme
for i in range(5):
    A.forward(150)
    A.right(144)
A.end_fill()

#yazı ekleme
A.goto(-200,-190)
A.color("white")
A.write("SEYİTHAN YILDIZ İLK UYGULAMA DERSİ",font=("articulate",17,"bold"))

A.goto(-999,0)  #kalemi uzağa kaydırarak kaybolması sağlanıyor.

B.exitonclick()
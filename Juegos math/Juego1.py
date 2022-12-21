import turtle
import random

s = turtle.Screen()
s.title("Proyecto 1")
jugador1 = turtle.Turtle()
jugador2 = turtle.Turtle()
s.bgcolor("gray")

jugador1.hideturtle()
jugador1.shape("turtle")
jugador1.color("green")
jugador1.shapesize(2,2,2)
jugador1.pensize(3)

jugador2.hideturtle()
jugador2.shape("turtle")
jugador2.color("blue")
jugador2.shapesize(2,2,2)
jugador2.pensize(3)

jugador1.penup()
jugador1.goto(200,200)
jugador1.pendown()
jugador1.circle(40)

jugador1.penup()
jugador1.goto(-250,240)
jugador1.showturtle()

jugador2.penup()
jugador2.goto(200,-200)
jugador2.pendown()
jugador2.circle(40)

jugador2.penup()
jugador2.goto(-250,-160)
jugador2.showturtle()

#jugador1.forward(380) # probando el limite del circulo. aquí justo en la linea.
#jugador2.forward(385)

dado = [2, 3, 5, 7, 11, 13]

for i in range(20):
    if jugador1.pos() >= (130,240):
        print("La tortuga verde ha ganado")
        break

    elif jugador2.pos() >= (130,-160):
        print("La tortuga azul ha ganado")
        break

    else:
        turno1 = input("Presiona Enter para continuar")
        turno1 = random.choice(dado)
        print("Tu numero en dado es: ",turno1,"\nAvanzas: ",turno1*10)
        jugador1.pendown()
        jugador1.forward(10*turno1)

        turno2 = input("Presiona Enter para continuar")
        turno2 = random.choice(dado)
        print("Tu numero en dado es: ",turno2,"\nAvanzas: ",turno2*10)
        jugador2.pendown()
        jugador2.forward(10*turno2)


turtle.done()
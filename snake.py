import time
import turtle
import random
import pygame
import tkinter as tk
from tkinter import messagebox
import keyboard


s = turtle.Screen()
s.clear()
s.tracer(0)
s.setup(width=600, height=600)

class snake():
    def __init__(self):
        head = turtle.Turtle()
        head.speed(0)
        head.shape("square")
        head.color("black")
        head.penup()
        head.goto(0, 20)
        head.setheading(0)
        head.forward(60)

        head2 = turtle.Turtle()
        head2.speed(0)
        head2.shape("square")
        head2.color("black")
        head2.penup()
        head2.goto(0, 20)
        head2.setheading(0)
        head2.forward(40)

        head3 = turtle.Turtle()
        head3.speed(0)
        head3.shape("square")
        head3.color("black")
        head3.penup()
        head3.goto(0, 20)
        head3.setheading(0)
        head3.forward(20)
        self.tfollow = []
        self.tfollow.append(head)
        self.tfollow.append(head2)
        self.tfollow.append(head3)
    def move(self):
        if  (keyboard.is_pressed('w') or keyboard.is_pressed('Up')):
            if self.tfollow[0].heading() != 270:
                self.tfollow[0].setheading(90)
                print(self.tfollow[0].heading())
        if (keyboard.is_pressed('a') or keyboard.is_pressed('Left')):
            if self.tfollow[0].heading() != 0:
                self.tfollow[0].setheading(180)
                print(self.tfollow[0].heading())
        if (keyboard.is_pressed('s') or keyboard.is_pressed('Down')):
            if self.tfollow[0].heading() != 90:
                self.tfollow[0].setheading(270)
                print(self.tfollow[0].heading())
        if (keyboard.is_pressed('d') or keyboard.is_pressed('Right')):
            if self.tfollow[0].heading() != 180:
                self.tfollow[0].setheading(0)
                print(self.tfollow[0].heading())
        self.tfollow[0].forward(20)
        for x in range(len(self.tfollow) - 1, 0, -1):
            self.tfollow[x].forward(20)
            self.tfollow[x].setheading(self.tfollow[x-1].heading())
    def addseg(self):
        num = len(self.tfollow) - 1
        head2 = turtle.Turtle()
        head2.speed(0)
        head2.shape("square")
        head2.color("black")
        head2.penup()
        head2.goto(self.tfollow[num].pos())
        head2.setheading(self.tfollow[num].heading())
        self.tfollow.append(head2)
        self.tfollow[0].forward(20)
        for x in range(len(self.tfollow) - 2, 0, -1):
            self.tfollow[x].forward(20)
            self.tfollow[x].setheading(self.tfollow[x - 1].heading())

class food():
    def __init__(self):
        x = random.randint(-13,13) * 20
        y = random.randint(-13,13) * 20
        self.f = turtle.Turtle()
        self.f.speed(0)
        self.f.shape("square")
        self.f.color("red")
        self.f.penup()
        self.f.setpos(x, y)
    def move(self):
        x1 = random.randint(-13, 13) * 20
        y1 = random.randint(-13, 13) * 20
        self.f.setpos(x1, y1)
    def checkhit(self, head):
        if self.f.distance(head) < 20:
            return True
        else:
            return False
snakee = snake()
foood = food()
while True:
    s.update()
    if foood.checkhit(snakee.tfollow[0]):
        snakee.addseg()
        foood.move()
    snakee.move()
    time.sleep(.1)
    print(snakee.tfollow[0].pos())






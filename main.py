import pygame
from pygame.locals import *
from pygame.time import Clock
from sys import exit

"""
Board
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
"""

largura = 580
altura = 580


class Screen():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Tic Tac Toe')
        self.squares = {}
        self.tela = pygame.display.set_mode((largura, altura))
        self.symbol = 'x'
        self.largura = 580
        self.altura = 580

    def draw_board(self):
        # desenhando linhas horizontais
        pygame.draw.line(self.tela, (255, 0, 0), (0, 193), (580, 193))
        pygame.draw.line(self.tela, (255, 0, 0), (0, 386), (580, 386))
        # desenhando linhas verticais
        pygame.draw.line(self.tela, (255, 0, 0), (193, 0), (193, 580))
        pygame.draw.line(self.tela, (255, 0, 0), (386, 0), (386, 580))

    def draw_symbol(self, square):
        if self.symbol == 'x':
            self.draw_x(square)
            self.symbol = 'o'
        else:
            self.draw_o(square)
            self.symbol = 'x'

    def search_square(self, pos):
        square = 0
        if 0 <= pos[1] <= 193:
            if 0 <= pos[0] <= 193:
                square = 1
            elif 193 < pos[0] <= 386:
                square = 2
            elif 386 < pos[0] <= 580:
                square = 3
        elif 193 < pos[1] <= 386:
            if 0 <= pos[0] <= 193:
                square = 4
            elif 193 < pos[0] <= 386:
                square = 5
            if 386 < pos[0] <= 580:
                square = 6
        elif 386 < pos[1] <= 580:
            if 0 <= pos[0] <= 193:
                square = 7
            elif 193 < pos[0] <= 386:
                square = 8
            elif 386 < pos[0] <= 580:
                square = 9

        if square not in self.squares:
            self.squares[square] = self.symbol
            self.draw_symbol(square)
            self.win_condicion()

    def draw_o(self, square):

        color = (255, 255, 255)
        # Primeira linha
        if square == 1:
            pygame.draw.circle(self.tela, color, (96.5, 96.5), 66.5)
        if square == 2:
            pygame.draw.circle(self.tela, color, (289.5, 96.5), 66.5)
        if square == 3:
            pygame.draw.circle(self.tela, color, (482.5, 96.5), 66.5)

        # Segunda linha
        if square == 4:
            pygame.draw.circle(self.tela, color, (96.5, 289.5), 66.5)
        if square == 5:
            pygame.draw.circle(self.tela, color, (289.5, 289.5), 66.5)
        if square == 6:
            pygame.draw.circle(self.tela, color, (482.5, 289.5), 66.5)

        # Terceira linha
        if square == 7:
            pygame.draw.circle(self.tela, color, (96.5, 482.5), 66.5)
        if square == 8:
            pygame.draw.circle(self.tela, color, (289.5, 482.5), 66.5)
        if square == 9:
            pygame.draw.circle(self.tela, color, (482.5, 482.5), 66.5)

    def draw_x(self, square):
        color = (255, 255, 255)
        # Primeira linha
        if square == 1:
            pygame.draw.line(self.tela, color, (30, 30), (163, 163))
            pygame.draw.line(self.tela, color, (163, 30), (30, 163))
        if square == 2:
            pygame.draw.line(self.tela, color, (223, 30), (356, 163))
            pygame.draw.line(self.tela, color, (356, 30), (223, 163))
        if square == 3:
            pygame.draw.line(self.tela, color, (416, 30), (549, 163))
            pygame.draw.line(self.tela, color, (549, 30), (416, 163))

        # Segunda linha
        if square == 4:
            pygame.draw.line(self.tela, color, (30, 223), (163, 356))
            pygame.draw.line(self.tela, color, (163, 223), (30, 356))
        if square == 5:
            pygame.draw.line(self.tela, color, (223, 223), (356, 356))
            pygame.draw.line(self.tela, color, (356, 223), (223, 356))
        if square == 6:
            pygame.draw.line(self.tela, color, (416, 223), (549, 356))
            pygame.draw.line(self.tela, color, (549, 223), (416, 356))

        # Terceira linha
        if square == 7:
            pygame.draw.line(self.tela, color, (30, 416), (163, 549))
            pygame.draw.line(self.tela, color, (163, 416), (30, 549))
        if square == 8:
            pygame.draw.line(self.tela, color, (223, 416), (356, 549))
            pygame.draw.line(self.tela, color, (356, 416), (223, 549))
        if square == 9:
            pygame.draw.line(self.tela, color, (416, 416), (549, 549))
            pygame.draw.line(self.tela, color, (549, 416), (416, 549))

    def win_condicion(self):
        try:
            if (self.squares[1] == self.squares[2] == self.squares[3]) or (self.squares[4] == self.squares[5] == self.squares[6]) or (self.squares[7] == self.squares[8] == self.squares[9]) or (self.squares[1] == self.squares[5] == self.squares[9]) or (self.squares[3] == self.squares[5] == self.squares[7]) or (self.squares[1] == self.squares[4] == self.squares[7]) or (self.squares[2] == self.squares[5] == self.squares[8]) or (self.squares[3] == self.squares[6] == self.squares[9]):
                print(self.squares)
                exit()

        except KeyError:
            pass


jogo = Screen()
jogo.draw_board()
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                jogo.search_square(pos)
                pygame.display.update()

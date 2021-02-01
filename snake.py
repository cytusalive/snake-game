import pygame
import sys

#initialize pygame
pygame.init()
pygame.display.set_caption("Snake game")

#initialize screen
screen = pygame.display.set_mode((600, 600))
bgcolor = (230, 230, 100)

#initialize fps
clock = pygame.time.Clock()

class Field:
    def __init__(self, x, y):
        self.field = [[0 for a in range(y)] for b in range(x)]
        self.ysize = y
        self.xsize = x
        self.gridsize = screen.get_width() // self.xsize
    
    def drawfield(self):
        for y in range(self.ysize):
            for x in range(self.xsize):
                if type(self.field[y][x]) == int and self.field[y][x] > 0:
                    pygame.draw.rect(screen, (20,50,200), (x*self.gridsize, y*self.gridsize, self.gridsize, self.gridsize))

    def iterate(self):
        for y in range(self.ysize):
            for x in range(self.xsize):
                if type(self.field[y][x]) == int and self.field[y][x] > 0:
                    self.field[y][x] -= 1

game = Field(15, 15)

class Snake:
    def __init__(self):
        self.length = 10
        self.xpos = 1
        self.ypos = 1
        self.direction = 1

    def move(self):
        # [LEFT, RIGHT, UP, DOWN]
        directions = [(self.xpos-1, self.ypos), (self.xpos+1, self.ypos), (self.xpos, self.ypos-1), (self.xpos, self.ypos+1)]
        x, y = directions[self.direction]
        if x in range(game.xsize) and y in range(game.ysize):
            if game.field[y][x] == 0:
                self.xpos, self.ypos = x, y
            else:
                self.gameover()
        else:
            self.gameover()
    
    def update(self): 
        game.field[self.ypos][self.xpos] = self.length
        
    def gameover(self):
        pygame.quit()
        print("Game Over, your length:", self.length)


snake = Snake()


while True:
    screen.fill(bgcolor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if snake.direction != 1:
                    snake.direction = 0
                    break
            if event.key == pygame.K_RIGHT:
                if snake.direction != 0:
                    snake.direction = 1
                    break
            if event.key == pygame.K_UP:
                if snake.direction != 3:
                    snake.direction = 2
                    break
            if event.key == pygame.K_DOWN:
                if snake.direction != 2:
                    snake.direction = 3
                    break
    game.iterate()
    snake.move()
    snake.update()
    game.drawfield()
    pygame.display.update()
    msElapsed = clock.tick(4)
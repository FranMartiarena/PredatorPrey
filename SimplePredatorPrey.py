import pygame
import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt


pygame.init()
screen = pygame.display.set_mode((750,500))
dis = 10
screen.fill((0,0,0))

cells_x, cells_y = 75, 50

npreys = 500
npredators = 20

states = [0,0,1,2]

prey_born_probability = 0.7
prey_death_probability = 0.9

predator_born_probability = 0.9
predator_death_probability = 0.7

data = [] #gen, predator, preys

#area = [[random.choice(states) for x in range(cells_x)] for y in range(cells_y)]

area = []
for y in range(cells_y):
    a = []
    for x in range(cells_x):
        c = random.choice(states)
        if c == 1 and npreys > 0:
            a.append(c)
            npreys -= 1
        elif c == 2 and npredators > 0:
            a.append(c)
            npredators -= 1
        else:
            a.append(0)
    area.append(a)

area = np.array(area)

def plot(df):
    df.columns = ["generations", "predators", "preys"]
    df.plot(kind = "line", x = "generations")
    plt.show()

def NextGen(area):
    generation = 0
    while True:
        generation += 1
        prey_already_taken = []
        pred_already_taken = []
        area2 = np.zeros((cells_y,cells_x))
        for y in range(area.shape[0]):
            for x in range(area.shape[1]):
                if area[y,x] == 1: # if is prey
                    preds = []
                    moves = []
                    preys = []
                    for i in [-1,0,1]:
                        for j in [-1,0,1]:
                            if i == 0 and j == 0:
                                preys.append([y+i,x+j])
                            elif y+i < cells_y and y+i >= 0 and x+j < cells_x and x+j >= 0:
                                #if area[y+i,x+j] == 0 and [y+i,x+j] not in prey_already_taken:
                                #    moves.append([y+i,x+j])
                                if area[y+i,x+j] == 1:
                                    preys.append([y+i,x+j])
                                elif area[y+i,x+j] == 2:
                                    preds.append([y+i,x+j])
                    chance = random.randint(0,100)
                    if chance < ((1-prey_death_probability)**len(preds))*100:#Si sobrevive
                        area2[y,x] = 1
                        prey_already_taken.append([y,x])
                    else:#Si muere
                        chance = random.randint(0,100)
                        if chance < predator_born_probability*100:#Si se convierte en depredador
                            if len(preds) == 0:
                                area2[y,x] = 2
                                pred_already_taken.append([y,x])
                            else:
                                area2[y,x] = 2
                                pred_already_taken.append([y,x])
                                pred = random.choice(preds)
                                area2[pred[0],pred[1]] = 2
                                pred_already_taken.append(pred)

                elif area[y,x] == 2:
                    chance = random.randint(0,100)
                    if chance < predator_death_probability*100 and [y,x] not in pred_already_taken:
                        area2[y,x] = 0
                    else:
                        area2[y,x] = 2
                        pred_already_taken.append([y,x])

                elif area[y,x] == 0:
                    preds = []
                    preys = []

                    for i in [-1,0,1]:
                        for j in [-1,0,1]:
                            if i == 0 and j == 0:
                                pass
                            elif y+i < cells_y and y+i >= 0 and x+j < cells_x and x+j >= 0:
                                if area[y+i,x+j] == 1:
                                    preys.append([y+i,x+j])
                                elif area[y+i,x+j] == 2:
                                    preds.append([y+i,x+j])

                    if len(preys) == 0 or len(preds) > 0:
                        pass
                    else:
                        chance = random.randint(0,100)
                        if chance <= ((1-prey_born_probability)**len(preys))*100: #Si no nace
                            pass
                        else:
                            area2[y,x] = 1
                            prey_already_taken.append([y,x])

        drawGrid(area2, generation)
        area = area2.copy()

def drawGrid(area, generation):
    preys = 0
    predators = 0
    df = pd.DataFrame(data)
    for x in range(cells_x):
        for y in range(cells_y):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    plot(df)
                    exit()
            if area[y,x] == 0:
                rect = pygame.Rect(x*dis, y*dis, dis, dis)#left, top, width, height
                #pygame.draw.rect(screen, (25,25,25), rect, 1)
                pygame.draw.rect(screen, (0,0,0), ((x)*dis, (y)*dis, dis, dis ))
            elif area[y,x] == 1:
                preys += 1
                pygame.draw.rect(screen, (0,255,0), ((x)*dis, (y)*dis, dis, dis ))
            elif area[y,x] == 2:
                predators += 1
                pygame.draw.rect(screen, (255,0,0), ((x)*dis, (y)*dis, dis, dis))

    data.append([generation,predators,preys])
    df = pd.DataFrame(data)
    df.columns = ["generation", "predators", "preys"]
    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            exit()
    drawGrid(area, 0)
    NextGen(area)

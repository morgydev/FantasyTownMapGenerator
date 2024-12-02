import numpy as np
import pygame as py

WIDTH = 1000
HEIGHT = 800
CENTER = (WIDTH/2, HEIGHT/2)
RADIUS = 300
STEP = 1
NUMBER_OF_POINTS = 500
COLOUR = (255, 232 + np.random.randint(0, 20), 168 + np.random.randint(0, 20))
COLOUR_ROAD = (120, 72, 17)
COLOUR_TOWERS = (0, 0, 0)

py.init()
window = py.display.set_mode((WIDTH, HEIGHT))

points = []
points_generated = 0
while points_generated < NUMBER_OF_POINTS:
    points_generated += 1
    point = (np.random.randint(20, WIDTH-20), np.random.randint(20, HEIGHT - 20))
    if (np.sqrt((point[0] - CENTER[0])**2 + (point[1] - CENTER[1])**2) <= RADIUS*1.1):
        points.append(point)

window.fill(COLOUR)

py.draw.circle(window, COLOUR_ROAD, (10, 10), HEIGHT, 10)
if np.random.random() > 0.5:
    py.draw.rect(window, COLOUR, (0, HEIGHT/2, WIDTH, HEIGHT/2))
else:
    py.draw.rect(window, COLOUR, (0, 0, WIDTH, HEIGHT/2))

vertices = []
for i in range(0, WIDTH, STEP):
    for j in range(0, HEIGHT, STEP):
        if int(np.sqrt((CENTER[0] - i)**2 + (CENTER[1] - j)**2)) < RADIUS:
            point_distance = []
            for p in range(len(points)):
                point_distance.append(int(np.sqrt((points[p][0] - i)**2 + (points[p][1] - j)**2)))
            py.draw.rect(window, COLOUR, (i, j, STEP, STEP))

            if (point_distance.count(min(point_distance)) > 1):
                vertices.append((i, j))

    print(f"{np.round(i/WIDTH*100, 2)}% complete.")

for vertex in vertices:
    if (int(np.sqrt((CENTER[0] - vertex[0])**2 + (CENTER[1] - vertex[1])**2)) < RADIUS):
            py.draw.circle(window, COLOUR_ROAD, vertex, 1)

towers = []
theta = np.arange(0, 2 * np.pi, 2 * np.pi/np.random.randint(7, 15))
for th in theta:
    position_x = 1.05 * RADIUS * np.cos(th) + CENTER[0]
    position_y = 1.05 * RADIUS * np.sin(th) + CENTER[1]
    py.draw.rect(window, COLOUR_TOWERS, (position_x - 10, position_y - 10, 20, 20))
    towers.append((position_x, position_y))

py.draw.lines(window, COLOUR_TOWERS, True, towers, 6)
    

print(f"100% complete!")
#for point in points:
#    py.draw.circle(window, (255, 0, 0), point, 3)

py.display.flip()

running = True
while(running):
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            running = False
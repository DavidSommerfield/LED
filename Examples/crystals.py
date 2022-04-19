import LED, random

print(LED.__file__)

points = []
colored_points = []
offset = 0
my_hue = 0
merge  = 1

W = LED.get_width_adjusted()
H = LED.get_height_adjusted()

for point in range(20):
    x = random.randint(0,W)
    y = random.randint(0,H)
    points.append([x,y,point*(255/20)])

for x in range(W):
    for y in range(H):
        prev_distance = 10000
        
        for point in points:
            distance = ((point[0]-x)**2+(point[1]-y)**2)

            if distance < prev_distance:
                prev_hue = my_hue
                merge = 0 if (prev_distance == 0) else (distance/prev_distance)
                my_hue = point[2] + (prev_hue - point[2]) * merge
                prev_distance = distance
        colored_points.append((x,y,my_hue,merge))

while True:
    for point in colored_points:
        offset += 0.0005
        LED.draw_pixel(point[0],point[1],LED.color_hsv(point[2]+offset,255,point[3]*255))
    LED.draw()
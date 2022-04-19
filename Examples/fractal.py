import numpy as np
from LED import *
from math import floor

W, H = get_width_adjusted(), get_height_adjusted()

# generating the range of x values and y values
xvals = np.arange(0, W)
yvals = np.arange(0, H)
palette = [(5, 5, 24), (107, 31, 255), (204, 40, 195), (255, 255, 200)]
scale = 1
zoom = 1.025
max_zoom = 2**54 # a very large number, right before floating point representation breaks

while True:
    # zoom in and out
    if (scale > max_zoom) or (scale < 1):
        zoom = 1 / zoom
    scale *= zoom

    # Zoom to a specific location
    x_shift = 529119.95 * (scale / 2097152)
    y_shift = 370.30776251 * (scale / 2097152)

    # create the complex plane we work from, adjusted for shift and scale
    x, y = np.meshgrid((xvals + x_shift - W / 2) / scale, (yvals + y_shift - H / 2) / scale)
    
    # mandelbrot set formula
    z = c = x + y * 1j

    iters = np.full(z.shape, 0)
    mask = np.full(z.shape, 1)
    detail = 48 + floor(min(1, scale / 1000000) * 2000)

    # count number of iterations for coloring
    for i in range(detail):
        mask *= np.abs(z) <= 2 * 100
        iters += mask
        z = (z ** 2 + c) * mask

    # draw each pixel
    for y, row in enumerate(iters):
        for x, pixel in enumerate(row):
            draw_pixel(x, y, merge_palette(palette, pixel / detail))

    draw()
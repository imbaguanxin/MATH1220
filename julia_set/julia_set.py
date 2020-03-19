import numpy as np
import matplotlib.pyplot as plt
import math


def julia_set_plt(width=720, height=480, zoom=0.7,
                  c=(0.37, 0.1), max_iter=512, move_xy=(0.0, 0.0),
                  color_iter=1,
                  three_color=(np.array([166. / 255., 55. / 255., 55. / 255.]),
                               np.array([255. / 255., 221. / 255., 141. / 255.]),
                               np.array([31. / 255., 61. / 255., 144. / 255.])),
                  bkgd_color=np.array([0.0, 0.0, 0.0]),
                  img_title="Julia_Fractal",
                  save_flag=False):
    # creating the new image
    img = np.zeros((height, width, 3))

    # setting up the variables according to
    # the equation to create the fractal
    cX, cY = c
    moveX, moveY = move_xy

    # setting coloring
    if color_iter < 1:
        print("The input number of color iteration should be integers greater no less than 1.")
        print("Your input is invalid so it is set to the default value: 1.")
        color_iter = 1
    else:
        color_iter = math.floor(color_iter)
    clr0, clr1, clr2 = three_color

    bin_num = 3 * color_iter + 1
    one_over_bin_num = 1.0 / bin_num
    # iterate to calculate
    for x in range(width):
        for y in range(height):
            zx = 1.5 * (x - width / 2) / (0.5 * zoom * width) + moveX
            zy = 1.0 * (y - height / 2) / (0.5 * zoom * height) + moveY
            i = 0
            while zx * zx + zy * zy < 4 and i < max_iter:
                tmp = zx * zx - zy * zy + cX
                zy, zx = 2.0 * zx * zy + cY, tmp
                i += 1
            # decided the color
            clr = i / max_iter
            clr = clr - math.floor(clr)
            if clr < one_over_bin_num:
                clr = clr / one_over_bin_num
                img[y, x] = bkgd_color * (1 - clr) + clr1 * clr
            else:
                clr = (clr - one_over_bin_num) / (1 - one_over_bin_num) * color_iter
                clr = clr - math.floor(clr)
                if clr < 0.5:
                    clr = clr * 2
                    img[y, x] = (clr0 * (1 - clr) + clr1 * clr)
                else:
                    clr = (clr - 0.5) * 2
                    img[y, x] = (clr1 * (1 - clr) + clr2 * clr)

    # to display the created fractal
    fig = plt.figure()
    plt.imshow(img)
    plt.title("Julia Fractal: C = {} + {}i".format(cX, cY))
    # save the figure
    if save_flag:
        fig.savefig('{}.png'.format(img_title), dpi=1000)
    plt.show()
    print("Picture size: {} * {}".format(width, height))
    print("maximum iteration: {}".format(max_iter))
    print("Zoom parameter: {}".format(zoom))


def main():
    julia_set_plt(color_iter=4, save_flag=True)


if __name__ == '__main__':
    main()

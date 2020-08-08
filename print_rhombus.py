def draw_rhombus(side_len):
    s = "*"
    for i in range(1, side_len*2, 2):
        print((s*i).center(side_len*2-1))
    for i in reversed(range(1, side_len*2-2, 2)):
        print((s * i).center(side_len*2-1))


if __name__ == '__main__':
    draw_rhombus(5)


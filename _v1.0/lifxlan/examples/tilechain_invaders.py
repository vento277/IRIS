from lifxlan import *
from random import randint
from time import sleep


def main():
    lan = LifxLAN()
    tilechain_lights = lan.get_tilechain_lights()
    if len(tilechain_lights) != 0:
        t = lan.get_tilechain_lights()[0]  # grab the first tilechain
        print("Selected TileChain light: {}".format(t.get_label()))
        original_colors = t.get_tilechain_colors()
        num_tiles = t.get_tile_count()

        duration_ms = 5
        DIM_BLUE = BLUE
        DIM_BLUE[2] = DIM_BLUE[2]/3
        palette = {0: YELLOW,
                   1: BLUE#DIM_BLUE
                    }

        num_frames = 2
        invader_matrix = \
               [[[1, 1, 1, 0, 0, 1, 1, 1],
                 [1, 1, 0, 0, 0, 0, 1, 1],
                 [1, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 1, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 1, 0, 1],
                 [0, 1, 1, 1, 1, 1, 1, 0],
                 [1, 0, 1, 1, 1, 1, 0, 1]],

                [[1, 1, 1, 0, 0, 1, 1, 1],
                 [1, 1, 0, 0, 0, 0, 1, 1],
                 [1, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 1, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 1, 0, 1, 1, 0, 1, 1],
                 [1, 0, 1, 0, 0, 1, 0, 1],
                 [0, 1, 0, 1, 1, 0, 1, 0]]]

        try:
            while True:
                for frame in range(num_frames):
                    sprite = []
                    for x in range(8):
                        for y in range(8):
                                sprite.append(palette[invader_matrix[frame][x][y]])
                    for index in range(num_tiles):
                        t.set_tile_colors(index, sprite, duration_ms, rapid=True)
                    sleep(1)
        except KeyboardInterrupt:
                t.set_tilechain_colors(original_colors)
                print("Done.")
    else:
            print("No TileChain lights found.")


def get_random_color():
    return randint(0, 65535), randint(0, 65535), randint(0, 65535), randint(2500, 9000)


if __name__ == "__main__":
    main()

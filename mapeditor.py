
import sys
import os
import ConfigParser
import pygame
from worldmap import Map
from tile import Tile

pygame.init()

Wi, X= 0, 0
He, Y= 1, 1
AVAILABLE= 0

BACKGROUND_COLOR= 0, 0, 0
LINE_COLOR= 35, 35, 35
GRID_COLOR= 255, 255, 0

#### TODO set up all this propperly ####
IMG_FILE_EXT= ".png"
MAP_FILE_EXT= ".txt"
IMAGES_PATH= ""
MAP_FILES_PATH= ""
########################################

DEFAULT_TILE_SIZE= 32
DISPLAY_HEIGHT= 672
VISION_RANGE_SIZE= 672, DISPLAY_HEIGHT
SURFACES_HEADER_SIZE= 256, 32
ITEMS_HEADER_SIZE= 256, 32
SURFACES_BOX_SIZE= SURFACES_HEADER_SIZE[Wi], DISPLAY_HEIGHT - SURFACES_HEADER_SIZE[He]
ITEMS_BOX_SIZE= ITEMS_HEADER_SIZE[Wi], DISPLAY_HEIGHT - ITEMS_HEADER_SIZE[He]

DIV_LINE_THICKNESS= 4

DISPLAY_SIZE= ( #display width results from all components' widths added
                (VISION_RANGE_SIZE[Wi] + SURFACES_BOX_SIZE[Wi] + 
                ITEMS_BOX_SIZE[Wi] + 2*DIV_LINE_THICKNESS) , 

                DISPLAY_HEIGHT)

if not (
        DEFAULT_TILE_SIZE > 0 and 
        DEFAULT_TILE_SIZE % 1 == 0 and #must be integer
        DISPLAY_HEIGHT > 0 and 
        VISION_RANGE_SIZE[Wi] > 0 and 
        SURFACES_HEADER_SIZE[Wi] > 0 and 
        SURFACES_HEADER_SIZE[He] > 0 and 
        ITEMS_HEADER_SIZE[Wi] > 0 and 
        ITEMS_HEADER_SIZE[He] > 0 
        ): 
            raise ValueError("Dimensions must be positive integers!")

if not (   
        DISPLAY_HEIGHT % DEFAULT_TILE_SIZE == 0 and 
        VISION_RANGE_SIZE[Wi] % DEFAULT_TILE_SIZE == 0 and 
        SURFACES_HEADER_SIZE[Wi] % DEFAULT_TILE_SIZE == 0 and 
        SURFACES_HEADER_SIZE[He] % DEFAULT_TILE_SIZE == 0 and 
        ITEMS_HEADER_SIZE[Wi] % DEFAULT_TILE_SIZE == 0 and 
        ITEMS_HEADER_SIZE[He] % DEFAULT_TILE_SIZE == 0 
        ): 
            raise ValueError("All dimensions must be multiples of " + 
                            str(DEFAULT_TILE_SIZE) + ".")


loaded_surfaces= []
loaded_items= []

#arrays of int values to indicate which sprite occupies a specific tile in a box
loaded_surfaces_box_tiles= [0] * (
                                    SURFACES_BOX_SIZE[Wi] / DEFAULT_TILE_SIZE * 
                                    SURFACES_BOX_SIZE[He] / DEFAULT_TILE_SIZE)

loaded_items_box_tiles= [0] * (
                                    ITEMS_BOX_SIZE[Wi] / DEFAULT_TILE_SIZE * 
                                    ITEMS_BOX_SIZE[He] / DEFAULT_TILE_SIZE
                                    )
highlighted_img= None
vision_range= 0, 0
editing_new_map= False

########################    rectangles for every component of GUI    ###########################

vision_range_rect= pygame.Rect(0, 0, VISION_RANGE_SIZE[Wi], VISION_RANGE_SIZE[He])

surfaces_rect= pygame.Rect(
                            VISION_RANGE_SIZE[Wi] + DIV_LINE_THICKNESS, 
                            SURFACES_HEADER_SIZE[He] , 
                            SURFACES_BOX_SIZE[Wi], 
                            SURFACES_BOX_SIZE[He]
                            )

items_rect= pygame.Rect(
                            VISION_RANGE_SIZE[Wi] + 2*DIV_LINE_THICKNESS + SURFACES_BOX_SIZE[Wi],
                            ITEMS_HEADER_SIZE[He], 
                            ITEMS_BOX_SIZE[Wi], 
                            ITEMS_BOX_SIZE[He]
                            )

header_rect= pygame.Rect (
                            VISION_RANGE_SIZE[Wi] + DIV_LINE_THICKNESS, 
                            0, 
                            SURFACES_HEADER_SIZE[Wi] + ITEMS_BOX_SIZE[Wi] + DIV_LINE_THICKNESS,
                            SURFACES_HEADER_SIZE[1]
                            )

################################################################################################

def load_sprites(img_list, box):
    for image in img_list:
        load_sprite(image, box)


def load_sprite(sprite, box):
    try:
        box.append(pygame.image.load(IMAGES_PATH + sprite + IMG_FILE_EXT))
        print "Surface " + sprite + " successfully loaded."

    except pygame.error:
        print ( "Sprite " + sprite + " could not be loaded. "
                "\nMake sure that file exists in " + IMAGES_PATH + " directory." )


def pos_from_index(index, size):
    size= size[Wi] / DEFAULT_TILE_SIZE , size[He] / DEFAULT_TILE_SIZE
    if index < size[Wi] * size[He]:
        x= index%size[Wi]
        y= index/size[Wi]
        return (x, y)
    else: print "Index is out of this box's boundaries."

def next_available_tile(starting_pos, box):
    for tile in range(starting_pos, box):
        if box(tile) == AVAILABLE:
            return tile

    print "There's not enough room to place another sprite in the box."
    return -1

def sprite_from_img_id(img_id, loaded_sprites):
    if is_positive_int(img_id):
        for sprite in loaded_sprites:
            pass
            


def find_room(sprite, box):
    img_size= (sprite.get_rect().width / DEFAULT_TILE_SIZE , 
                sprite.get_rect.height / DEFAULT_TILE_SIZE)
    av_tile= 0
    while av_tile < len(box):
            av_tile= pos_from_index(next_available_tile(loaded_surfaces_box_tiles), SURFACES_BOX_SIZE) # TODO hardcoded
            if av_tile < 0: return # in case there's no space.

           # if av_tile + img_size[Wi] >

            for tile in range(av_tile, size[Wi]):
                pass




def window(surface, message= "", options= ()):
    pass

#used to validate filenames for maps and images.
def is_positive_int(name):
    try:
        return int(name) and int(name) > 0
    except ValueError:
        return False



def draw_grid(surface):

    draw_pos= DEFAULT_TILE_SIZE
    while draw_pos < VISION_RANGE_SIZE[Wi]:
        pygame.draw.line(surface, GRID_COLOR, (draw_pos, 0), (draw_pos, VISION_RANGE_SIZE[He]))
        draw_pos += 32

    draw_pos= DEFAULT_TILE_SIZE
    while draw_pos < VISION_RANGE_SIZE[He]:
        pygame.draw.line(surface, GRID_COLOR, (0, draw_pos), (VISION_RANGE_SIZE[Wi], draw_pos))
        draw_pos += 32


def tile_from_click(pos):
    pass

font= pygame.font.Font(None, 38)

while True:

    if editing_new_map:
        for event in pygame.event.get():

            if (event.type == pygame.QUIT or 
                (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE)):
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                pass 

            if event.type == pygame.KEYUP and event.key == pygame.K_l: #to load sprites
                sprites_to_load= raw_input("Enter sprite numbers separated by spaces: ")
                sprites_list= sprites_to_load.split()

                all_valid= True
                for sprite in sprites_list:
                    if not is_positive_int(sprite):
                        print ("One or more of the characters you entered"
                                " are not positive integers or spaces.")
                        all_valid= False
                        break

                if all_valid: load_sprites(sprites_list, loaded_surfaces) #FIXME hardcoded

    else:
        desc= raw_input("Enter a brief description for the new map: ")

        while True: # loop for map id
            map_id= raw_input("Enter a positive integer to be this map's id and filename: ")

            if is_positive_int(map_id):

                if not os.path.exists(MAP_FILES_PATH + map_id + MAP_FILE_EXT):
                    break
                else: 
                    print "A map named " + map_id + MAP_FILE_EXT + " already exists!"

            else: print "Map id must be a positive integer!"

        while True:
            size= raw_input("Enter this map's width and height, separated by a space: ")
            size_list= size.split()

            if (len(size_list) == 2 and
                is_positive_int(size_list[0]) and
                is_positive_int(size_list[1])
                ):
                size = int(size_list[0]) , int(size_list[1])
                break
            else:
                print "Both width and height must be positive integers separated by a space!"

        worldmap= Map(map_id, desc, size)

        for pos_x in range (worldmap.size[Wi]):
            for pos_y in range (worldmap.size[He]):
                worldmap.tiles.append(Tile(worldmap.id, pos_x, pos_y))

        screen = pygame.display.set_mode(DISPLAY_SIZE)
        screen.fill(BACKGROUND_COLOR)

        pygame.draw.line(
                        screen,
                        LINE_COLOR,
                        (VISION_RANGE_SIZE[Wi] + DIV_LINE_THICKNESS/2 , 0),
                        (VISION_RANGE_SIZE[Wi]  + DIV_LINE_THICKNESS/2, VISION_RANGE_SIZE[He]),
                        DIV_LINE_THICKNESS)

        line_x_coord= VISION_RANGE_SIZE[Wi] + DIV_LINE_THICKNESS + SURFACES_BOX_SIZE[Wi]
        # had to predefine line_x_coord for statement below not to be 250 characters long.
        pygame.draw.line(
                        screen,
                        LINE_COLOR,
                        (line_x_coord  + DIV_LINE_THICKNESS/2 , 0),
                        (line_x_coord  + DIV_LINE_THICKNESS/2 , DISPLAY_SIZE[He]),
                        DIV_LINE_THICKNESS)

        screen.fill(LINE_COLOR, header_rect)
        screen.blit(
                    font.render(
                                "        SURFACES                    ITEMS",
                                True,
                                (255, 255, 255)),
                    header_rect)

        draw_grid(screen)
        pygame.display.flip()
        editing_new_map= True
import sys, os, pygame, ConfigParser
from worldmap import Map
from tile import Tile
pygame.init()

Wi= 0
He= 1
SURFACE= True
ITEM= False

FILE_EXTENSION= ".png"
IMAGE_PATH= "graphics_indexer/"

VISION_RANGE_SIZE= 672, 672
LOADED_SURFACES_CHART_SIZE= 256, 640
LOADED_SURFACES_HEADER_SIZE= 256, 32
LOADED_ITEMS_CHART_SIZE= 256, 640
LOADED_ITEMS_HEADER_SIZE= 256, 32

DIVISION_LINE_THICKNESS= 4

DISPLAY_SIZE= (VISION_RANGE_SIZE[Wi] + LOADED_SURFACES_CHART_SIZE[Wi] + LOADED_ITEMS_CHART_SIZE[Wi] + 2*DIVISION_LINE_THICKNESS) , 672

DEFAULT_TILE_SIZE= 32
BACKGROUND_COLOR= 0, 0, 0
LINE_COLOR= 35, 35, 35
GRID_COLOR= 255, 255, 0

loaded_surfaces= []
#array of boolean values used to accommodate sprites at the loaded_surfaces chart
loaded_surfaces_chart_tiles= [False] * (LOADED_SURFACES_CHART_SIZE[Wi] / DEFAULT_TILE_SIZE * LOADED_SURFACES_CHART_SIZE[He] / DEFAULT_TILE_SIZE)
loaded_items= []
#array of boolean values used to accommodate sprites at the loaded_items chart
loaded_items_chart_tiles= [False] * (LOADED_ITEMS_CHART_SIZE[Wi] / DEFAULT_TILE_SIZE * LOADED_ITEMS_CHART_SIZE[He] / DEFAULT_TILE_SIZE)
highlighted_img= None
vision_range= 0, 0
editing_new_map= False

#rectangles for every component of GUI
vision_range_rect= pygame.Rect(0, 0, VISION_RANGE_SIZE[Wi], VISION_RANGE_SIZE[He])
loaded_surfaces_rect= pygame.Rect(VISION_RANGE_SIZE[Wi] + DIVISION_LINE_THICKNESS, LOADED_SURFACES_HEADER_SIZE[He] , LOADED_SURFACES_CHART_SIZE[Wi], LOADED_SURFACES_CHART_SIZE[He])
loaded_items_rect= pygame.Rect(VISION_RANGE_SIZE[Wi] + 2*DIVISION_LINE_THICKNESS + LOADED_SURFACES_CHART_SIZE[Wi], LOADED_ITEMS_HEADER_SIZE[He], LOADED_ITEMS_CHART_SIZE[Wi], LOADED_ITEMS_CHART_SIZE[He])
loaded_header_rect= pygame.Rect (VISION_RANGE_SIZE[Wi] + DIVISION_LINE_THICKNESS, 0, LOADED_SURFACES_HEADER_SIZE[Wi] + LOADED_ITEMS_CHART_SIZE[Wi] + DIVISION_LINE_THICKNESS, LOADED_SURFACES_HEADER_SIZE[1])




def load_sprites(img_list, surfaces): # surfaces will be true to load surfaces and false to load items
	if surfaces:
		global loaded_surfaces

		for image in img_list:
			load_surface(image)

	else: # we're trying to load images
		global loaded_items

		for image in range (len(img_list)):
			load_item(image)


def load_surface(sprite):
	try:
		loaded_surfaces.append(pygame.image.load(IMAGE_PATH + sprite + FILE_EXTENSION))
		print "Surface " + sprite + " successfully loaded."

	except pygame.error:
		print "Surface " + sprite + " could not be loaded. \nMake sure that file exists in " + IMAGE_PATH + " directory."

def load_item(sprite): 
	try:
		loaded_items.append(pygame.image.load(IMAGE_PATH + sprite + FILE_EXTENSION))
		print "Item " + sprite + " successfully loaded."

	except pygame.error:
		print "Item " + sprite + " could not be loaded. \nMake sure that file exists in " + IMAGE_PATH + " directory."


#def 




def window(surface, message= "", options= ()):
	pass


def is_valid_sprite_name(string):
	try:
		return int(string) and int(string) > 0
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
			if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
				sys.exit()

			if event.type == pygame.MOUSEBUTTONUP:
				pass 

			if event.type == pygame.KEYUP and event.key == pygame.K_l: #to load sprites
				sprites_to_load= raw_input("Enter sprite numbers separated by spaces: ")
				sprites_list= sprites_to_load.split()

				all_valid= True
				for sprite in sprites_list:
					if not is_valid_sprite_name(sprite):
						print "One or more of the characters you entered are not spaces or positive integers."
						all_valid= False
						break

				if all_valid: load_sprites(sprites_list, SURFACE)
				print loaded_surfaces

	else:
		worldmap= Map(1, "test", (100, 100))

		for pos_x in range (worldmap.size[Wi]):
			for pos_y in range (worldmap.size[He]):
				worldmap.tiles.append(Tile(worldmap.id, pos_x, pos_y))

		screen = pygame.display.set_mode(DISPLAY_SIZE)
		screen.fill(BACKGROUND_COLOR)
		pygame.draw.line(screen, LINE_COLOR, (VISION_RANGE_SIZE[Wi] + DIVISION_LINE_THICKNESS/2 , 0), (VISION_RANGE_SIZE[Wi]  + DIVISION_LINE_THICKNESS/2, VISION_RANGE_SIZE[He]), DIVISION_LINE_THICKNESS)

		draw_point_x= VISION_RANGE_SIZE[Wi] + DIVISION_LINE_THICKNESS + LOADED_SURFACES_CHART_SIZE[Wi]
		pygame.draw.line(screen, LINE_COLOR, (draw_point_x  + DIVISION_LINE_THICKNESS/2 , 0), (draw_point_x  + DIVISION_LINE_THICKNESS/2 , DISPLAY_SIZE[He]), DIVISION_LINE_THICKNESS)
		screen.fill(LINE_COLOR, loaded_header_rect)
		screen.blit(font.render("        SURFACES                    ITEMS", True, (255, 255, 255)), loaded_header_rect) # this shitty method doesn't understand tabs so I used spaces :S
		draw_grid(screen)
		pygame.display.flip()
		editing_new_map= True
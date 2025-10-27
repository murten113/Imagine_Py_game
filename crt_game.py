import pygame
import sys
import RPi.GPIO as GPIO
from mfrc522 import MFRC522

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Display Image")

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#############
########   RC522 READER

# SPI0 uses GPIO 11 (SCK), 10 (MOSI), 9 (MISO) - hardware fixed
# SPI1 uses GPIO 21 (SCK), 20 (MOSI), 19 (MISO) - hardware fixed 

RST_PIN = 25  # Reset (Shared for all modules)

# Create an instance for each RC522 module
reader1 = MFRC522(bus=0, device=0, pin_rst=RST_PIN)  # SPI0, CE0 (GPIO 8)
reader2 = MFRC522(bus=0, device=1, pin_rst=RST_PIN)  # SPI0, CE1 (GPIO 7)
reader3 = MFRC522(bus=1, device=0, pin_rst=RST_PIN)  # SPI1, CE0 (GPIO 18)

#############
########   TEXT

font = pygame.font.Font(None, 74)

def render_text(text, font_size, color, position):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=position)
    screen.blit(text_surface, text_rect)

#############
########   MISC VISUAL

bg_image = pygame.image.load('/home/jeditor/Imagine_Py_game/images/xray.jpg')
bg_image = pygame.transform.scale(bg_image, (screen.get_width(), screen.get_height()))

black = (0, 0, 0)
gray = (169, 169, 169)
white = (255, 255, 255)

#############
########   ORGAN + TAG SETUP

class Organ:
    def __init__(self, tag, image):
        self.tag = tag
        self.image = image
        self.visible = False
    
    def check_tag(self, tag_str):
        if tag_str == self.tag:
            return True
        else: 
            return False

organs = [
    Organ("organ1",pygame.image.load('/home/jeditor/Imagine_Py_game/images/organs/obj1.png')),
    Organ("organ2",pygame.image.load('/home/jeditor/Imagine_Py_game/images/organs/obj2.png')),
    Organ("organ3",pygame.image.load('/home/jeditor/Imagine_Py_game/images/organs/obj3.png')),
    Organ("organ4",pygame.image.load('/home/jeditor/Imagine_Py_game/images/organs/obj4.png')),
    Organ("organ5",pygame.image.load('/home/jeditor/Imagine_Py_game/images/organs/obj5.png')),
    Organ("organ6",pygame.image.load('/home/jeditor/Imagine_Py_game/images/organs/obj6.png')),
    Organ("organ7",pygame.image.load('/home/jeditor/Imagine_Py_game/images/organs/obj7.png')),
    Organ("organ8",pygame.image.load('/home/jeditor/Imagine_Py_game/images/organs/obj8.png')),
    Organ("organ9",pygame.image.load('/home/jeditor/Imagine_Py_game/images/organs/obj9.png')),
]

#############
########   ORGAN TILES

class OrganTile:
    def __init__(self, x, y, flashing=False):
        self.x = x
        self.y = y
        self.size = 100
        self.default_border_width = 5
        self.flashing_border_width = 10
        self.border_width = self.default_border_width
        self.flashing = flashing
        self.show_border = True
        self.last_update_time = pygame.time.get_ticks()
        self.flash_interval = 100

    def update(self):
        if self.flashing:
            self.border_width = self.flashing_border_width
            current_time = pygame.time.get_ticks()
            if current_time - self.last_update_time >= self.flash_interval:
                self.show_border = not self.show_border
                self.last_update_time = current_time
        else:
            self.border_width = self.default_border_width

    def draw(self, screen):
        if self.show_border:
            pygame.draw.rect(screen, white, pygame.Rect(self.x - self.border_width, self.y - self.border_width, self.size + self.border_width * 2, self.size + self.border_width * 2))
        pygame.draw.rect(screen, black, pygame.Rect(self.x, self.y, self.size, self.size))

organ_tiles = [
    OrganTile(400, 100, False),
    OrganTile(500, 225, True),   #temp w/ border
    OrganTile(400, 350, False)
]

#############
########   MAIN LOOP

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:  # Right mouse button
                run = False

    screen.blit(bg_image, (0, 0))

    # Read RFID tags
    status1, TagType1 = reader1.MFRC522_Request(reader1.PICC_REQIDL)
    if status1 == reader1.MI_OK:
        print("1 yes")
        status1, uid1 = reader1.MFRC522_Anticoll()
        if status1 == reader1.MI_OK:
            tag_id1 = str(uid1[0]) + str(uid1[1]) + str(uid1[2]) + str(uid1[3])
            print(f"Reader 1: {tag_id1}")

#    status2, TagType2 = reader2.MFRC522_Request(reader2.PICC_REQIDL)
#    if status2 == reader2.MI_OK:
#        status2, uid2 = reader2.MFRC522_Anticoll()
#        if status2 == reader2.MI_OK:
#            tag_id2 = str(uid2[0]) + str(uid2[1]) + str(uid2[2]) + str(uid2[3])
#            print(f"Reader 2: {tag_id2}")

#    status3, TagType3 = reader3.MFRC522_Request(reader3.PICC_REQIDL)
#    if status3 == reader3.MI_OK:
#        status3, uid3 = reader3.MFRC522_Anticoll()
#        if status3 == reader3.MI_OK:
#            tag_id3 = str(uid3[0]) + str(uid3[1]) + str(uid3[2]) + str(uid3[3])
#            print(f"Reader 3: {tag_id3}")

    for index, tile in enumerate(organ_tiles):
        tile.update() 
        tile.draw(screen)
        
        render_text(str(index + 1) + ".", 28, (255, 255, 255), (tile.x + 8, tile.y + 10))

    pygame.display.update()

pygame.quit()
sys.exit()

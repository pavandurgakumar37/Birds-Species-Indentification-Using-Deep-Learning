from tkinter import messagebox
from tkinter import *
from tkinter import simpledialog
import tkinter
from tkinter import filedialog
import matplotlib.pyplot as plt
import datetime
import cv2
import numpy as np
import random

from tkinter.filedialog import askopenfilename

import time
import cv2
import os
import matplotlib.patches as patches


from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image

main = tkinter.Tk()
main.title("Bird Species Identification using Deep Learning")
main.geometry("1200x1200")

global filename


# Model saved with Keras model.save()
MODEL_PATH = 'birds.h5'

# Load your trained model
model = load_model(MODEL_PATH, compile=False)


lab = {0: 'AFRICAN CROWNED CRANE', 1: 'AFRICAN FIREFINCH', 2: 'ALBATROSS', 3: 'ALEXANDRINE PARAKEET', 4: 'AMERICAN AVOCET', 5: 'AMERICAN BITTERN', 6: 'AMERICAN COOT', 7: 'AMERICAN GOLDFINCH', 8: 'AMERICAN KESTREL', 9: 'AMERICAN PIPIT', 10: 'AMERICAN REDSTART', 11: 'ANHINGA', 12: 'ANNAS HUMMINGBIRD', 13: 'ANTBIRD', 14: 'ARARIPE MANAKIN', 15: 'ASIAN CRESTED IBIS', 16: 'BALD EAGLE', 17: 'BALI STARLING', 18: 'BALTIMORE ORIOLE', 19: 'BANANAQUIT', 20: 'BANDED BROADBILL', 21: 'BAR-TAILED GODWIT', 22: 'BARN OWL', 23: 'BARN SWALLOW', 24: 'BARRED PUFFBIRD', 25: 'BAY-BREASTED WARBLER', 26: 'BEARDED BARBET', 27: 'BEARDED REEDLING', 28: 'BELTED KINGFISHER', 29: 'BIRD OF PARADISE', 30: 'BLACK & YELLOW bROADBILL', 31: 'BLACK FRANCOLIN', 32: 'BLACK SKIMMER', 33: 'BLACK SWAN', 34: 'BLACK TAIL CRAKE', 35: 'BLACK THROATED BUSHTIT', 36: 'BLACK THROATED WARBLER', 37: 'BLACK VULTURE', 38: 'BLACK-CAPPED CHICKADEE', 39: 'BLACK-NECKED GREBE', 40: 'BLACK-THROATED SPARROW', 41: 'BLACKBURNIAM WARBLER', 42: 'BLUE GROUSE', 43: 'BLUE HERON', 44: 'BOBOLINK', 45: 'BORNEAN BRISTLEHEAD', 46: 'BORNEAN LEAFBIRD', 47: 'BROWN NOODY', 48: 'BROWN THRASHER', 49: 'BULWERS PHEASANT', 50: 'CACTUS WREN', 51: 'CALIFORNIA CONDOR', 52: 'CALIFORNIA GULL', 53: 'CALIFORNIA QUAIL', 54: 'CANARY', 55: 'CAPE MAY WARBLER', 56: 'CAPUCHINBIRD', 57: 'CARMINE BEE-EATER', 58: 'CASPIAN TERN', 59: 'CASSOWARY', 60: 'CEDAR WAXWING', 61: 'CHARA DE COLLAR', 62: 'CHIPPING SPARROW', 63: 'CHUKAR PARTRIDGE', 64: 'CINNAMON TEAL', 65: 'COCK OF THE  ROCK', 66: 'COCKATOO', 67: 'COMMON FIRECREST', 68: 'COMMON GRACKLE', 69: 'COMMON HOUSE MARTIN', 70: 'COMMON LOON', 71: 'COMMON POORWILL', 72: 'COMMON STARLING', 73: 'COUCHS KINGBIRD', 74: 'CRESTED AUKLET', 75: 'CRESTED CARACARA', 76: 'CRESTED NUTHATCH', 77: 'CROW', 78: 'CROWNED PIGEON', 79: 'CUBAN TODY', 80: 'CURL CRESTED ARACURI', 81: 'D-ARNAUDS BARBET', 82: 'DARK EYED JUNCO', 83: 'DOUBLE BARRED FINCH', 84: 'DOWNY WOODPECKER', 85: 'EASTERN BLUEBIRD', 86: 'EASTERN MEADOWLARK', 87: 'EASTERN ROSELLA', 88: 'EASTERN TOWEE', 89: 'ELEGANT TROGON', 90: 'ELLIOTS  PHEASANT', 91: 'EMPEROR PENGUIN', 92: 'EMU', 93: 'ENGGANO MYNA', 94: 'EURASIAN GOLDEN ORIOLE', 95: 'EURASIAN MAGPIE', 96: 'EVENING GROSBEAK', 97: 'FIRE TAILLED MYZORNIS', 98: 'FLAME TANAGER', 99: 'FLAMINGO', 100: 'FRIGATE', 101: 'GAMBELS QUAIL', 102: 'GANG GANG COCKATOO', 103: 'GILA WOODPECKER', 104: 'GILDED FLICKER', 105: 'GLOSSY IBIS', 106: 'GO AWAY BIRD', 107: 'GOLD WING WARBLER', 108: 'GOLDEN CHEEKED WARBLER', 109: 'GOLDEN CHLOROPHONIA', 110: 'GOLDEN EAGLE', 111: 'GOLDEN PHEASANT', 112: 'GOLDEN PIPIT', 113: 'GOULDIAN FINCH', 114: 'GRAY CATBIRD', 115: 'GRAY PARTRIDGE', 116: 'GREAT POTOO', 117: 'GREATOR SAGE GROUSE', 118: 'GREEN JAY', 119: 'GREEN MAGPIE', 120: 'GREY PLOVER', 121: 'GUINEA TURACO', 122: 'GUINEAFOWL', 123: 'GYRFALCON', 124: 'HARPY EAGLE', 125: 'HAWAIIAN GOOSE', 126: 'HELMET VANGA', 127: 'HIMALAYAN MONAL', 128: 'HOATZIN', 129: 'HOODED MERGANSER', 130: 'HOOPOES', 131: 'HORNBILL', 132: 'HORNED GUAN', 133: 'HORNED SUNGEM', 134: 'HOUSE FINCH', 135: 'HOUSE SPARROW', 136: 'IMPERIAL SHAQ', 137: 'INCA TERN', 138: 'INDIAN BUSTARD', 139: 'INDIAN PITTA', 140: 'INDIGO BUNTING', 141: 'JABIRU', 142: 'JAVA SPARROW', 143: 'KAKAPO', 144: 'KILLDEAR', 145: 'KING VULTURE', 146: 'KIWI', 147: 'KOOKABURRA', 148: 'LARK BUNTING', 149: 'LEARS MACAW', 150: 'LILAC ROLLER', 151: 'LONG-EARED OWL', 152: 'MAGPIE GOOSE', 153: 'MALABAR HORNBILL', 154: 'MALACHITE KINGFISHER', 155: 'MALEO', 156: 'MALLARD DUCK', 157: 'MANDRIN DUCK', 158: 'MARABOU STORK', 159: 'MASKED BOOBY', 160: 'MASKED LAPWING', 161: 'MIKADO  PHEASANT', 162: 'MOURNING DOVE', 163: 'MYNA', 164: 'NICOBAR PIGEON', 165: 'NOISY FRIARBIRD', 166: 'NORTHERN BALD IBIS', 167: 'NORTHERN CARDINAL', 168: 'NORTHERN FLICKER', 169: 'NORTHERN GANNET', 170: 'NORTHERN GOSHAWK', 171: 'NORTHERN JACANA', 172: 'NORTHERN MOCKINGBIRD', 173: 'NORTHERN PARULA', 174: 'NORTHERN RED BISHOP', 175: 'NORTHERN SHOVELER', 176: 'OCELLATED TURKEY', 177: 'OKINAWA RAIL', 178: 'OSPREY', 179: 'OSTRICH', 180: 'OYSTER CATCHER', 181: 'PAINTED BUNTIG', 182: 'PALILA', 183: 'PARADISE TANAGER', 184: 'PARUS MAJOR', 185: 'PEACOCK', 186: 'PELICAN', 187: 'PEREGRINE FALCON', 188: 'PHILIPPINE EAGLE', 189: 'PINK ROBIN', 190: 'PUFFIN', 191: 'PURPLE FINCH', 192: 'PURPLE GALLINULE', 193: 'PURPLE MARTIN', 194: 'PURPLE SWAMPHEN', 195: 'QUETZAL', 196: 'RAINBOW LORIKEET', 197: 'RAZORBILL', 198: 'RED BEARDED BEE EATER', 199: 'RED BELLIED PITTA', 200: 'RED BROWED FINCH', 201: 'RED FACED CORMORANT', 202: 'RED FACED WARBLER', 203: 'RED HEADED DUCK', 204: 'RED HEADED WOODPECKER', 205: 'RED HONEY CREEPER', 206: 'RED TAILED THRUSH', 207: 'RED WINGED BLACKBIRD', 208: 'RED WISKERED BULBUL', 209: 'REGENT BOWERBIRD', 210: 'RING-NECKED PHEASANT', 211: 'ROADRUNNER', 212: 'ROBIN', 213: 'ROCK DOVE', 214: 'ROSY FACED LOVEBIRD', 215: 'ROUGH LEG BUZZARD', 216: 'ROYAL FLYCATCHER', 217: 'RUBY THROATED HUMMINGBIRD', 218: 'RUFOUS KINGFISHER', 219: 'RUFUOS MOTMOT', 220: 'SAMATRAN THRUSH', 221: 'SAND MARTIN', 222: 'SCARLET IBIS', 223: 'SCARLET MACAW', 224: 'SHOEBILL', 225: 'SHORT BILLED DOWITCHER', 226: 'SMITHS LONGSPUR', 227: 'SNOWY EGRET', 228: 'SNOWY OWL', 229: 'SORA', 230: 'SPANGLED COTINGA', 231: 'SPLENDID WREN', 232: 'SPOON BILED SANDPIPER', 233: 'SPOONBILL', 234: 'SRI LANKA BLUE MAGPIE', 235: 'STEAMER DUCK', 236: 'STORK BILLED KINGFISHER', 237: 'STRAWBERRY FINCH', 238: 'STRIPPED SWALLOW', 239: 'SUPERB STARLING', 240: 'SWINHOES PHEASANT', 241: 'TAIWAN MAGPIE', 242: 'TAKAHE', 243: 'TASMANIAN HEN', 244: 'TEAL DUCK', 245: 'TIT MOUSE', 246: 'TOUCHAN', 247: 'TOWNSENDS WARBLER', 248: 'TREE SWALLOW', 249: 'TRUMPTER SWAN', 250: 'TURKEY VULTURE', 251: 'TURQUOISE MOTMOT', 252: 'UMBRELLA BIRD', 253: 'VARIED THRUSH', 254: 'VENEZUELIAN TROUPIAL', 255: 'VERMILION FLYCATHER', 256: 'VICTORIA CROWNED PIGEON', 257: 'VIOLET GREEN SWALLOW', 258: 'VULTURINE GUINEAFOWL', 259: 'WATTLED CURASSOW', 260: 'WHIMBREL', 261: 'WHITE CHEEKED TURACO', 262: 'WHITE NECKED RAVEN', 263: 'WHITE TAILED TROPIC', 264: 'WILD TURKEY', 265: 'WILSONS BIRD OF PARADISE', 266: 'WOOD DUCK', 267: 'YELLOW BELLIED FLOWERPECKER', 268: 'YELLOW CACIQUE', 269: 'YELLOW HEADED BLACKBIRD'}

def model_predict():
    global image_names,distances
    img_path = filename
    img=image.load_img(img_path,target_size=(224,224,3))

    # Preprocessing the image
    img=image.img_to_array(img)
    img=img/255
    img=np.expand_dims(img,[0])
    
    # Be careful how your trained model deals with the input
    # otherwise, it won't make correct prediction!
    answer=model.predict(img)
    y_class = answer.argmax(axis=-1)
    print(y_class)
    y = " ".join(str(x) for x in y_class)
    y = int(y)
    res = lab[y]

    dataset = './birds/train/'
    filepath = os.path.join(dataset,res)
    print(filepath)
    imagenames = os.listdir(filepath)
    #print(imagenames)

    filenames_complete_path = []
    image_names = []
    cv2_names = []
    for i in range(6):
        imagename = random.choice(imagenames)
        #imagepath = os.path.join(filepath,imagename)
        #print(imagename)
        #print(filepath+'/'+imagename)
        image_names.append(imagename)
        p = filepath+'/'+imagename
        filenames_complete_path.append(p)
        c = cv2.imread(filenames_complete_path[i])
        cv2_names.append(c)
        #print(filenames_complete_path)
    distances = []
    for i in range(4):
        distance1 = calculateDistance(img,cv2_names[i])
        distances.append(distance1)
    

    print(distances)
    # setting values to rows and column variables
    rows = 2
    columns = 2
    fig = plt.figure(figsize=(10, 7))

    for i in range(1,5):
        # Adds a subplot at the 1st position
        fig.add_subplot(rows, columns, i)

        # showing image
        plt.imshow(cv2_names[i])
        plt.axis('off')
        plt.title(res)
    plt.show()
    
    return res
   
def upload():
   
    global filename
    filename = askopenfilename(initialdir = "./birds/test/")
    pathlabel.config(text=filename)
    



def calculateDistance(i1, i2):
    return np.sum((i1-i2)**2)

def scoreGraph():
    global image_names,distances
    y_pos = np.arange(len(image_names)-2)
    plt.bar(y_pos, distances)
    plt.xticks(y_pos, image_names)
    plt.show()

font = ('times', 20, 'bold')
title = Label(main, text='Bird Species Identification using Deep Learning')
title.config(bg='brown', fg='white')  
title.config(font=font)           
title.config(height=3, width=80)       
title.place(x=5,y=5)

font1 = ('times', 14, 'bold')
upload = Button(main, text="Upload Bird Image", command=upload)
upload.place(x=50,y=100)
upload.config(font=font1)  

pathlabel = Label(main)
pathlabel.config(bg='brown', fg='white')  
pathlabel.config(font=font1)           
pathlabel.place(x=300,y=100)

depthbutton = Button(main, text="Run DCNN Algorithm & View Identified Species", command=model_predict)
depthbutton.place(x=50,y=150)
depthbutton.config(font=font1) 


viewresults = Button(main, text="View Score Graph", command=scoreGraph)
viewresults.place(x=50,y=200)
viewresults.config(font=font1) 

main.config(bg='brown')
main.mainloop()
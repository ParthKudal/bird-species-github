from flask import Flask , render_template, url_for, request

import keras
from keras.preprocessing import image
from keras import models
import numpy as np
from keras.applications.vgg16 import preprocess_input


app = Flask(__name__)


@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/',methods=['POST'])
def predict():
    imagefile = request.files['imagefile']
    image_path = "../images" + imagefile.filename
    imagefile.save(image_path)
    

    label = {0: 'AFRICAN CROWNED CRANE',
            1: 'AFRICAN FIREFINCH',
            2: 'ALBATROSS',
            3: 'ALEXANDRINE PARAKEET',
            4: 'AMERICAN AVOCET',
            5: 'AMERICAN BITTERN',
            6: 'AMERICAN COOT',
            7: 'AMERICAN GOLDFINCH',
            8: 'AMERICAN KESTREL',
            9: 'AMERICAN PIPIT',
            10: 'AMERICAN REDSTART',
            11: 'ANHINGA',
            12: 'ANNAS HUMMINGBIRD',
            13: 'ANTBIRD',
            14: 'ARARIPE MANAKIN',
            15: 'ASIAN CRESTED IBIS',
            16: 'BALD EAGLE',
            17: 'BALD IBIS',
            18: 'BALI STARLING',
            19: 'BALTIMORE ORIOLE',
            20: 'BANANAQUIT',
            21: 'BANDED BROADBILL',
            22: 'BANDED PITA',
            23: 'BAR-TAILED GODWIT',
            24: 'BARN OWL',
            25: 'BARN SWALLOW',
            26: 'BARRED PUFFBIRD',
            27: 'BAY-BREASTED WARBLER',
            28: 'BEARDED BARBET',
            29: 'BEARDED BELLBIRD',
            30: 'BEARDED REEDLING',
            31: 'BELTED KINGFISHER',
            32: 'BIRD OF PARADISE',
            33: 'BLACK & YELLOW bROADBILL',
            34: 'BLACK FRANCOLIN',
            35: 'BLACK SKIMMER',
            36: 'BLACK SWAN',
            37: 'BLACK TAIL CRAKE',
            38: 'BLACK THROATED BUSHTIT',
            39: 'BLACK THROATED WARBLER',
            40: 'BLACK VULTURE',
            41: 'BLACK-CAPPED CHICKADEE',
            42: 'BLACK-NECKED GREBE',
            43: 'BLACK-THROATED SPARROW',
            44: 'BLACKBURNIAM WARBLER',
            45: 'BLONDE CRESTED WOODPECKER',
            46: 'BLUE GROUSE',
            47: 'BLUE HERON',
            48: 'BOBOLINK',
            49: 'BORNEAN BRISTLEHEAD',
            50: 'BORNEAN LEAFBIRD',
            51: 'BORNEAN PHEASANT',
            52: 'BROWN CREPPER',
            53: 'BROWN NOODY',
            54: 'BROWN THRASHER',
            55: 'BULWERS PHEASANT',
            56: 'CACTUS WREN',
            57: 'CALIFORNIA CONDOR',
            58: 'CALIFORNIA GULL',
            59: 'CALIFORNIA QUAIL',
            60: 'CANARY',
            61: 'CAPE MAY WARBLER',
            62: 'CAPPED HERON',
            63: 'CAPUCHINBIRD',
            64: 'CARMINE BEE-EATER',
            65: 'CASPIAN TERN',
            66: 'CASSOWARY',
            67: 'CEDAR WAXWING',
            68: 'CERULEAN WARBLER',
            69: 'CHARA DE COLLAR',
            70: 'CHIPPING SPARROW',
            71: 'CHUKAR PARTRIDGE',
            72: 'CINNAMON TEAL',
            73: 'CLARKS NUTCRACKER',
            74: 'COCK OF THE  ROCK',
            75: 'COCKATOO',
            76: 'COLLARED ARACARI',
            77: 'COMMON FIRECREST',
            78: 'COMMON GRACKLE',
            79: 'COMMON HOUSE MARTIN',
            80: 'COMMON LOON',
            81: 'COMMON POORWILL',
            82: 'COMMON STARLING',
            83: 'COUCHS KINGBIRD',
            84: 'CRESTED AUKLET',
            85: 'CRESTED CARACARA',
            86: 'CRESTED NUTHATCH',
            87: 'CRIMSON SUNBIRD',
            88: 'CROW',
            89: 'CROWNED PIGEON',
            90: 'CUBAN TODY',
            91: 'CUBAN TROGON',
            92: 'CURL CRESTED ARACURI',
            93: 'D-ARNAUDS BARBET',
            94: 'DARK EYED JUNCO',
            95: 'DOUBLE BARRED FINCH',
            96: 'DOUBLE BRESTED CORMARANT',
            97: 'DOWNY WOODPECKER',
            98: 'EASTERN BLUEBIRD',
            99: 'EASTERN MEADOWLARK',
            100: 'EASTERN ROSELLA',
            101: 'EASTERN TOWEE',
            102: 'ELEGANT TROGON',
            103: 'ELLIOTS  PHEASANT',
            104: 'EMPEROR PENGUIN',
            105: 'EMU',
            106: 'ENGGANO MYNA',
            107: 'EURASIAN GOLDEN ORIOLE',
            108: 'EURASIAN MAGPIE',
            109: 'EVENING GROSBEAK',
            110: 'FAIRY BLUEBIRD',
            111: 'FIRE TAILLED MYZORNIS',
            112: 'FLAME TANAGER',
            113: 'FLAMINGO',
            114: 'FRIGATE',
            115: 'GAMBELS QUAIL',
            116: 'GANG GANG COCKATOO',
            117: 'GILA WOODPECKER',
            118: 'GILDED FLICKER',
            119: 'GLOSSY IBIS',
            120: 'GO AWAY BIRD',
            121: 'GOLD WING WARBLER',
            122: 'GOLDEN CHEEKED WARBLER',
            123: 'GOLDEN CHLOROPHONIA',
            124: 'GOLDEN EAGLE',
            125: 'GOLDEN PHEASANT',
            126: 'GOLDEN PIPIT',
            127: 'GOULDIAN FINCH',
            128: 'GRAY CATBIRD',
            129: 'GRAY PARTRIDGE',
            130: 'GREAT POTOO',
            131: 'GREATOR SAGE GROUSE',
            132: 'GREEN BROADBILL',
            133: 'GREEN JAY',
            134: 'GREEN MAGPIE',
            135: 'GREY PLOVER',
            136: 'GUINEA TURACO',
            137: 'GUINEAFOWL',
            138: 'GYRFALCON',
            139: 'HARPY EAGLE',
            140: 'HAWAIIAN GOOSE',
            141: 'HELMET VANGA',
            142: 'HIMALAYAN MONAL',
            143: 'HOATZIN',
            144: 'HOODED MERGANSER',
            145: 'HOOPOES',
            146: 'HORNBILL',
            147: 'HORNED GUAN',
            148: 'HORNED LARK',
            149: 'HORNED SUNGEM',
            150: 'HOUSE FINCH',
            151: 'HOUSE SPARROW',
            152: 'IMPERIAL SHAQ',
            153: 'INCA TERN',
            154: 'INDIAN BUSTARD',
            155: 'INDIAN PITTA',
            156: 'INDIGO BUNTING',
            157: 'JABIRU',
            158: 'JAVA SPARROW',
            159: 'KAGU',
            160: 'KAKAPO',
            161: 'KILLDEAR',
            162: 'KING VULTURE',
            163: 'KIWI',
            164: 'KOOKABURRA',
            165: 'LARK BUNTING',
            166: 'LEARS MACAW',
            167: 'LILAC ROLLER',
            168: 'LONG-EARED OWL',
            169: 'MAGPIE GOOSE',
            170: 'MALABAR HORNBILL',
            171: 'MALACHITE KINGFISHER',
            172: 'MALAGASY WHITE EYE',
            173: 'MALEO',
            174: 'MALLARD DUCK',
            175: 'MANDRIN DUCK',
            176: 'MARABOU STORK',
            177: 'MASKED BOOBY',
            178: 'MASKED LAPWING',
            179: 'MIKADO  PHEASANT',
            180: 'MOURNING DOVE',
            181: 'MYNA',
            182: 'NICOBAR PIGEON',
            183: 'NOISY FRIARBIRD',
            184: 'NORTHERN BALD IBIS',
            185: 'NORTHERN CARDINAL',
            186: 'NORTHERN FLICKER',
            187: 'NORTHERN GANNET',
            188: 'NORTHERN GOSHAWK',
            189: 'NORTHERN JACANA',
            190: 'NORTHERN MOCKINGBIRD',
            191: 'NORTHERN PARULA',
            192: 'NORTHERN RED BISHOP',
            193: 'NORTHERN SHOVELER',
            194: 'OCELLATED TURKEY',
            195: 'OKINAWA RAIL',
            196: 'ORANGE BRESTED BUNTING',
            197: 'OSPREY',
            198: 'OSTRICH',
            199: 'OVENBIRD',
            200: 'OYSTER CATCHER',
            201: 'PAINTED BUNTIG',
            202: 'PALILA',
            203: 'PARADISE TANAGER',
            204: 'PARAKETT  AKULET',
            205: 'PARUS MAJOR',
            206: 'PEACOCK',
            207: 'PELICAN',
            208: 'PEREGRINE FALCON',
            209: 'PHILIPPINE EAGLE',
            210: 'PINK ROBIN',
            211: 'PUFFIN',
            212: 'PURPLE FINCH',
            213: 'PURPLE GALLINULE',
            214: 'PURPLE MARTIN',
            215: 'PURPLE SWAMPHEN',
            216: 'PYGMY KINGFISHER',
            217: 'QUETZAL',
            218: 'RAINBOW LORIKEET',
            219: 'RAZORBILL',
            220: 'RED BEARDED BEE EATER',
            221: 'RED BELLIED PITTA',
            222: 'RED BROWED FINCH',
            223: 'RED FACED CORMORANT',
            224: 'RED FACED WARBLER',
            225: 'RED HEADED DUCK',
            226: 'RED HEADED WOODPECKER',
            227: 'RED HONEY CREEPER',
            228: 'RED NAPED TROGON',
            229: 'RED TAILED HAWK',
            230: 'RED TAILED THRUSH',
            231: 'RED WINGED BLACKBIRD',
            232: 'RED WISKERED BULBUL',
            233: 'REGENT BOWERBIRD',
            234: 'RING-NECKED PHEASANT',
            235: 'ROADRUNNER',
            236: 'ROBIN',
            237: 'ROCK DOVE',
            238: 'ROSY FACED LOVEBIRD',
            239: 'ROUGH LEG BUZZARD',
            240: 'ROYAL FLYCATCHER',
            241: 'RUBY THROATED HUMMINGBIRD',
            242: 'RUDY KINGFISHER',
            243: 'RUFOUS KINGFISHER',
            244: 'RUFUOS MOTMOT',
            245: 'SAMATRAN THRUSH',
            246: 'SAND MARTIN',
            247: 'SANDHILL CRANE',
            248: 'SCARLET IBIS',
            249: 'SCARLET MACAW',
            250: 'SCARLET TANAGER',
            251: 'SHOEBILL',
            252: 'SHORT BILLED DOWITCHER',
            253: 'SMITHS LONGSPUR',
            254: 'SNOWY EGRET',
            255: 'SNOWY OWL',
            256: 'SORA',
            257: 'SPANGLED COTINGA',
            258: 'SPLENDID WREN',
            259: 'SPOON BILED SANDPIPER',
            260: 'SPOONBILL',
            261: 'SRI LANKA BLUE MAGPIE',
            262: 'STEAMER DUCK',
            263: 'STORK BILLED KINGFISHER',
            264: 'STRAWBERRY FINCH',
            265: 'STRIPPED MANAKIN',
            266: 'STRIPPED SWALLOW',
            267: 'SUPERB STARLING',
            268: 'SWINHOES PHEASANT',
            269: 'TAIWAN MAGPIE',
            270: 'TAKAHE',
            271: 'TASMANIAN HEN',
            272: 'TEAL DUCK',
            273: 'TIT MOUSE',
            274: 'TOUCHAN',
            275: 'TOWNSENDS WARBLER',
            276: 'TREE SWALLOW',
            277: 'TRUMPTER SWAN',
            278: 'TURKEY VULTURE',
            279: 'TURQUOISE MOTMOT',
            280: 'UMBRELLA BIRD',
            281: 'VARIED THRUSH',
            282: 'VENEZUELIAN TROUPIAL',
            283: 'VERMILION FLYCATHER',
            284: 'VICTORIA CROWNED PIGEON',
            285: 'VIOLET GREEN SWALLOW',
            286: 'VULTURINE GUINEAFOWL',
            287: 'WALL CREAPER',
            288: 'WATTLED CURASSOW',
            289: 'WHIMBREL',
            290: 'WHITE CHEEKED TURACO',
            291: 'WHITE NECKED RAVEN',
            292: 'WHITE TAILED TROPIC',
            293: 'WHITE THROATED BEE EATER',
            294: 'WILD TURKEY',
            295: 'WILSONS BIRD OF PARADISE',
            296: 'WOOD DUCK',
            297: 'YELLOW BELLIED FLOWERPECKER',
            298: 'YELLOW CACIQUE',
            299: 'YELLOW HEADED BLACKBIRD'}

    

    model = keras.models.load_model('D:/sdp/vgg16_model.h5',compile=True)


    img = image.load_img(image_path,color_mode='rgb', target_size=(224, 224))
    x = image.img_to_array(img)
    x.shape
    #Adding the fouth dimension, for number of images
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    features = model.predict(x)
    classes = np.argmax(features, axis = 1)
    result = label[int(classes)]



    return render_template('index.html',prediction = result)


if __name__ == "__main__":
    app.run(debug =True) 

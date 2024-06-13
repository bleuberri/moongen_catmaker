import pygame
import pygame_gui
from bidict import bidict

# Start PyGame
pygame.init()
screen_x, screen_y = 800, 700
SCREEN = pygame.display.set_mode((screen_x, screen_y))
MANAGER = pygame_gui.ui_manager.UIManager((screen_x, screen_y), 'resources/defaults.json', enable_live_theme_updates=False)

MANAGER.get_theme().load_theme('resources/defaults.json')
MANAGER.get_theme().load_theme('resources/buttons.json')
MANAGER.get_theme().load_theme('resources/text_boxes.json')
MANAGER.get_theme().load_theme('resources/text_boxes.json')


import scripts.cat.cats

CREATED_CAT = scripts.cat.cats.Cat()


def sort_bidict(d: bidict, first_element=None):
    """Sorts Dictionary alphbetically. If None if in the dictionary, always have that first. """

    temp = bidict({})
    if first_element in d:
        temp[first_element] = d[first_element]
        del d[first_element]

    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))
    temp.update(sorted_dict)
    return temp


pelt_options = bidict({"SingleColour": "Plain",  "Smoke": "Smoke", 'Singlestripe': "Single Stripe", 'Tabby': "Tabby",
                       'Ticked': "Ticked Tabby", 'Mackerel': "Mackerel Tabby", 'Classic': "Classic Tabby",
                       'Sokoke': 'Sokoke', 'Agouti': "Agouti", "Speckled": "Speckled Tabby", "Rosette": "Rosette",
                       "Bengal": "Bengal", "Marbled": "Marbled Tabby", "Masked": "Masked Tabby", 
                       'Dotted': "Dotted", 'Striped': "Striped", 'Wildcat': "Wildcat", 'Cheetah': "Cheetah", 
                       'Lynx': "Lynx", 'Ocelot': "Ocelot", 'Bobtail': "Bobtail", 'Manedwolf': "Maned Wolf"})
pelt_options = sort_bidict(pelt_options)

tortie_patches_patterns = bidict({"single": "Plain", "tabby": "Tabby", "bengal": "Bengal", "marbled": "Marbled Tabby",
                                  "ticked": "Ticked Tabby", "rosette": "Rosette", "smoke": "Smoke",
                                  "speckled": "Speckled Tabby", "agouti": "Agouti", "classic": "Classic Tabby",
                                  "mackerel": "Mackerel Tabby", "sokoke": "Sokoke", 
                                  "dotted": "Dotted", "striped": "Striped", "wildcat": "Wildcat", "cheetah": "Cheetah", 
                                  "lynx": "Lynx", "ocelot": "Ocelot", "bobtail": "Bobtail", "manedwolf": "Maned Wolf"})
tortie_patches_patterns = sort_bidict(tortie_patches_patterns)

tortie_patches_shapes = bidict({"ONE": "One", "TWO": "Two", "THREE": "Three", "FOUR": "Four",  'REDTAIL': "Redtail",
                                'DELILAH': "Delilah", 'MINIMALONE': "Minimal 1", 'MINIMALTWO': "Minimal 2",
                                'MINIMALTHREE': "Minimal 3", 'MINIMALFOUR': "Minimal 4", 'OREO': "Oreo", 'SWOOP': "Swoop",
                                'MOTTLED': "Mottled", 'SIDEMASK': "Sidemask", 'EYEDOT': "Eye dot",
                                'BANDANA': "Bandana", 'PACMAN': "Pacman", 'STREAMSTRIKE': "Streamstrike",
                                'ORIOLE': "Oriole", 'ROBIN': "Robin", 'BRINDLE': "Brindle", 'PAIGE': "Paige", 
                                "ROSETAIL": "Rosetail", "SAFI": "Safi", "HALF": "Half", "CHIMERA": "Chimera", 
                                "SMUDGED": "Smudged", "DAUB": "Daub", "DAPPLENIGHT": "Dapplenight", "STREAK": "Streak", 
                                "MASK": "Mask", "CHEST": "Chest", "ARMTAIL": "Armtail", "EMBER": "Ember", "SMOKE": "Smoke", 
                                "GRUMPYFACE": "Grumpy Face", "BRIE": "Brie", "BELOVED": "Beloved", "SHILOH" : "Shiloh", 
                                "BODY" : "Body", 'MINKFULLWHITE': 'Minkfullwhite', 'MINKANY': 'Minkany', 'MINKTUXEDO': 'Minktuxedo', 
                                'MINKLITTLE': 'Minklittle', 'MINKCOLOURPOINT': 'Minkcolourpoint', 'MINKVAN': 'Minkvan', 
                                'MINKANYTWO': 'Minkanytwo', 'MINKMOON': 'Minkmoon', 'MINKPHANTOM': 'Minkphantom', 
                                'MINKPOWDER': 'Minkpowder', 'MINKBLEACHED': 'Minkbleached', 'MINKSAVANNAH': 'Minksavannah', 
                                'MINKFADESPOTS': 'Minkfadespots', 'MINKPEBBLESHINE': 'Minkpebbleshine', 'MINKEXTRA': 'Minkextra', 
                                'MINKONEEAR': 'Minkoneear', 'MINKBROKEN': 'Minkbroken', 'MINKLIGHTTUXEDO': 'Minklighttuxedo', 
                                'MINKBUZZARDFANG': 'Minkbuzzardfang', 'MINKRAGDOLL': 'Minkragdoll', 'MINKLIGHTSONG': 'Minklightsong', 
                                'MINKVITILIGO': 'Minkvitiligo', 'MINKBLACKSTAR': 'Minkblackstar', 'MINKPIEBALD': 'Minkpiebald', 
                                'MINKCURVED': 'Minkcurved', 'MINKPETAL': 'Minkpetal', 'MINKSHIBAINU': 'Minkshibainu', 'MINKOWL': 'Minkowl', 
                                'MINKTIP': 'Minktip', 'MINKFANCY': 'Minkfancy', 'MINKFRECKLES': 'Minkfreckles', 'MINKRINGTAIL': 'Minkringtail', 
                                'MINKHALFFACE': 'Minkhalfface', 'MINKPANTSTWO': 'Minkpantstwo', 'MINKGOATEE': 'Minkgoatee', 
                                'MINKVITILIGOTWO': 'Minkvitiligotwo', 'MINKPAWS': 'Minkpaws', 'MINKMITAINE': 'Minkmitaine', 
                                'MINKBROKENBLAZE': 'Minkbrokenblaze', 'MINKSCOURGE': 'Minkscourge', 'MINKDIVA': 'Minkdiva', 
                                'MINKBEARD': 'Minkbeard', 'MINKTAIL': 'Minktail', 'MINKBLAZE': 'Minkblaze', 'MINKPRINCE': 'Minkprince', 
                                'MINKBIB': 'Minkbib', 'MINKVEE': 'Minkvee', 'MINKUNDERS': 'Minkunders', 'MINKHONEY': 'Minkhoney', 
                                'MINKFAROFA': 'Minkfarofa', 'MINKDAMIEN': 'Minkdamien', 'MINKMISTER': 'Minkmister', 
                                'MINKBELLY': 'Minkbelly', 'MINKTAILTIP': 'Minktailtip', 'MINKTOES': 'Minktoes', 'MINKTOPCOVER': 'Minktopcover', 
                                'MINKAPRON': 'Minkapron', 'MINKCAPSADDLE': 'Minkcapsaddle', 'MINKMASKMANTLE': 'Minkmaskmantle', 
                                'MINKSQUEAKS': 'Minksqueaks', 'MINKSTAR': 'Minkstar', 'MINKTOESTAIL': 'Minktoestail', 
                                'MINKRAVENPAW': 'Minkravenpaw', 'MINKPANTS': 'Minkpants', 'MINKREVERSEPANTS': 'Minkreversepants', 
                                'MINKSKUNK': 'Minkskunk', 'MINKKARPATI': 'Minkkarpati', 'MINKHALFWHITE': 'Minkhalfwhite', 
                                'MINKAPPALOOSA': 'Minkappaloosa', 'MINKDAPPLEPAW': 'Minkdapplepaw', 'MINKHEART': 'Minkheart', 
                                'MINKLILTWO': 'Minkliltwo', 'MINKGLASS': 'Minkglass', 'MINKMOORISH': 'Minkmoorish', 
                                'MINKSEPIAPOINT': 'Minksepiapoint', 'MINKMINKPOINT': 'MinkMinkpoint', 
                                'MINKSEALPOINT': 'Minksealpoint', 'MINKMAO': 'Minkmao', 'MINKLUNA': 'Minkluna', 
                                'MINKCHESTSPECK': 'Minkchestspeck', 'MINKWINGS': 'Minkwings', 'MINKPAINTED': 'Minkpainted',
                                'MINKHEARTTWO': 'Minkhearttwo', 'MINKWOODPECKER': 'Minkwoodpecker', 'MINKBOOTS': 'Minkboots', 
                                'MINKMISS': 'Minkmiss', 'MINKCOW': 'Minkcow', 'MINKCOWTWO': 'Minkcowtwo', 'MINKBUB': 'Minkbub', 
                                'MINKBOWTIE': 'Minkbowtie', 'MINKMUSTACHE': 'Minkmustache', 'MINKREVERSEHEART': 'Minkreverseheart', 
                                'MINKSPARROW': 'Minksparrow', 'MINKVEST': 'Minkvest', 'MINKLOVEBUG': 'Minklovebug',
                                'MINKTRIXIE': 'Minktrixie', 'MINKSAMMY': 'Minksammy', 'MINKSPARKLE': 'Minksparkle', 
                                'MINKRIGHTEAR': 'Minkrightear', 'MINKLEFTEAR': 'Minkleftear', 'MINKESTRELLA': 'Minkestrella', 
                                'MINKSHOOTINGSTAR': 'Minkshootingstar', 'MINKEYESPOT': 'Minkeyespot', 
                                'MINKREVERSEEYE': 'Minkreverseeye', 'MINKFADEBELLY': 'Minkfadebelly', 'MINKFRONT': 'Minkfront', 
                                'MINKBLOSSOMSTEP': 'Minkblossomstep', 'MINKPEBBLE': 'Minkpebble', 'MINKTAILTWO': 'Minktailtwo', 
                                'MINKBUDDY': 'Minkbuddy', 'MINKBACKSPOT': 'Minkbackspot', 'MINKEYEBAGS': 'Minkeyebags', 
                                'MINKBULLSEYE': 'Minkbullseye', 'MINKFINN': 'Minkfinn', 'MINKDIGIT': 'Minkdigit', 
                                'MINKKROPKA': 'Minkkropka', 'MINKFCTWO': 'Minkfctwo', 'MINKFCONE': 'Minkfcone', 
                                'MINKMIA': 'Minkmia', 'MINKSCAR': 'Minkscar', 'MINKBUSTER': 'Minkbuster', 
                                'MINKSMOKEY': 'Minksmokey', 'MINKHAWKBLAZE': 'Minkhawkblaze', 'MINKCAKE': 'Minkcake', 
                                'MINKROSINA': 'Minkrosina', 'MINKPRINCESS': 'Minkprincess', 'MINKLOCKET': 'Minklocket', 
                                'MINKBLAZEMASK': 'Minkblazemask', 'MINKTEARS': 'Minktears', 'MINKDOUGIE': 'Minkdougie'})
tortie_patches_shapes = sort_bidict(tortie_patches_shapes)

eye_colors = bidict({'YELLOW': "Yellow", 'AMBER': "Amber", 'HAZEL': "Hazel", 'PALEGREEN': "Pale Green",
                      'GREEN': "Green", 'BLUE': "Blue", 'DARKBLUE': "Dark Blue", 'GREY': "Grey", 'CYAN': "Cyan",
                      'EMERALD': "Emerald", 'PALEBLUE': "Pale Blue", 'PALEYELLOW': "Pale Yellow", 'GOLD': "Gold",
                      'HEATHERBLUE': "Heather Blue", 'SAGE': "Sage", 'COBALT': "Cobalt", 'SUNLITICE': "Sunlit Ice",
                      "GREENYELLOW": "Green-Yellow", 'COPPER': 'Copper', 'BRONZE': 'Bronze', 'SILVER': 'Silver', 

                      'BERRYBANANA': "Berry Banana", 'HALLOWEEN': "Halloween", 'MIDNIGHT': "Midnight",
                      'WORMY': "Wormy", 'COTTONCANDY': "Cotton-Candy", 'BLUEHAZEL': "Blue Hazel", 'FALL': "Fall",
                      'SUNSETORANGE': "Sunset Orange", 'SUNSETPURPLE': "Sunset Purple", 'MOONSTONE': "Moonstone", 
                      'WALNUT': "Walnut", 'CHRISTMAS': "Christmas", 'BROWN': "Brown", 'SUNSETBLUE': "Sunset Blue", 'CEDAR': "Cedar", 
                      'LOBELIA': "Lobelia", 'OXIDIZED': "Oxidized", 'SNOW': "Snow", 'DARKPINE': "Dark Pine",
                      'FORESTFIRE': "Forest Fire", 'GOLDMOON': "Gold Moon", 'ROSE': "Rose", 'LIGHTFLAME': "Light Flame", 
                      'CLOUDY': "Cloudy", 'TURQUOISE': "Turquoise", 'TROPICALGREEN': "Tropical Green", 'SWAMP': "Swamp", 
                      'RAINY': "Rainy", 'SEAFOAM': "Seafoam", 'AQUAMARINE': "Aquamarine", 'EARTH': "Earth", 'RED': "Red", 
                      'PUMPKIN': "Pumpkin", 'LILAC': "Lilac", 'PERIWINKLE': "Periwinkle", 'TROPICALRED': "Tropical Red", 
                      'POND': "Pond", 'DIRT': "Dirt", 'VIOLET': "Violet", 'SUMMERYELLOW': "Summer Yellow", 'SUMMERORANGE': "Summer Orange", 
                      'AUTUMNHAZEL': "Autumn Hazel", 'GALAXY': "Galaxy", 'AUTUMNGREEN': "Autumn Green", 'WINTERBLUE': "Winter Blue", 
                      'WINTERVIOLET': "Winter Violet", 'DUSK': "Dusk", 'PEACOCK': "Peacock", 'NEBULA': "Nebula", 
                      'WINTERPURPLE': "Winter Purple", 'ECLIPSE': "Eclipse", 'SPRINGRED': "Spring Red", 'SPRINGROSE': "Spring Rose", 
                      'AURORA': "Aurora", 'AFTERGLOW': "Afterglow", 'AUTUMNBROWN': "Autumn Brown", 'LIGHTNING': "Lightning", 
                      'SPRINGPINK': "Spring Pink", 'SUMMERGOLD': "Summer Gold", 'HUMMINGBIRD': "Hummingbird", 'ETA': "Eta", 
                      'CARINA': "Carina", 'EAGLE': "Eagle", 'GHOSTHEAD': "Ghosthead", 'LAGOON': "Lagoon", 'MILKYWAY': "Milkyway", 
                      'SOUL': "Soul", 'SWAN': "Swan", 'TARANTULA': "Tarantula", 'VEIL': "Veil", 'SHROUD': "Shroud", 'CARITA': "Carita", 
                      'SEAFOAM': "Seafoam", 'LILAC': "Lilac", 'AZURE': "Azure", 'STORM': "Storm", 'RUSSET': "Russet", 'SAND': "Sand", 
                      'MIST': "Mist", 'AMETHYST': "Amethyst", 'TEMPEST': "Tempest", 'MIDNIGHT': "Midnight", 'HAZE': "Haze", 
                      'ECLIPSEDDAWN': "Eclipsed Dawn", 'GRIMAURA': "Grim Aura", 'LOVEMIX': "Love Mix", 'ASTRALSPELL': "Astral Spell", 
                      'SURPRISE': "Surprise", 'VIRIDIAN': "Viridian", 'ARTISTIQUE': "Artistique", 'SPECTRUMBREEZE': "Spectrum Breeze", 
                      'RADIANTCOMET': "Radiant Comet", 'COSMIAN': "Cosmian", 'CHERRYCHARM': "Cherry Charm", 'FIRECRACKER': "Firecracker", 
                      'ALLURA': "Allura", 'DAHLIA': "Dahlia", 'STARBELLE': "Starbelle", 'SILVERTONGUE': "Silver Tongue", 
                      'JEWELEDSANDS': "Jeweled Sands", 'MOONLIT': "Moonlit", 'MYTHICWIND': "Mythic Wind", 'ZINNIA': "Zinnia", 
                      'CRYSTALCORE': "Crystal Core", 'APPLESWEETS': "Apple Sweets", 'PEACHCOBBLER': "Peach Cobbler", 
                      'TITANIA': "Titania", 'CYPERUS': "Cyperus", 'LUNARGARDEN': "Lunar Garden", 'NECTAR': "Nectar", 
                      'CLOUDEDSUNRISE': "Clouded Sunrise", 'BLAZE': "Blaze", 'STARLITSPECTRUM': "Starlit Spectrum", 
                      'SHADOWCHARM': "Shadow Charm", 'SUNSETSPARKLE': "Sunset Sparkle", 'WILDACE': "Wild Ace", 'SCULPTEDMIND': "Sculpted Mind", 
                      'SUGARCOATING': "Sugar Coating", 'OCEANSUNRISE': "Ocean Sunrise", 'CLEARSKIES': "Clear Skies", 'DARKVISION': "Dark Vision", 
                      'VOLCANIC': "Volcanic", 'STELLARSOUL': "Stellar Soul", 'LIGHTYELLOW': "Light Yellow", 'LIGHTAMBER': "Light Amber", 
                      'LIGHTHAZEL': "Light Hazel", 'LIGHTPALEGREEN': "Bright Green", 'LIGHTGREEN': "Light Green", 'LIGHTBLUE': "Light Blue", 
                      'LIGHTDARKBLUE': "Bright Blue", 'LIGHTGREY': "Light Grey", 'LIGHTCYAN': "Light Cyan", 'LIGHTEMERALD': "Light Emerald", 
                      'LIGHTHEATHERBLUE': "Light Periwinkle", 'LIGHTSUNLITICE': "Bright Cyan", 'LIGHTCOPPER': "Light Copper", 'LIGHTSAGE': "Light Sage", 
                      'LIGHTCOBALT': "Light Cobalt", 'LIGHTPALEBLUE': "Sky Blue", 'LIGHTBRONZE': "Light Bronze", 'LIGHTSILVER': "Light Silver", 
                      'LIGHTPALEYELLOW': "Bright Yellow", 'LIGHTGOLD': "Light Gold", 'LIGHTGREENYELLOW': "Lime Green"})
eye_colors = sort_bidict(eye_colors)

tints = bidict({"none": "None", "pink": "Pink", "gray": "Gray", "red": "Red", "black": "Black", "orange": "Orange", "yellow": "Yellow", 
                "purple": "Purple", "blue": "Blue", "blush": "Blush", "willow": "Willow", "bluegray": "Blue-Gray", "lilac": "Lilac", 
                "sandy": "Sandy", "plum": "Plum", "midgray": "Mid-Gray", "flint": "Flint", "cadet": "Cadet", "sage": "Sage", 
                "coral": "Coral", "storm": "Storm", "maroon": "Maroon", "tan": "Tan", "bronze": "Bronze", "acacia": "Acacia", "rosy": "Rosy", 
                "redwood": "Redwood", "darkpurple": "Dark-Purple", "beige": "Beige", "cream": "Cream", "steel": "Steel", "cobalt": "Cobalt", 
                "ebony": "Ebony", "sooty": "Sooty"})
tints = sort_bidict(tints, 'none')

white_patches_tint = bidict({"none": "None", "darkcream": "Dark Cream", "cream": "Cream", "offwhite": "Offwhite",
                             "gray": "Gray", "pink": "Pink", "blue": "Blue", "orange": "Orange", "ebb": "Ebb", "almond": "Almond", 
                             "mocha": "Mocha", "honeydew": "Honeydew", "vanilla": "Vanilla", "malted": "Malted", "ashgray": "Ash Gray", 
                             "coffee": "Coffee", "cherry": "Cherry", "dawn": "Dawn", "powder": "Powder", "peach": "Peach", "violet": "Violet", 
                             "coyote": "Coyote", "obsidian": "Obsidian", "caramel": "Caramel", "golden": "Golden", "black": "Black", 
                             "dark": "Dark"})

skin_colors = bidict({'BLACK': "Black", 'RED': "Red", 'PINK': "Pink", 'DARKBROWN': "Dark Brown", 'BROWN': "Brown",
                      'LIGHTBROWN': "Light Brown", 'DARK': "Dark", 'DARKGREY': "Dark Gray", 'GREY': "Gray",
                      'DARKSALMON': "Dark Salmon", 'SALMON': 'Salmon', 'PEACH': 'Peach', 'DARKMARBLED': 'Dark Marbled',
                      'MARBLED': 'Marbled', 'LIGHTMARBLED': 'Light Marbled', 'DARKBLUE': 'Dark Blue', 'BLUE': 'Blue',
                      'LIGHTBLUE': 'Light Blue'})
skin_colors = sort_bidict(skin_colors)

colors = bidict({'WHITE': 'White', 'GREY': 'Grey', 'DARKGREY': 'Dark Grey', 'PALEGREY': 'Pale Grey',
                 'SILVER': 'Silver', 'GOLDEN': 'Golden', 'DARKGINGER': 'Dark Ginger', 'PALEGINGER': 'Pale Ginger',
                 'CREAM': 'Cream', 'BROWN': 'Brown', 'DARKBROWN': 'Dark Brown', 'LIGHTBROWN': 'Light Brown',
                 'BLACK': 'Black', "GHOST": "Ghost", "GINGER": "Ginger", "SIENNA": "Sienna", "LILAC": "Lilac",
                 "GOLDEN-BROWN": "Golden Brown", "CHOCOLATE": "Chocolate"})
colors = sort_bidict(colors)

white_patches = bidict({None: 'None', 'MAO': 'Mao', 'LUNA': 'Luna', 'CHESTSPECK': 'Chest Speck', 'WINGS': 'Wings',
                        'PAINTED': 'Painted', 'BLACKSTAR': 'Blackstar', 'LITTLE': 'Little', 'TUXEDO': 'Tuxedo',
                        'LIGHTTUXEDO': 'Light Tuxedo', 'BUZZARDFANG': 'Buzzardfang', 'TIP': 'Tip', 'BLAZE': 'Blaze',
                        'BIB': 'Bib', 'VEE': 'Vee', 'PAWS': 'Paws', 'BELLY': 'Belly', 'TAILTIP': 'Tail Tip',
                        'TOES': 'Toes', 'BROKENBLAZE': 'Broken Blaze', 'LILTWO': 'Lil Two', 'SCOURGE': 'Scourge',
                        'TOESTAIL': 'Toes Tail', 'RAVENPAW': 'Ravenpaw', 'HONEY': 'Honey', 'FANCY': 'Fancy',
                        'UNDERS': 'Unders', 'DAMIEN': 'Damien', 'SKUNK': 'Skunk', 'MITAINE': 'Mitaine',
                        'SQUEAKS': 'Squeaks', 'STAR': 'Star', 'ANY': 'Any', 'ANYTWO': 'Any Two', 'BROKEN': 'Broken',
                        'FRECKLES': 'Freckles', 'RINGTAIL': 'Ringtail', 'HALFFACE': 'Half Face', 'PANTSTWO': 'Pants 2',
                        'GOATEE': 'Goatee', 'PRINCE': 'Prince', 'FAROFA': 'Farofa', 'MISTER': 'Mister',
                        'PANTS': 'Pants', 'REVERSEPANTS': 'Reverse Pants', 'HALFWHITE': 'Half White',
                        'APPALOOSA': 'Appaloosa', 'PIEBALD': 'Piebald', 'CURVED': 'Curved', 'GLASS': 'Glass',
                        'MASKMANTLE': 'Mask Mantle', 'VAN': 'Van', 'ONEEAR': 'One Ear', 'LIGHTSONG': 'Lightsong',
                        'TAIL': 'Tail', 'HEART': 'Heart', 'HEARTTWO': 'Heart 2', 'MOORISH': 'Moorish', 'APRON': 'Apron',
                        'CAPSADDLE': 'Cap Saddle', 'FULLWHITE': 'Full White', "EXTRA": "Extra", 'PETAL': 'Petal',
                        "DIVA": "Diva", "SAVANNAH": "Savannah", "FADESPOTS": "Fadespots", "SHIBAINU": "Shiba Inu", 
                        "TOPCOVER": "Top Cover", "DAPPLEPAW": "Dapplepaw", "BEARD": "Beard", "PEBBLESHINE": "Pebbleshine", 
                        "OWL": "Owl", "WOODPECKER": "Woodpecker", "MISS": "Miss", "BOOTS": "Boots", "COW": "Cow", 
                        "COWTWO": "Cow 2", "BUB": "Bub", "BOWTIE": "Bowtie", "MUSTACHE" : "Mustache", "REVERSEHEART": "Reverse Heart", 
                        "SPARROW": "Sparrow", "VEST": "Vest", "LOVEBUG" : "Lovebug", "TRIXIE": "Trixie", "SPARKLE": "Sparkle", 
                        "RIGHTEAR" : "Right Ear", "LEFTEAR": "Left Ear", "ESTRELLA": "Estrella", "REVERSEEYE" : "Reverse Eye", 
                        "BACKSPOT": "Back spot", "EYEBAGS": "Eye Bags", "FADEBELLY": "Fade Belly", "SAMMY": "Sammy", "FRONT" : "Front", 
                        "BLOSSOMSTEP": "Blossomstep", "BULLSEYE": "Bullseye", "SHOOTINGSTAR" : "Shooting Star", "EYESPOT" : "Eye Spot", 
                        "PEBBLE": "Pebble", "TAILTWO": "Tail Two", "BUDDY": "Buddy", "FCONE": "FC One", "FCTWO": "FC Two", 
                        "MIA": "Mia", "DIGIT": "Digit", "SCAR": "Scar", "BUSTER": "Buster", "FINN": "Finn", "KROPKA": "Kropka", 
                        "HAWKBLAZE": "Hawkblaze", "LOCKET": "Locket", "PRINCESS": "Princess", "ROSINA" : "Rosina", "CAKE" : "Cake", 
                        'MINKMINIMALONE': 'Minkminimalone', 'MINKMINIMALTWO': 'Minkminimaltwo', 'MINKMINIMALTHREE': 'Minkminimalthree', 
                        'MINKMINIMALFOUR': 'Minkminimalfour', 'MINKMASK': 'Minkmask', 'MINKCHEST': 'Minkchest', 'MINKSIDEMASK': 'Minksidemask', 
                        'MINKEMBER': 'Minkember', 'MINKORIOLE': 'Minkoriole', 'MINKONE': 'Minkone', 'MINKDAPPLENIGHT': 'Minkdapplenight', 
                        'MINKSAFI': 'Minksafi', 'MINKROSETAIL': 'Minkrosetail', 'MINKTWO': 'Minktwo', 'MINKFOUR': 'Minkfour', 
                        'MINKREDTAIL': 'Minkredtail', 'MINKSTREAK': 'Minkstreak', 'MINKARMTAIL': 'Minkarmtail', 'MINKSTREAMSTRIKE': 'Minkstreamstrike', 
                        'MINKDAUB': 'Minkdaub', 'MINKBRIE': 'Minkbrie', 'MINKROBIN': 'Minkrobin', 'MINKBLANKET': 'Minkblanket', 
                        'MINKBELOVED': 'Minkbeloved', 'MINKHEARTBEAT': 'Minkheartbeat', 'MINKCHIMERA': 'Minkchimera', 'MINKEYEDOT': 'Minkeyedot', 
                        'MINKSHILOH': 'Minkshiloh', 'MINKTHREE': 'Minkthree', 'MINKOREO': 'Minkoreo', 'MINKGRUMPYFACE' : 'Minkgrumpyface', 
                        'MINKPACMAN': 'Minkpacman', 'MINKPAIGE': 'Minkpaige', 'MINKMOTTLED': 'Minkmottled', 'MINKDELILAH': 'Minkdelilah', 
                        'MINKHALF': 'Minkhalf', 'MINKBANDANA': 'Minkbandana', 'MINKSWOOP': 'Minkswoop'})
white_patches = sort_bidict(white_patches, None)

points = bidict({None: 'None', 'COLOURPOINT': 'Colorpoint', 'RAGDOLL': 'Ragdoll', 'SEPIAPOINT': 'Sepiapoint', 'MINKPOINT': 'Minkpoint',
                 'SEALPOINT': 'Sealpoint', 'MINKSMOKE': 'Minksmoke', 'MINKBODY': 'Minkbody'})
points = sort_bidict(points, None)

vit = bidict({None: 'None', 'VITILIGO': 'Vitiligo 1', 'VITILIGOTWO': 'Vitiligo 2', 'KARPATI': 'Karpati',
              'MOON': 'Moon', 'PHANTOM': 'Phantom', 'POWDER': 'Powder', 'BLEACHED': 'Bleached', "SMOKEY": "Smokey",
              'MINKBRINDLE': 'Minkbrindle', 'MINKFRECKLED': 'Minkfreckled', 'MINKSMUDGED': 'Minksmudged'})
vit = sort_bidict(vit, None)

scars = bidict({None: "None", "ONE": "Chest", "TWO": "Shoulder", "THREE": "Over Eye", "TAILSCAR": "Tail",
                "SNOUT": "Snout", "CHEEK": "Cheek",
                "SIDE": "Side", "THROAT": "Throat", "TAILBASE": "Tail Base", "BELLY": "Belly", "LEGBITE": "Bite: Leg",
                "NECKBITE": "Bite: Neck", "FACE": "Face", "MANLEG": "Mangled Leg", "BRIGHTHEART": "Mangled Face",
                "MANTAIL": "Mangled Tail", "BRIDGE": "Bridge", "RIGHTBLIND": "Right Eye Blind",
                "LEFTBLIND": "Left Eye Blind", "BOTHBLIND": "Both Eyes Blind", "BEAKCHEEK": "Beak: Cheek",
                "BEAKLOWER": "Beak: Lower", "CATBITE": "Cat Bite", "RATBITE": "Rat Bite", "QUILLCHUNK": "Quill Chunk",
                "QUILLSCRATCH": "Quill Scratch", "LEFTEAR": "Left Ear Notch", "RIGHTEAR": "Right Ear Notch",
                "NOLEFTEAR": "No Left Ear", "NORIGHTEAR": "No Right Ear", "NOEAR": "No Ears", "NOTAIL": "No Tail",
                "HALFTAIL": "Half Tail", "NOPAW": "Missing Leg",
                "SNAKE": "Bite: Snake", "TOETRAP": "Toe Trap", "BURNPAWS": "Burnt Paws", "BURNTAIL": "Burnt Tail",
                "BURNBELLY": "Burnt Belly", "BURNRUMP": "Burnt Rump", "FROSTFACE": "Frostbitten Face",
                "FROSTTAIL": "Frostbitten Tail", "FROSTMITT": "Frostbitten Paw1", "FROSTSOCK": "Frostbitten Paw2"})
scars = sort_bidict(scars, None)

accessories = bidict({None: "None", "MAPLE LEAF": "Maple Leaf", "HOLLY": "Holly", "BLUE BERRIES": "Blue Berries",
                      "FORGET ME NOTS": "Forget-me-nots", "RYE STALK": "Rye Stalk", "LAUREL": "Laurel",
                      "BLUEBELLS": "Bluebells", "NETTLE": "Nettle", "POPPY": "Poppy", "LAVENDER": "Lavender",
                      "HERBS": "Herbs", "PETALS": "Petals", "DRY HERBS": "Dry Herbs", "OAK LEAVES": "Oak Leaves",
                      "CATMINT": "Catmint", "MAPLE SEED": "Maple Seed", "JUNIPER": "Juniper",
                      "RED FEATHERS": "Red Feathers", "BLUE FEATHERS": "Blue Feathers", "JAY FEATHERS": "Jay Feathers",
                      "MOTH WINGS": "Moth Wings", "CICADA WINGS": "Cicada Wings", "CRIMSON": "Crimson Collar",
                      "BLUE": "Blue Collar", "YELLOW": "Yellow Collar", "CYAN": "Cyan Collar", "RED": "Red Collar",
                      "LIME": "Lime Collar", "GREEN": "Green Collar", "RAINBOW": "Rainbow Collar",
                      "BLACK": "Black Collar", "SPIKES": "Spiked Collar", "PINK": "Pink Collar",
                      "PURPLE": "Purple Collar", "MULTI": "Mulicolored Collar", "CRIMSONBELL": "Crimson Bell Collar",
                      "BLUEBELL": "Blue Bell Collar", "YELLOWBELL": "Yellow Bell Collar",
                      "CYANBELL": "Cyan Bell Collar", "REDBELL": "Red Bell Collar", "LIMEBELL": "Lime Bell Collar",
                      "GREENBELL": "Green Bell Collar", "RAINBOWBELL": "Rainbow Bell Color",
                      "BLACKBELL": "Black Bell Collar", "SPIKESBELL": "Spiked Bell Collar",
                      "PINKBELL": "Pine Bell Collar", "PURPLEBELL": "Purple Bell Collar",
                      "MULTIBELL": "Mulitcolored Bell Color", "CRIMSONBOW": "Crimson Bow", "BLUEBOW": "Blue Bow",
                      "YELLOWBOW": "Yellow Bow", "CYANBOW": "Cyan Bow", "REDBOW": "Red Bow", "LIMEBOW": "Lime Bow",
                      "GREENBOW": "Green Bow", "RAINBOWBOW": "Rainbow Bow", "BLACKBOW": "Black Bow",
                      "SPIKESBOW": "Spiked Bow", "PINKBOW": "Pink Bow", "PURPLEBOW": "Purple Bow",
                      "MULTIBOW": "Multicolored Bow", "WHITEBOW": "White Bow", "INDIGOBOW": "Indigo Bow",
                      "INDIGO": "Indigo Collar", "WHITE": "White Collar", "WHITEBELL": "White Bell Collar",
                      "INDIGOBELL": "Indigo Bell Collar", "CRIMSONNYLON": "Crimson Nylon Collar",
                      "BLUENYLON": "Blue Nylon Collar", "YELLOWNYLON": "Yellow Nylon Collar",
                      "CYANNYLON": "Cyan Nylon Collar", "REDNYLON": "Red Nylon Collar",
                      "LIMENYLON": "Line Nylon Collar", "GREENNYLON": "Green Nylon Collar",
                      "RAINBOWNYLON": "Rainbow Nylon Collar", "BLACKNYLON": "Black Nylon Collar",
                      "SPIKESNYLON": "Spiked Nylon Collar", "WHITENYLON": "White Nylon Collar",
                      "PINKNYLON": "Pink Nylon Collar", "PURPLENYLON": "Purple Nylon Collar",
                      "MULTINYLON": "Mulicolored Nylon Collar", "INDIGONYLON": "Indigo Nylon Collar", 
                      "LILYPAD": "Lilypad", "LARGE DEATHBERRY": "Large Deathberry", 
                      "SMALL DEATHBERRY": "Small Deathberry", "ACORN2": "Acorn2", "PINECONE": "Pinecone", 
                      "VINE": "Vine", "CHERRY2": "Cherry2", "BLEEDING HEARTS": "Bleeding Hearts", "SHELL PACK": "Shell Pack",
                      "FERNS": "Ferns", "GOLD FERNS": "Gold Ferns", "AUTUMN FERNS": "Autumn Ferns", "WHEAT": "Wheat", 
                      "BLACK WHEAT": "Black Wheat", "BERRIES": "Berries", "CLOVERS": "Clovers", "CLOVER": "Clover", 
                      "MOSS": "Moss", "FLOWER MOSS": "Flower Moss", "RED MUSHROOM": "Red Mushroom", "LARGE LUNA": "Large Luna", 
                      "LARGE COMET": "Large Comet", "SMALL LUNA": "Small Luna", "MORPHO BUTTERFLY": "Morpho Butterfly", 
                      "MUD PAWS": "Mud Paws", "ORANGEBUTTERFLY": "Orange Butterfly", "BLUEBUTTERFLY": "Blue Butterfly", 
                      "BROWNPELT": "Brownpelt", "GRAYPELT": "Graypelt", "BROWNMOSSPELT": "Brownmosspelt", 
                      "GRAYMOSSPELT": "Graymosspelt", "FERN": "Fern", "MOREFERN": "More fern", "BLEEDINGHEART": "Bleedingheart", 
                      "LILY": "Lily", "YELLOWCROWN": "Yellow crown", "REDCROWN": "Red crown", "LILYPADCROWN": "Lilypad crown", 
                      "WOODDRAGON": "Wood dragon", "CHERRYBLOSSOM": "Cherry Blossom", "TULIPPETALS": "Tulip Petals", 
                      "CLOVERFLOWER": "Clover Flower", "PANSIES": "Pansies", "BELLFLOWERS": "Bellflowers", 
                      "SANVITALIAFLOWERS": "Sanvitalia Flowers", "EGGSHELLS": "Eggshells", "BLUEEGGSHELLS": "Blue Eggshells", 
                      "EASTEREGG": "Easter Egg", "FORSYTHIA": "Forsythia", "MINTLEAF": "Mint Leaf", "STICKS": "Sticks", 
                      "SPRINGFEATHERS": "Spring Feathers", "SNAILSHELL": "Snail Shell", "MUD": "Mud", 
                      "CHERRYPLUMLEAVES": "Cherry Plum Leaves", "CATKIN": "Catkin", "HONEYCOMB": "Honeycomb", 
                      "FLOWERCROWN": "Flowercrown", "LILIESOFTHEVALLEY": "Lilies of the Valley", "STRAWMANE": "Straw Mane", 
                      "MISTLETOE": "Mistletoe", "REDPOINSETTIA": "Red Poinsettia", "WHITEPOINSETTIA": "White Poinsettia", 
                      "COTONEASTERWREATH": "Cotoneaster Wreath", "YEWS": "Yews", "HEATHER": "Heather", "TEETHCOLLAR": "Teeth Collar", 
                      "DRIEDORANGE": "Dried Orange", "ROESKULL": "Roeskull", "WOODENOAKANTLERS": "Wooden oak antlers", 
                      "WOODENBIRCHANTLERS": "Wooden birch antlers", "DOGWOOD": "Dogwood", "GRAYWOOL": "Graywool", "BLACKWOOL": "Blackwool", 
                      "CREAMWOOL": "Creamwool", "WHITEWOOL": "Whitewool", "FIRBRANCHES": "Fir branches", "CORALBELLS": "Coral bells", 
                      "SILVERDUSTPLANT": "Silverdust plant", "REDHARNESS": "Red harness", "NAVYHARNESS": "Navy harness", 
                      "YELLOWHARNESS": "Yellow harness", "TEALHARNESS": "Teal harness", "ORANGEHARNESS": "Orange harness", 
                      "GREENHARNESS": "Green harness", "MOSSHARNESS": "Moss harness", "RAINBOWHARNESS": "Rainbow harness", 
                      "BLACKHARNESS": "Black harness", "BEEHARNESS": "Bee harness", "CREAMHARNESS": "Cream harness", 
                      "PINKHARNESS": "Pink harness", "MAGENTAHARNESS": "Magenta harness", "PEACHHARNESS": "Peach harness", 
                      "VIOLETHARNESS": "Violet harness", "DAISY": "Daisy", "DIANTHUS": "Dianthus", "BLEEDING HEARTS": "Bleeding hearts", 
                      "FRANGIPANI": "Frangipani", "BLUE GLORY": "Blue glory", "CATNIP FLOWER": "Catnip flower", 
                      "BLANKET FLOWER": "Blanket flower", "ALLIUM": "Allium", "LACELEAF": "Laceleaf", "PURPLE GLORY": "Purple glory", 
                      "YELLOW PRIMROSE": "Yellow primrose", "HESPERIS": "Hesperis", "MARIGOLD": "Marigold", "WISTERIA": "Wisteria", 
                      "PINKFLOWERCROWN": "Pink flowercrown", "YELLOWFLOWERCROWN": "Yellow flowercrown", "BLUEFLOWERCROWN": "Blue flowercrown", 
                      "PURPLEFLOWERCROWN": "Purple flowercrown", "CLOVER": "Clover", "STICK": "Stick", "PUMPKIN": "Pumpkin", 
                      "MOSS": "Moss", "IVY": "Ivy", "ACORN": "Acorn", "MOSS PELT": "Moss pelt", "REEDS": "Reeds", "BAMBOO": "Bamboo", 
                      "GRASS SNAKE": "Grass snake", "BLUE RACER": "Blue racer", "WESTERN COACHWHIP": "Western coachwhip", 
                      "KINGSNAKE": "Kingsnake", "GRAY SQUIRREL": "Gray squirrel", "RED SQUIRREL": "Red squirrel", "CRAB": "Crab", 
                      "WHITE RABBIT": "White rabbit", "BLACK RABBIT": "Black rabbit", "BROWN RABBIT": "Brown rabbit", 
                      "INDIAN GIANT SQUIRREL": "Indian giant squirrel", "FAWN RABBIT": "Fawn rabbit", 
                      "BROWN AND WHITE RABBIT": "Brown and white rabbit", "BLACK AND WHITE RABBIT": "Black and white rabbit", 
                      "WHITE AND FAWN RABBIT": "White and fawn rabbit", "BLACK VITILIGO RABBIT": "Black vitiligo rabbit", 
                      "BROWN VITILIGO RABBIT": "Brown vitiligo rabbit", "FAWN VITILIGO RABBIT": "Fawn vitiligo rabbit", 
                      "BLACKBIRD": "Blackbird", "ROBIN": "Robin", "JAY": "Jay", "THRUSH": "Thrush", "CARDINAL": "Cardinal", 
                      "MAGPIE": "Magpie", "CUBAN TROGON": "Cuban trogon", "TAN RABBIT": "Tan rabbit", 
                      "TAN AND WHITE RABBIT": "Tan and white rabbit", "TAN VITILIGO RABBIT": "Tan vitiligo rabbit", "RAT": "Rat", 
                      "WHITE MOUSE": "White mouse", "BLACK MOUSE": "Black mouse", "GRAY MOUSE": "Gray mouse", "BROWN MOUSE": "Brown mouse", 
                      "GRAY RABBIT": "Gray rabbit", "GRAY AND WHITE RABBIT": "Gray and white rabbit", 
                      "GRAY VITILIGO RABBIT": "Gray vitiligo rabbit", "LUNAR MOTH": "Lunar moth", "ROSY MAPLE MOTH": "Rosy maple moth", 
                      "MONARCH BUTTERFLY": "Monarch butterfly", "DAPPLED MONARCH": "Dappled monarch", "POLYPHEMUS MOTH": "Polyphemus moth", 
                      "MINT MOTH": "Mint moth", "BROWN SNAIL": "Brown snail", "RED SNAIL": "Red snail", "WORM": "Worm", 
                      "BLUE SNAIL": "Blue snail", "ZEBRA ISOPOD": "Zebra isopod", "DUCKY ISOPOD": "Ducky isopod", 
                      "DAIRY COW ISOPOD": "Dairy cow isopod", "BEETLEJUICE ISOPOD": "Beetlejuice isopod", "BEE": "Bee", 
                      "RED LADYBUG": "Red ladybug", "ORANGE LADYBUG": "Orange ladybug", "YELLOW LADYBUG": "Yellow ladybug", 
                      "RASPBERRY": "Raspberry", "BLACKBERRY": "Blackberry", "GOLDEN RASPBERRY": "Golden raspberry", 
                      "CHERRY": "Cherry", "YEW": "Yew", "WILLOWBARK BAG": "Willowbark bag", "CLAY DAISY POT": "Clay Daisy Pot", 
                      "CLAY AMANITA POT": "Clay Amanita Pot", "CLAY BROWNCAP POT": "Clay Browncap Pot", "BIRD SKULL": "Bird Skull", 
                      "LEAF BOW": "Leaf Bow", "RAINCOAT": "Raincoat", "POPTABS": "Poptabs", "FAZBEAR": "Fazbear", 
                      "WHITEBEAR": "White Bear", "PANDA": "Panda", "BEAR": "Bear", "BROWNBEAR": "Brown Bear", "TIDE": "Tide", 
                      "CELESTIALCHIMES": "Celestial Chimes", "LUNARCHIMES": "Lunar Chimes", "STARCHIMES": "Star Chimes", 
                      "SILVERLUNARCHIMES": "Silver Lunar Chimes", "FIDDLEHEADS": "Fiddleheads", "LANTERNS": "Lanterns", 
                      "HEARTCHARMS": "Heartcharms", "CHIMES": "Chimes", "SEAWEED": "Seaweed", "DAISY CORSAGE": "Daisy Corsage"})
accessories = sort_bidict(accessories, None)

platforms = {"None": None,
             "Greenleaf Plains - Day": "resources/images/platforms/plains/greenleaf_light.png",
             "Leaf-fall Plains - Day": "resources/images/platforms/plains/leaffall_light.png",
             "Leaf-bare Plains - Day": "resources/images/platforms/plains/leafbare_light.png",
             "Newleaf Plains - Day": "resources/images/platforms/plains/newleaf_light.png",
             "Greenleaf Plains - Night": "resources/images/platforms/plains/greenleaf_dark.png",
             "Leaf-fall Plains - Night": "resources/images/platforms/plains/leaffall_dark.png",
             "Leaf-bare Plains - Night": "resources/images/platforms/plains/leafbare_dark.png",
             "Newleaf Plains - Night": "resources/images/platforms/plains/newleaf_dark.png",
             "Greenleaf Forest - Day": "resources/images/platforms/forest/greenleaf_light.png",
             "Leaf-fall Forest - Day": "resources/images/platforms/forest/leaffall_light.png",
             "Leaf-bare Forest - Day": "resources/images/platforms/forest/leafbare_light.png",
             "Newleaf Forest - Day": "resources/images/platforms/forest/newleaf_light.png",
             "Greenleaf Forest - Night": "resources/images/platforms/forest/greenleaf_dark.png",
             "Leaf-fall Forest - Night": "resources/images/platforms/forest/leaffall_dark.png",
             "Leaf-bare Forest - Night": "resources/images/platforms/forest/leafbare_dark.png",
             "Newleaf Forest - Night": "resources/images/platforms/forest/newleaf_dark.png",
             "Greenleaf Mountains - Day": "resources/images/platforms/mountainous/greenleaf_light.png",
             "Leaf-fall Mountains - Day": "resources/images/platforms/mountainous/leaffall_light.png",
             "Leaf-bare Mountains - Day": "resources/images/platforms/mountainous/leafbare_light.png",
             "Newleaf Mountains - Day": "resources/images/platforms/mountainous/newleaf_light.png",
             "Greenleaf Mountains - Night": "resources/images/platforms/mountainous/greenleaf_dark.png",
             "Leaf-fall Mountains - Night": "resources/images/platforms/mountainous/leaffall_dark.png",
             "Leaf-bare Mountains - Night": "resources/images/platforms/mountainous/leafbare_dark.png",
             "Newleaf Mountains - Night": "resources/images/platforms/mountainous/newleaf_dark.png",
             "Greenleaf Beach - Day": "resources/images/platforms/beach/greenleaf_light.png",
             "Leaf-fall Beach - Day": "resources/images/platforms/beach/leaffall_light.png",
             "Leaf-bare Beach - Day": "resources/images/platforms/beach/leafbare_light.png",
             "Newleaf Beach - Day": "resources/images/platforms/beach/newleaf_light.png",
             "Greenleaf Beach - Night": "resources/images/platforms/beach/greenleaf_dark.png",
             "Leaf-fall Beach - Night": "resources/images/platforms/beach/leaffall_dark.png",
             "Leaf-bare Beach - Night": "resources/images/platforms/beach/leafbare_dark.png",
             "Newleaf Beach - Night": "resources/images/platforms/beach/newleaf_dark.png",
             "Dark Forest - Light": "resources/images/platforms/darkforestplatform_light.png",
             "Dark Forest - Dark": "resources/images/platforms/darkforestplatform_dark.png",
             "StarClan": "resources/images/platforms/starclanplatform_dark.png"}

lineart = ["Normal", "StarClan", "Dark Forest"]

poses = {
    "short": {
        "newborn": {
            "1": 20,
            "2": 20,
            "3": 20
        },
        "kitten": {
            "1": 0,
            "2": 1,
            "3": 2
        },
        "adolescent": {
            "1": 3,
            "2": 4,
            "3": 5
        },
        "adult": {
            "1": 6,
            "2": 7,
            "3": 8
        },
        "senior": {
            "1": 12,
            "2": 13,
            "3": 14
        }
    },
    "long": {
        "newborn": {
            "1": 20,
            "2": 20,
            "3": 20
        },
        "kitten": {
            "1": 0,
            "2": 1,
            "3": 2
        },
        "adolescent": {
            "1": 3,
            "2": 4,
            "3": 5
        },
        "adult": {
            "1": 9,
            "2": 10,
            "3": 11
        },
        "senior": {
            "1": 12,
            "2": 13,
            "3": 14
        }
    }
}
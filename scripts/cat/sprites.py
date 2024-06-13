import pygame

import ujson

from scripts.game_structure.game_essentials import game

class Sprites():
    cat_tints = {}
    white_patches_tints = {}

    def __init__(self, size=None):
        """Class that handles and hold all spritesheets. 
        Size is normall automatically determined by the size
        of the lineart. If a size is passed, it will override 
        this value. """
        self.size = None
        self.spritesheets = {}
        self.images = {}
        self.sprites = {}

        # Shared empty sprite for placeholders
        self.blank_sprite = None
        
        self.load_tints()

    def load_tints(self):
        try:
            with open("sprites/dicts/tint.json", 'r') as read_file:
                Sprites.cat_tints = ujson.loads(read_file.read())
        except:
            print("ERROR: Reading Tints")

        try:
            with open("sprites/dicts/white_patches_tint.json", 'r') as read_file:
                Sprites.white_patches_tints = ujson.loads(read_file.read())
        except:
            print("ERROR: Reading White Patches Tints")
            
    def spritesheet(self, a_file, name):
        """
        Add spritesheet called name from a_file.

        Parameters:
        a_file -- Path to the file to create a spritesheet from.
        name -- Name to call the new spritesheet.
        """
        self.spritesheets[name] = pygame.image.load(a_file).convert_alpha()

    def make_group(self,
                   spritesheet,
                   pos,
                   name,
                   sprites_x=3,
                   sprites_y=7):  # pos = ex. (2, 3), no single pixels
        """
        Divide sprites on a sprite-sheet into groups of sprites that are easily accessible.

        Parameters:
        spritesheet -- Name of spritesheet.
        pos -- (x,y) tuple of offsets. NOT pixel offset, but offset of other sprites.
        name -- Name of group to make.
        
        Keyword Arguments
        sprites_x -- Number of sprites horizontally (default: 3)
        sprites_y -- Number of sprites vertically (default: 3)
        """

        group_x_ofs = pos[0] * sprites_x * self.size
        group_y_ofs = pos[1] * sprites_y * self.size
        i = 0

        # splitting group into singular sprites and storing into self.sprites section
        for y in range(sprites_y):
            for x in range(sprites_x):
                try:
                    new_sprite = pygame.Surface.subsurface(
                        self.spritesheets[spritesheet],
                        group_x_ofs + x * self.size,
                        group_y_ofs + y * self.size,
                        self.size, self.size
                    )
                except ValueError:
                    # Fallback for non-existent sprites
                    if not self.blank_sprite:
                        self.blank_sprite = pygame.Surface(
                            (self.size, self.size),
                            pygame.HWSURFACE | pygame.SRCALPHA
                        )
                    new_sprite = self.blank_sprite
                self.sprites[f'{name}{i}'] = new_sprite
                i += 1

    def load_all(self):
        # get the width and height of the spritesheet
        lineart = pygame.image.load('sprites/lineart.png')
        width, height = lineart.get_size()
        del lineart # unneeded

        # if anyone changes lineart for whatever reason update this
        if isinstance(self.size, int):
            pass
        elif width / 3 == height / 7:
            self.size = width / 3
        else:
            self.size = 50 # default, what base clangen uses
            print(f"lineart.png is not 3x7, falling back to {self.size}")
            print(f"if you are a modder, please update scripts/cat/sprites.py and do a search for 'if width / 3 == height / 7:'")

        del width, height # unneeded

        for x in [
            'lineart', 'lineartdf', 'lineartdead',
            'eyes', 'eyes2', 'skin',
            'scars', 'missingscars',
            'medcatherbs',
            'collars', 'bellcollars', 'bowcollars', 'nyloncollars',
            'singlecolours', 'speckledcolours', 'tabbycolours', 'bengalcolours', 'marbledcolours',
            'rosettecolours', 'smokecolours', 'tickedcolours', 'mackerelcolours', 'classiccolours',
            'sokokecolours', 'agouticolours', 'singlestripecolours', 'maskedcolours',
            'shadersnewwhite', 'lightingnew',
            'whitepatches', 'tortiepatchesmasks',
            'fademask', 'fadestarclan', 'fadedarkforest',
            'symbols',

            # Colors of Nature
            'dottedcolours', 'stripedcolours', 'wildcatcolours',

            # Mycena's Many Markings

            'ocelotcolours', 'lynxcolours', 'cheetahcolours',

            'bobtailcolours', 'manedwolfcolours',

            # Mink's White Patches/Torties
            'minkstorties', 'minkswhite',
            
            # Beetle's Eyes

            'eyeswood', 'eyeswood2', 'moreeyes', 'moreeyes2', 'recoloredeyes', 'recoloredeyestwo',

            # Myst's Eyes

            'brightmistyeyes', 'brightmistyeyestwo', 'dullmistyeyes', 'dullmistyeyestwo', 'glowmistyeyes', 
            'glowmistyeyestwo', 'supermistyeyes', 'supermistyeyestwo', 

            # Odhan's

            'flower_accessories', 'plant2_accessories', 'snake_accessories', 'smallAnimal_accessories', 'deadInsect_accessories',
            'aliveInsect_accessories', 'fruit_accessories', 'crafted_accessories', 'tail2_accessories',

            #WILDS
            'wildacc', 'wildacc2', 'wildacc3',

            #SUPERARTSI
            'superartsi',

            #coffee
            'coffee',

            'eragona',

            "crowns",

            "wooddragon",

            "springwinter",

            "raincoat",

            "poptabs",

            "fazbear",

            "bears",

            "tide",

            "chimes",

            "moipa"

        ]:
            self.spritesheet(f"sprites/{x}.png", x)

        # Line art
        self.make_group('lineart', (0, 0), 'lines')
        self.make_group('shadersnewwhite', (0, 0), 'shaders')
        self.make_group('lightingnew', (0, 0), 'lighting')

        self.make_group('lineartdead', (0, 0), 'lineartdead')
        self.make_group('lineartdf', (0, 0), 'lineartdf')

        # Fading Fog
        for i in range(0, 3):
            self.make_group('fademask', (i, 0), f'fademask{i}')
            self.make_group('fadestarclan', (i, 0), f'fadestarclan{i}')
            self.make_group('fadedarkforest', (i, 0), f'fadedf{i}')

        # Define eye colors
        eye_colors = [
            ['YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE', 'GREY', 'CYAN', 'EMERALD',
             'HEATHERBLUE', 'SUNLITICE'],
            ['COPPER', 'SAGE', 'COBALT', 'PALEBLUE', 'BRONZE', 'SILVER', 'PALEYELLOW', 'GOLD', 'GREENYELLOW']
        ]
        
        # TESTING AREA !!!

        # Beetle's Eyes
        eyeswood = [
            ['BROWN', 'CEDAR', 'CHRISTMAS', 'COTTONCANDY', 'DARKPINE', 'FALL',
            'FORESTFIRE', 'GOLDMOON', 'HALLOWEEN', 'LOBELIA', 'MIDNIGHT', 'MOONSTONE'],
            ['OXIDIZED', 'SNOW', 'BERRYBANANA', 'SUNSETBLUE', 'SUNSETORANGE', 'SUNSETPURPLE',
            'WALNUT', 'WORMY', 'BLUEHAZEL']
        ]

        moreeyes = [
            ['ROSE', 'TROPICALGREEN', 'SEAFOAM', 'LIGHTFLAME', 'CLOUDY', 'RED', 
            'TROPICALRED', 'TURQUOISE', 'SWAMP', 'RAINY', 'AQUAMARINE', 'EARTH'],
            ['PUMPKIN', 'LILAC', 'PERIWINKLE', 'VIOLET', 'POND', 'DIRT']
        ]
        
        recoloredeyes = [
            ['LIGHTYELLOW', 'LIGHTAMBER', 'LIGHTHAZEL', 'LIGHTPALEGREEN', 'LIGHTGREEN', 'LIGHTBLUE', 
            'LIGHTDARKBLUE', 'LIGHTGREY', 'LIGHTCYAN', 'LIGHTEMERALD', 'LIGHTHEATHERBLUE', 'LIGHTSUNLITICE'],
            ['LIGHTCOPPER', 'LIGHTSAGE', 'LIGHTCOBALT', 'LIGHTPALEBLUE', 'LIGHTBRONZE', 'LIGHTSILVER',
            'LIGHTPALEYELLOW', 'LIGHTGOLD', 'LIGHTGREENYELLOW']
        ]

        # Myst's Eyes

        brightmistyeyes = [
            ['SUMMERYELLOW', 'SUMMERORANGE', 'AUTUMNHAZEL', 'GALAXY', 'AUTUMNGREEN', 'WINTERBLUE', 'WINTERVIOLET', 'DUSK', 
            'PEACOCK', 'NEBULA', 'WINTERPURPLE', 'ECLIPSE'],
            ['SPRINGRED', 'SPRINGROSE', 'AURORA', 'AFTERGLOW', 'AUTUMNBROWN', 'LIGHTNING', 'SPRINGPINK', 'SUMMERGOLD', 'HUMMINGBIRD']
        ]

        dullmistyeyes = [
            ['ETA', 'CARINA', 'EAGLE', 'GHOSTHEAD', 'LAGOON', 'MILKYWAY', 'SOUL', 'SWAN', 'TARANTULA', 'VEIL', 'SHROUD', 'CARITA'],
            ['SEAFOAM', 'LILAC', 'AZURE', 'STORM', 'RUSSET', 'SAND', 'MIST', 'AMETHYST', 'TEMPEST']
        ]

        glowmistyeyes = [
            ['MIDNIGHT', 'HAZE', 'ECLIPSEDDAWN', 'GRIMAURA', 'LOVEMIX', 'ASTRALSPELL', 'SURPRISE', 'VIRIDIAN', 'ARTISTIQUE', 
             'SPECTRUMBREEZE', 'RADIANTCOMET', 'COSMIAN'],
            ['CHERRYCHARM', 'FIRECRACKER', 'ALLURA', 'DAHLIA', 'STARBELLE', 'SILVERTONGUE', 'JEWELEDSANDS', 'MOONLIT', 'MYTHICWIND']
        ]

        supermistyeyes = [
            ['ZINNIA', 'CRYSTALCORE', 'APPLESWEETS', 'PEACHCOBBLER', 'TITANIA', 'CYPERUS', 'LUNARGARDEN', 'NECTAR', 
             'CLOUDEDSUNRISE', 'BLAZE', 'STARLITSPECTRUM', 'SHADOWCHARM'],
             ['SUNSETSPARKLE', 'WILDACE', 'SCULPTEDMIND', 'SUGARCOATING', 'OCEANSUNRISE', 'CLEARSKIES', 'DARKVISION', 'VOLCANIC', 'STELLARSOUL']
        ]

        # Def eyes

        for row, colors in enumerate(eye_colors):
            for col, color in enumerate(colors):
                self.make_group('eyes', (col, row), f'eyes{color}')
                self.make_group('eyes2', (col, row), f'eyes2{color}')

        for row, colors in enumerate(eyeswood):
            for col, color in enumerate(colors):
                self.make_group('eyeswood', (col, row), f'eyes{color}')
                self.make_group('eyeswood2', (col, row), f'eyes2{color}')

        for row, colors in enumerate(moreeyes):
            for col, color in enumerate(colors):
                self.make_group('moreeyes', (col, row), f'eyes{color}')
                self.make_group('moreeyes2', (col, row), f'eyes2{color}')
        
        for row, colors in enumerate(recoloredeyes):
            for col, color in enumerate(colors):
                self.make_group('recoloredeyes', (col, row), f'eyes{color}')
                self.make_group('recoloredeyestwo', (col, row), f'eyes2{color}')

        for row, colors in enumerate(brightmistyeyes):
            for col, color in enumerate(colors):
                self.make_group('brightmistyeyes', (col, row), f'eyes{color}')
                self.make_group('brightmistyeyestwo', (col, row), f'eyes2{color}')

        for row, colors in enumerate(dullmistyeyes):
            for col, color in enumerate(colors):
                self.make_group('dullmistyeyes', (col, row), f'eyes{color}')
                self.make_group('dullmistyeyestwo', (col, row), f'eyes2{color}')

        for row, colors in enumerate(glowmistyeyes):
            for col, color in enumerate(colors):
                self.make_group('glowmistyeyes', (col, row), f'eyes{color}')
                self.make_group('glowmistyeyestwo', (col, row), f'eyes2{color}')

        for row, colors in enumerate(supermistyeyes):
            for col, color in enumerate(colors):
                self.make_group('supermistyeyes', (col, row), f'eyes{color}')
                self.make_group('supermistyeyestwo', (col, row), f'eyes2{color}')

        # Define white patches
        white_patches = [
            ['FULLWHITE', 'ANY', 'TUXEDO', 'LITTLE', 'COLOURPOINT', 'VAN', 'ANYTWO', 'MOON', 'PHANTOM', 'POWDER',
             'BLEACHED', 'SAVANNAH', 'FADESPOTS', 'PEBBLESHINE'],
            ['EXTRA', 'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG', 'RAGDOLL', 'LIGHTSONG', 'VITILIGO', 'BLACKSTAR',
             'PIEBALD', 'CURVED', 'PETAL', 'SHIBAINU', 'OWL'],
            ['TIP', 'FANCY', 'FRECKLES', 'RINGTAIL', 'HALFFACE', 'PANTSTWO', 'GOATEE', 'VITILIGOTWO', 'PAWS', 'MITAINE',
             'BROKENBLAZE', 'SCOURGE', 'DIVA', 'BEARD'],
            ['TAIL', 'BLAZE', 'PRINCE', 'BIB', 'VEE', 'UNDERS', 'HONEY', 'FAROFA', 'DAMIEN', 'MISTER', 'BELLY',
             'TAILTIP', 'TOES', 'TOPCOVER'],
            ['APRON', 'CAPSADDLE', 'MASKMANTLE', 'SQUEAKS', 'STAR', 'TOESTAIL', 'RAVENPAW', 'PANTS', 'REVERSEPANTS',
             'SKUNK', 'KARPATI', 'HALFWHITE', 'APPALOOSA', 'DAPPLEPAW'],
            ['HEART', 'LILTWO', 'GLASS', 'MOORISH', 'SEPIAPOINT', 'MINKPOINT', 'SEALPOINT', 'MAO', 'LUNA', 'CHESTSPECK',
             'WINGS', 'PAINTED', 'HEARTTWO', 'WOODPECKER'],
            ['BOOTS', 'MISS', 'COW', 'COWTWO', 'BUB', 'BOWTIE', 'MUSTACHE', 'REVERSEHEART', 'SPARROW', 'VEST',
             'LOVEBUG', 'TRIXIE', 'SAMMY', 'SPARKLE'],
            ['RIGHTEAR', 'LEFTEAR', 'ESTRELLA', 'SHOOTINGSTAR', 'EYESPOT', 'REVERSEEYE', 'FADEBELLY', 'FRONT',
             'BLOSSOMSTEP', 'PEBBLE', 'TAILTWO', 'BUDDY', 'BACKSPOT', 'EYEBAGS'],
            ['BULLSEYE', 'FINN', 'DIGIT', 'KROPKA', 'FCTWO', 'FCONE', 'MIA', 'SCAR', 'BUSTER', 'SMOKEY', 'HAWKBLAZE',
             'CAKE', 'ROSINA', 'PRINCESS'],
            ['LOCKET', 'BLAZEMASK', 'TEARS', 'DOUGIE']
        ]

        # minks white patches
        minkswhite = [
            ['MINKONE', 'MINKTWO', 'MINKTHREE', 'MINKFOUR', 'MINKREDTAIL', 'MINKDELILAH', 'MINKHALF', 'MINKSTREAK', 'MINKMASK', 'MINKSMOKE'],
            ['MINKMINIMALONE', 'MINKMINIMALTWO', 'MINKMINIMALTHREE', 'MINKMINIMALFOUR', 'MINKOREO', 'MINKSWOOP', 'MINKCHIMERA', 'MINKCHEST', 
             'MINKARMTAIL', 'MINKGRUMPYFACE'],
            ['MINKMOTTLED', 'MINKSIDEMASK', 'MINKEYEDOT', 'MINKBANDANA', 'MINKPACMAN', 'MINKSTREAMSTRIKE', 'MINKSMUDGED', 'MINKDAUB', 
             'MINKEMBER', 'MINKBRIE'],
            ['MINKORIOLE', 'MINKROBIN', 'MINKBRINDLE', 'MINKPAIGE', 'MINKROSETAIL', 'MINKSAFI', 'MINKDAPPLENIGHT', 'MINKBLANKET', 
             'MINKBELOVED', 'MINKBODY'],
            ['MINKSHILOH', 'MINKFRECKLED', 'MINKHEARTBEAT']
        ]

        for row, patches in enumerate(white_patches):
            for col, patch in enumerate(patches):
                self.make_group('whitepatches', (col, row), f'white{patch}')
        
        for row, patches in enumerate(minkswhite):
            for col, patch in enumerate(patches):
                self.make_group('minkswhite', (col, row), f'white{patch}')

        # Define colors and categories
        color_categories = [
            ['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST', 'BLACK'],
            ['CREAM', 'PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'SIENNA'],
            ['LIGHTBROWN', 'LILAC', 'BROWN', 'GOLDEN-BROWN', 'DARKBROWN', 'CHOCOLATE']
        ]

        color_types = [
            'singlecolours', 'tabbycolours', 'marbledcolours', 'rosettecolours',
            'smokecolours', 'tickedcolours', 'speckledcolours', 'bengalcolours',
            'mackerelcolours', 'classiccolours', 'sokokecolours', 'agouticolours',
            'singlestripecolours', 'maskedcolours',
            'dottedcolours', 'stripedcolours', 'wildcatcolours',  
            'ocelotcolours', 'lynxcolours', 'cheetahcolours',
            'bobtailcolours', 'manedwolfcolours'
        ]

        for row, colors in enumerate(color_categories):
            for col, color in enumerate(colors):
                for color_type in color_types:
                    self.make_group(color_type, (col, row), f'{color_type[:-7]}{color}')

        # tortiepatchesmasks
        tortiepatchesmasks = [
            ['ONE', 'TWO', 'THREE', 'FOUR', 'REDTAIL', 'DELILAH', 'HALF', 'STREAK', 'MASK', 'SMOKE'],
            ['MINIMALONE', 'MINIMALTWO', 'MINIMALTHREE', 'MINIMALFOUR', 'OREO', 'SWOOP', 'CHIMERA', 'CHEST', 'ARMTAIL',
             'GRUMPYFACE'],
            ['MOTTLED', 'SIDEMASK', 'EYEDOT', 'BANDANA', 'PACMAN', 'STREAMSTRIKE', 'SMUDGED', 'DAUB', 'EMBER', 'BRIE'],
            ['ORIOLE', 'ROBIN', 'BRINDLE', 'PAIGE', 'ROSETAIL', 'SAFI', 'DAPPLENIGHT', 'BLANKET', 'BELOVED', 'BODY'],
            ['SHILOH', 'FRECKLED', 'HEARTBEAT']
        ]

        minkstorties = [
            ['MINKFULLWHITE', 'MINKANY', 'MINKTUXEDO', 'MINKLITTLE', 'MINKCOLOURPOINT', 'MINKVAN', 'MINKANYTWO', 'MINKMOON', 
             'MINKPHANTOM', 'MINKPOWDER', 'MINKBLEACHED', 'MINKSAVANNAH', 'MINKFADESPOTS', 'MINKPEBBLESHINE'],
            ['MINKEXTRA', 'MINKONEEAR', 'MINKBROKEN', 'MINKLIGHTTUXEDO', 'MINKBUZZARDFANG', 'MINKRAGDOLL', 'MINKLIGHTSONG', 
             'MINKVITILIGO', 'MINKBLACKSTAR', 'MINKPIEBALD', 'MINKCURVED', 'MINKPETAL', 'MINKSHIBAINU', 'MINKOWL'],
            ['MINKTIP', 'MINKFANCY', 'MINKFRECKLES', 'MINKRINGTAIL', 'MINKHALFFACE', 'MINKPANTSTWO', 'MINKGOATEE', 'MINKVITILIGOTWO', 
             'MINKPAWS', 'MINKMITAINE', 'MINKBROKENBLAZE', 'MINKSCOURGE', 'MINKDIVA', 'MINKBEARD'],
            ['MINKTAIL', 'MINKBLAZE', 'MINKPRINCE', 'MINKBIB', 'MINKVEE', 'MINKUNDERS', 'MINKHONEY', 'MINKFAROFA', 'MINKDAMIEN', 
             'MINKMISTER', 'MINKBELLY', 'MINKTAILTIP', 'MINKTOES', 'MINKTOPCOVER'],
            ['MINKAPRON', 'MINKCAPSADDLE', 'MINKMASKMANTLE', 'MINKSQUEAKS', 'MINKSTAR', 'MINKTOESTAIL', 'MINKRAVENPAW', 'MINKPANTS', 
             'MINKREVERSEPANTS', 'MINKSKUNK', 'MINKKARPATI', 'MINKHALFWHITE', 'MINKAPPALOOSA', 'MINKDAPPLEPAW'],
            ['MINKHEART', 'MINKLILTWO', 'MINKGLASS', 'MINKMOORISH', 'MINKSEPIAPOINT', 'MINKMINKPOINT', 'MINKSEALPOINT', 'MINKMAO', 
             'MINKLUNA', 'MINKCHESTSPECK', 'MINKWINGS', 'MINKPAINTED', 'MINKHEARTTWO', 'MINKWOODPECKER'],
            ['MINKBOOTS', 'MINKMISS', 'MINKCOW', 'MINKCOWTWO', 'MINKBUB', 'MINKBOWTIE', 'MINKMUSTACHE', 'MINKREVERSEHEART',
             'MINKSPARROW', 'MINKVEST', 'MINKLOVEBUG', 'MINKTRIXIE', 'MINKSAMMY', 'MINKSPARKLE'],
            ['MINKRIGHTEAR', 'MINKLEFTEAR', 'MINKESTRELLA', 'MINKSHOOTINGSTAR', 'MINKEYESPOT', 'MINKREVERSEEYE', 'MINKFADEBELLY', 
             'MINKFRONT', 'MINKBLOSSOMSTEP', 'MINKPEBBLE', 'MINKTAILTWO', 'MINKBUDDY', 'MINKBACKSPOT', 'MINKEYEBAGS'],
            ['MINKBULLSEYE', 'MINKFINN', 'MINKDIGIT', 'MINKKROPKA', 'MINKFCTWO', 'MINKFCONE', 'MINKMIA', 'MINKSCAR', 'MINKBUSTER', 
             'MINKSMOKEY', 'MINKHAWKBLAZE', 'MINKCAKE', 'MINKROSINA', 'MINKPRINCESS'],
            ['MINKLOCKET', 'MINKBLAZEMASK', 'MINKTEARS', 'MINKDOUGIE']
        ]

        for row, masks in enumerate(tortiepatchesmasks):
            for col, mask in enumerate(masks):
                self.make_group('tortiepatchesmasks', (col, row), f"tortiemask{mask}")

        for row, masks in enumerate(minkstorties):
            for col, mask in enumerate(masks):
                self.make_group('minkstorties', (col, row), f"tortiemask{mask}")

        # Define skin colors 
        skin_colors = [
            ['BLACK', 'RED', 'PINK', 'DARKBROWN', 'BROWN', 'LIGHTBROWN'],
            ['DARK', 'DARKGREY', 'GREY', 'DARKSALMON', 'SALMON', 'PEACH'],
            ['DARKMARBLED', 'MARBLED', 'LIGHTMARBLED', 'DARKBLUE', 'BLUE', 'LIGHTBLUE']
        ]

        for row, colors in enumerate(skin_colors):
            for col, color in enumerate(colors):
                self.make_group('skin', (col, row), f"skin{color}")

        self.load_scars()

    def load_scars(self):
        """
        Loads scar sprites and puts them into groups.
        """
        # Define scars
        scars_data = [
            ["ONE", "TWO", "THREE", "MANLEG", "BRIGHTHEART", "MANTAIL", "BRIDGE", "RIGHTBLIND", "LEFTBLIND",
             "BOTHBLIND", "BURNPAWS", "BURNTAIL"],
            ["BURNBELLY", "BEAKCHEEK", "BEAKLOWER", "BURNRUMP", "CATBITE", "RATBITE", "FROSTFACE", "FROSTTAIL",
             "FROSTMITT", "FROSTSOCK", "QUILLCHUNK", "QUILLSCRATCH"],
            ["TAILSCAR", "SNOUT", "CHEEK", "SIDE", "THROAT", "TAILBASE", "BELLY", "TOETRAP", "SNAKE", "LEGBITE",
             "NECKBITE", "FACE"],
            ["HINDLEG", "BACK", "QUILLSIDE", "SCRATCHSIDE", "TOE", "BEAKSIDE", "CATBITETWO", "SNAKETWO", "FOUR"]
        ]

        # define missing parts
        missing_parts_data = [
            ["LEFTEAR", "RIGHTEAR", "NOTAIL", "NOLEFTEAR", "NORIGHTEAR", "NOEAR", "HALFTAIL", "NOPAW"]
        ]

        # scars 
        for row, scars in enumerate(scars_data):
            for col, scar in enumerate(scars):
                self.make_group('scars', (col, row), f'scars{scar}')

        # missing parts
        for row, missing_parts in enumerate(missing_parts_data):
            for col, missing_part in enumerate(missing_parts):
                self.make_group('missingscars', (col, row), f'scars{missing_part}')

        # accessories
        medcatherbs_data = [
            ["MAPLE LEAF", "HOLLY", "BLUE BERRIES", "FORGET ME NOTS", "RYE STALK", "LAUREL"],
            ["BLUEBELLS", "NETTLE", "POPPY", "LAVENDER", "HERBS", "PETALS"],
            [],  # Empty row because this is the wild data, except dry herbs.
            ["OAK LEAVES", "CATMINT", "MAPLE SEED", "JUNIPER"]
        ]

        wild_data = [
            ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS", "MOTH WINGS", "CICADA WINGS"]
        ]

        collars_data = [
            ["CRIMSON", "BLUE", "YELLOW", "CYAN", "RED", "LIME"],
            ["GREEN", "RAINBOW", "BLACK", "SPIKES", "WHITE"],
            ["PINK", "PURPLE", "MULTI", "INDIGO"]
        ]

        bellcollars_data = [
            ["CRIMSONBELL", "BLUEBELL", "YELLOWBELL", "CYANBELL", "REDBELL", "LIMEBELL"],
            ["GREENBELL", "RAINBOWBELL", "BLACKBELL", "SPIKESBELL", "WHITEBELL"],
            ["PINKBELL", "PURPLEBELL", "MULTIBELL", "INDIGOBELL"]
        ]

        bowcollars_data = [
            ["CRIMSONBOW", "BLUEBOW", "YELLOWBOW", "CYANBOW", "REDBOW", "LIMEBOW"],
            ["GREENBOW", "RAINBOWBOW", "BLACKBOW", "SPIKESBOW", "WHITEBOW"],
            ["PINKBOW", "PURPLEBOW", "MULTIBOW", "INDIGOBOW"]
        ]

        nyloncollars_data = [
            ["CRIMSONNYLON", "BLUENYLON", "YELLOWNYLON", "CYANNYLON", "REDNYLON", "LIMENYLON"],
            ["GREENNYLON", "RAINBOWNYLON", "BLACKNYLON", "SPIKESNYLON", "WHITENYLON"],
            ["PINKNYLON", "PURPLENYLON", "MULTINYLON", "INDIGONYLON"]
        ]

        # ohdan's accessories / wild's accessories / superartsi's accessories / coffee's accessories / eragona rose's accessories

        # wild's expanded accessories

        extrawild_data = [
            ["LILYPAD", "LARGE DEATHBERRY", "SMALL DEATHBERRY", "ACORN2", "PINECONE", "VINE"],
            ["CHERRY2", "BLEEDING HEARTS", "SHELL PACK", "FERNS", "GOLD FERNS", "AUTUMN FERNS"],
            ["WHEAT", "BLACK WHEAT"]
        ]

        extrawild2_data = [ 
            ["BERRIES", "CLOVERS", "CLOVER", "MOSS", "FLOWER MOSS", "RED MUSHROOM"]
        ]

        extrawild3_data = [ 
            ["LARGE LUNA", "LARGE COMET", "SMALL LUNA", "MORPHO BUTTERFLY"],
            ["MUD PAWS"]
        ]

        # superartsi
        superartsi_data = [
            ["ORANGEBUTTERFLY", "BLUEBUTTERFLY", "BROWNPELT", "GRAYPELT", "BROWNMOSSPELT", "GRAYMOSSPELT"],
            ["FERN", "MOREFERN", "BLEEDINGHEART", "LILY"]
        ]
        
        flower_accessories_data = [
           ["DAISY", "DIANTHUS", "BLEEDING HEARTS", "FRANGIPANI", "BLUE GLORY", "CATNIP FLOWER", "BLANKET FLOWER", 
            "ALLIUM", "LACELEAF", "PURPLE GLORY"],
           ["YELLOW PRIMROSE", "HESPERIS", "MARIGOLD", "WISTERIA"]
        ]

        crowns_data = [
            ["PINKFLOWERCROWN", "YELLOWFLOWERCROWN", "BLUEFLOWERCROWN", "PURPLEFLOWERCROWN"]
        ]

        crowns2_data = [
            ["YELLOWCROWN", "REDCROWN", "LILYPADCROWN"]
        ]

        plant2_accessories_data = [
            ["CLOVER", "STICK", "PUMPKIN", "MOSS", "IVY", "ACORN", "MOSS PELT", "REEDS", "BAMBOO"]
        ]
        
        snake_accessories_data = [
            ["GRASS SNAKE", "BLUE RACER", "WESTERN COACHWHIP", "KINGSNAKE"]
        ]

        smallAnimal_accessories_data = [
            ["GRAY SQUIRREL", "RED SQUIRREL", "CRAB", "WHITE RABBIT", "BLACK RABBIT", "BROWN RABBIT", "INDIAN GIANT SQUIRREL", 
            "FAWN RABBIT", "BROWN AND WHITE RABBIT", "BLACK AND WHITE RABBIT"],
            ["WHITE AND FAWN RABBIT", "BLACK VITILIGO RABBIT", "BROWN VITILIGO RABBIT", "FAWN VITILIGO RABBIT", "BLACKBIRD", "ROBIN", 
             "JAY", "THRUSH", "CARDINAL", "MAGPIE"],
            ["CUBAN TROGON", "TAN RABBIT", "TAN AND WHITE RABBIT", "TAN VITILIGO RABBIT", "RAT", "WHITE MOUSE", "BLACK MOUSE", "GRAY MOUSE", 
             "BROWN MOUSE", "GRAY RABBIT"],
            ["GRAY AND WHITE RABBIT", "GRAY VITILIGO RABBIT"]
        ]
            
        deadInsect_accessories_data = [
            ["LUNAR MOTH", "ROSY MAPLE MOTH", "MONARCH BUTTERFLY", "DAPPLED MONARCH", "POLYPHEMUS MOTH", "MINT MOTH"]
        ]
         
        aliveInsect_accessories_data = [
            ["BROWN SNAIL", "RED SNAIL", "WORM", "BLUE SNAIL", "ZEBRA ISOPOD", "DUCKY ISOPOD", "DAIRY COW ISOPOD", "BEETLEJUICE ISOPOD", 
             "BEE", "RED LADYBUG"],
            ["ORANGE LADYBUG", "YELLOW LADYBUG"]
        ]
            
        fruit_accessories_data = [
            ["RASPBERRY", "BLACKBERRY", "GOLDEN RASPBERRY", "CHERRY", "YEW"]
        ]
        
        crafted_accessories_data = [
            ["WILLOWBARK BAG", "CLAY DAISY POT", "CLAY AMANITA POT", "CLAY BROWNCAP POT", "BIRD SKULL", "LEAF BOW"]
        ]

        crafted2_accessories_data = [
            ["FIDDLEHEADS", "LANTERNS", "HEARTCHARMS", "CHIMES"]
        ]

        raincoat_data = [
            ["RAINCOAT"]
        ]
        
        poptabs_data = [
            ["POPTABS"]
        ]

        fazbear_data = [
            ["FAZBEAR"]
        ]

        bears_data = [
            ["WHITEBEAR", "PANDA", "BEAR", "BROWNBEAR"]
        ]

        tide_data = [
            ["TIDE"]
        ]

        chimes_data = [
            ["CELESTIALCHIMES", "STARCHIMES", "LUNARCHIMES", "SILVERLUNARCHIMES"]
        ]

        tail2_accessories_data = [
            ["SEAWEED", "DAISY CORSAGE"]
        ]

        harness_data = [
            ["REDHARNESS", "NAVYHARNESS", "YELLOWHARNESS", "TEALHARNESS", "ORANGEHARNESS", "GREENHARNESS"],
            ["MOSSHARNESS", "RAINBOWHARNESS", "BLACKHARNESS", "BEEHARNESS", "CREAMHARNESS"],
            ["PINKHARNESS", "MAGENTAHARNESS", "PEACHHARNESS", "VIOLETHARNESS"]
        ]

        wooddragon_data = [
            ["WOODDRAGON"]
        ]

        springwinter_accessories_data = [
            ["CHERRYBLOSSOM","TULIPPETALS","CLOVERFLOWER","PANSIES","BELLFLOWERS","SANVITALIAFLOWERS", "EGGSHELLS","BLUEEGGSHELLS",
             "EASTEREGG","FORSYTHIA"],
            ["MINTLEAF","STICKS","SPRINGFEATHERS","SNAILSHELL","MUD","CHERRYPLUMLEAVES","CATKIN","HONEYCOMB",
             "FLOWERCROWN","LILIESOFTHEVALLEY"],
            ["STRAWMANE","MISTLETOE","REDPOINSETTIA","WHITEPOINSETTIA","COTONEASTERWREATH","YEWS","HEATHER", "TEETHCOLLAR","DRIEDORANGE",
             "ROESKULL"],
            ["WOODENOAKANTLERS","WOODENBIRCHANTLERS","DOGWOOD","GRAYWOOL","BLACKWOOL","CREAMWOOL","WHITEWOOL", "FIRBRANCHES",
             "CORALBELLS","SLIVERDUSTPLANT"]
        ]

        # medcatherbs
        for row, herbs in enumerate(medcatherbs_data):
            for col, herb in enumerate(herbs):
                self.make_group('medcatherbs', (col, row), f'acc_herbs{herb}')
        self.make_group('medcatherbs', (5, 2), 'acc_herbsDRY HERBS')

        # wilds
        for row, wilds in enumerate(wild_data):
            for col, wild in enumerate(wilds):
                self.make_group('medcatherbs', (col, 2), f'acc_wild{wild}')

        # collars
        for row, collars in enumerate(collars_data):
            for col, collar in enumerate(collars):
                self.make_group('collars', (col, row), f'collars{collar}')

        # bellcollars
        for row, bellcollars in enumerate(bellcollars_data):
            for col, bellcollar in enumerate(bellcollars):
                self.make_group('bellcollars', (col, row), f'collars{bellcollar}')

        # bowcollars
        for row, bowcollars in enumerate(bowcollars_data):
            for col, bowcollar in enumerate(bowcollars):
                self.make_group('bowcollars', (col, row), f'collars{bowcollar}')

        # nyloncollars
        for row, nyloncollars in enumerate(nyloncollars_data):
            for col, nyloncollar in enumerate(nyloncollars):
                self.make_group('nyloncollars', (col, row), f'collars{nyloncollar}')
        
        # CUSTOM ACCESSORIES

        # wild's mod
        for row, extrawilds in enumerate(extrawild_data):
            for col, extrawild in enumerate(extrawilds):
                sprites.make_group('wildacc', (col, row), f'acc_herbs{extrawild}')

        for row, extrawild2s in enumerate(extrawild2_data):
            for col, extrawild2 in enumerate(extrawild2s):
                sprites.make_group('wildacc2', (col, row), f'acc_herbs{extrawild2}')

        for row, extrawild3s in enumerate(extrawild3_data):
            for col, extrawild3 in enumerate(extrawild3s):      
                sprites.make_group('wildacc3', (col, row), f'acc_wild{extrawild3}')

        # superartsi accessories
        for row, superartsis in enumerate(superartsi_data):
            for col, superartsi in enumerate(superartsis):
                self.make_group('superartsi', (col, row), f'acc_wild{superartsi}')
                self.make_group('superartsi', (col, 1), f'acc_wild{superartsi}')

        # flower accessories
        for row, flowers in enumerate(flower_accessories_data):
            for col, flower in enumerate(flowers):
                self.make_group('flower_accessories', (col, row), f'acc_flower{flower}')

        # coffee's accessories - flower crowns
        for row, flowercrowns in enumerate(crowns_data):
            for col, flowercrown in enumerate(flowercrowns):
                 self.make_group('coffee', (col, row), f'acc_flower{flowercrown}')

        # flower crowns2
        for row, flower2crowns in enumerate(crowns2_data):
            for col, flower2crown in enumerate(flower2crowns):
                 self.make_group('crowns', (col, row), f'acc_wild{flower2crown}')

        # plant2 accessories
        for row, plant2s in enumerate(plant2_accessories_data):
            for col, plant2 in enumerate(plant2s):
                self.make_group('plant2_accessories', (col, row), f'acc_plant2{plant2}')
        
        # snake accessories
        for row, snakes in enumerate(snake_accessories_data):
            for col, snake in enumerate(snakes):
                self.make_group('snake_accessories', (col, row), f'acc_snake{snake}')
        
        # small animal accessories
        for row, smallanimals in enumerate(smallAnimal_accessories_data):
            for col, smallanimal in enumerate(smallanimals):
                self.make_group('smallAnimal_accessories', (col, row), f'acc_smallAnimal{smallanimal}')
        
        # dead insect accessories
        for row, deadinsects in enumerate(deadInsect_accessories_data):
            for col, deadinsect in enumerate(deadinsects):
                self.make_group('deadInsect_accessories', (col, row), f'acc_deadInsect{deadinsect}')

        # alive insect accessories
        for row, aliveinsects in enumerate(aliveInsect_accessories_data):
            for col, aliveinsect in enumerate(aliveinsects):
                self.make_group('aliveInsect_accessories', (col, row), f'acc_aliveInsect{aliveinsect}')
        
        # fruit accessories
        for row, fruits in enumerate(fruit_accessories_data):
            for col, fruit in enumerate(fruits):
                self.make_group('fruit_accessories', (col, row), f'acc_fruit{fruit}')

        # crafted accessories
        for row, crafts in enumerate(crafted_accessories_data):
            for col, craft in enumerate(crafts):
                self.make_group('crafted_accessories', (col, row), f'acc_crafted{craft}')
        
        # moipa - crafted2 accessories
        for row, craft2s in enumerate(crafted2_accessories_data):
            for col, craft2 in enumerate(craft2s):
                self.make_group('moipa', (col, row), f'acc_crafted{craft2}')

        # tail2 accessories
        for row, tail2s in enumerate(tail2_accessories_data):
            for col, tail2 in enumerate(tail2s):
                self.make_group('tail2_accessories', (col, row), f'acc_tail2{tail2}')
        
        # harness accessories
        for row, harnesses in enumerate(harness_data):
            for col, harness in enumerate(harnesses):
                self.make_group('eragona', (col, row), f'collars{harness}')
                self.make_group('eragona', (col, 1), f'collars{harness}')
                self.make_group('eragona', (col, 2), f'collars{harness}')

        # wood dragon accessory
        for row, wooddragons in enumerate(wooddragon_data):
            for col, wooddragon in enumerate(wooddragons):
                self.make_group('wooddragon', (col, row), f'acc_wild{wooddragon}')
        
        # springwinter accessories
        for row, springwinters in enumerate(springwinter_accessories_data):
            for col, springwinter in enumerate(springwinters):
                self.make_group('springwinter', (col, row), f'acc_wild{springwinter}')
        
        # raincoat accessory
        for row, raincoats in enumerate(raincoat_data):
            for col, raincoat in enumerate(raincoats):
                self.make_group('raincoat', (col, row), f'acc_crafted{raincoat}')
        
        # poptabs accessory
        for row, poptabs in enumerate(poptabs_data):
            for col, poptab in enumerate(poptabs):
                self.make_group('poptabs', (col, row), f'acc_crafted{poptab}')
        
        # fazbear accessory
        for row, fazbears in enumerate(fazbear_data):
            for col, fazbear in enumerate(fazbears):
                self.make_group('fazbear', (col, row), f'acc_crafted{fazbear}')
        
        # bears accessories
        for row, bears in enumerate(bears_data):
            for col, bear in enumerate(bears):
                self.make_group('bears', (col, row), f'acc_crafted{bear}')
        
        # tide accessory
        for row, tides in enumerate(tide_data):
            for col, tide in enumerate(tides):
                self.make_group('tide', (col, row), f'acc_crafted{tide}')
        
        # chimes acccessories
        for row, chimes in enumerate(chimes_data):
            for col, chime in enumerate(chimes):
                self.make_group('chimes', (col, row), f'acc_crafted{chime}')
            

# CREATE INSTANCE 
sprites = Sprites()
sprites.load_all()

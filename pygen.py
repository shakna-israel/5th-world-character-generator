import random

def choose_name(sex):
    unisex_names = ["Cameron","Jordan","Taylor","Tyler","Jamie","Casey","Bailey","Cassidy","Presley","Cori","Cory","Dylan","Devin","Jayden","Ashton","Avery","Blair","Brett","Chandler","Kendall","Lane","Morgan","Perry","Parker","Peyton","Quinn","Raegan","Reese","Shayne","Skylar","Spencer","Sydney","Alex","Danny","Kelley","Ashley","Sam","Jesse","Jessie","Kyle","Dakota","Shawn","Sean","Blake","Brooke","Casey","Hayden","Jaden","Avery","Bailey","Carson","Drew","Kennedy"]
    if sex == "male":
        male_names = ["Nicolas","Bernardo","Maximiliano","Matias","Vicente","Elijah","Jeronimo","Jacob","Davi","Antonio","Josiah","James","Ryan","Felipe","Omar","Yassin","Moshe","Andres","Felipe","Abdallah","Logan","Tomas","Charles","Jesus","Pierre","Diego","Jaden","Santiago","Mohamed","Habib","Benjamin","Jack","Deven","Hassan","Peter","George","Carter","Liam","Oliver","Benjamin","Diego","Alejandro","Khaled","Jackson","Samuel","Liam","Mark","Ethan","Richard","Ishaan","Benjamin","Juan","Ibrahim","Selim","Adrian","Kirollos","Juan","Sebastian","Jaxson","Beshoi","Mamadou","Suraj","Stevenson","Abdel-Rahman","David","Mohammed","Alexis","Arthur","Hussein","Manuel","William","Rafael","Hamza","Miguel","angel","Carter","Angel","Matheus","Tareq","Owen","Martin","Ethan","Arnav","Bautista","Mahmoud","Peterson","Thiago","Ricardo","Wilson","Jameson","Joseph","William","Juan","Andres","Fadi","Mohamed","Santiago","Juan","David","Iker","Jack","Daniel","Alejandro","Heitor","Liam","Nathan","Jose","Lukas","Fabian","Dyllan","Karim","Olivier","Amir","Halim","Logan","Robert","Neil","Aiden","Sebastian","Emmanuel","Muhammad","Juan","Jose","Santino","Ian","Kevin","Keven","Hunter","Liam","Jason","Ajani","Felix","Daniel","Ali","Jeremiah","Mehdi","Alonso","Samuel","Bilal","Youssef","Aryan","Armaan","Luis","Alexander","Jayden","Dylan","Ahmed","Javier","Michael","Justin","Gabriel","Noah","Liam","Joaquin","Miguel","Taha","Cesar","Carlos","Samuel","Ramon","Joshua","Nikhil","Thomas","Murad","Noah","Mina","Mustafa","Mateo","Logan","Alejandro","Stanley","Evens","Liam","Eric","Pedro","Rohan","Lucas","Jaxon","Hudson","Mason","Oliver","Agustin","Martin","John","Matthew"]
        name_selection = male_names + unisex_names
        choice = random.choice(name_selection) + " " + random.choice(name_selection)
        return choice
    elif sex == "female":
        female_names = ["Tiare", "Hinano", "Poema", "Maeva", "Hina", "Vaea", "Titaua", "Moea", "Moeata", "Tarita", "Titaina", "Teura", "Heikapu", "Mareva", "Shaimaa", "Fatma", "Maha", "Reem", "Farida", "Aya", "Shahd", "Ashraqat", "Sahar", "Fatin", "Dalal", "Doha", "Fajr", "Suha", "Rowan", "Hosniya", "Hasnaa", "Hosna", "Gamila", "Gamalat", "Habiba", "Mary", "Marie", "Mariam", "Marina", "Irene", "Malak", "Habiba", "Hana", "Farah", "Marwa", "Nada", "Salma"]
        name_selection = female_names + unisex_names
        choice = random.choice(name_selection) + " " + random.choice(name_selection)
        return choice
    else:
        print("Sex not male nor female.")
        raise TypeError

def choose_profession():
    professions = ["Unemployed","fabricshearer", "curate", "ship provisioner", "bottelier", "scythesmith", "link man", "captain", "mercer", "linener", "gong farmer", "sergeant-at-arms", "lacemaker", "linen-draper", "chaplain", "sheepshearer", "hatter", "master builder", "falconer", "scout", "accoucheur", "accoucheus", "cook", "surgeon", "harlot", "pilgrim", "carman", "knight", "minnesinger", "glasspainter", "stringer", "joiner", "fletcher", "thresher", "pastrycook", "knifesmith", "stonecarver", "dog trainer", "sperviter", "wattler", "billier", "hay merchant", "liner", "panter", "merchant taylor", "procurator", "piper", "ship's captain", "valet", "miniaturist", "tillerman", "nurse", "admiral", "reedmaker", "famulus", "weirkeeper", "urchin", "guild master", "clerk", "waller", "abbess", "unguentary", "raker", "poulter", "jongleur", "alchemist", "vintner", "pot mender", "bladesmith", "guide", "illuminator", "spicer", "grinder (occupation)", "bodyservant", "lorimer", "clark", "spy", "barker", "courtier", "composer", "pinmaker", "luthier", "seneschal", "linen-armorer", "ale-conner", "player (actor)", "oilmaker", "captain of the guard", "butler", "knifeman", "malemaker", "plasterer", "papermaker", "guardsman", "pie seller", "musician", "brightsmith", "legerdemainist", "transient", "royal food taster", "sculptor", "bartender", "campaner", "sailmaker", "vaginarius", "chamberlain", "laundress", "archer", "bodger", "userer", "barrister", "woodcutter", "woodward", "bearleader", "spearman", "shepherd", "teamster", "ostler", "salter", "weaponsmith", "pinder", "pikeman", "gardener", "drummer", "bear-ward", "cartier", "boothman", "thimblerigger", "bawd", "fishmonger", "gardner", "threadmaker", "chancery clerk", "knapper", "coiner", "molecatcher", "pursuivant", "linenspinner", "chapman", "riverboat pilot", "scrivener", "reaper", "gamekeeper", "bellmaker", "wiredrawer", "oynter", "mailmaker", "silk-mercer", "harness maker", "privycleaner", "meat butcher", "anchorite", "gentleman's gentleman", "pointer", "keeper of the wardrobe", "netmaker", "pissprophet", "reeve", "mummer", "beer seller", "blacksmith's striker", "glazier", "armorsmith", "housewife", "tile-theeker", "maid", "artisan", "farmer", "ceiler", "cardinal", "yeoman", "fool", "landed gentry", "footpad", "tumbler", "beekeeper", "hunter", "gunstocker", "bookprinter", "costermonger", "mathematician", "bellfounder", "herald", "peasant", "fisherman", "moneyer", "greengrocer", "shipchandler", "drywaller", "toad doctor", "brushbinder", "purse maker", "apothecary", "marler", "pewterer", "calligrapher", "scribe", "hacker", "broderer", "cordwainer", "nailmaker", "mason", "messenger", "herder", "goldbeater", "freibauer", "sexton", "dairymaid", "peddler", "fresco painter", "conman", "oil merchant", "minstrel", "delver", "rag and bone man", "hatmaker", "bowman", "stonecutter", "arrowsmith", "steward", "crossbowman", "blacksmith", "chainmaker", "attendent", "playwright", "beadle", "potter", "sailor", "tallowchandler", "glass seller", "navigator", "watchman", "combmaker", "carter", "cutpurse", "fuller", "exchequer", "swordsmith", "upholder", "miller", "woodcarver", "paperer (needlemaking)", "sergeant", "rectifier", "draper", "catchpole", "solicitor", "tapster", "trapper", "treasurer", "fruitier", "silk-dyer", "king", "bodyguard", "shill", "serf", "fueller", "architect", "carder", "mariner", "dapifer", "oysterer", "latoner", "scabbard maker", "corsetier", "pickpocket", "lawyer", "fewterer", "ditcher", "actuary", "cannoneer", "perfumer", "cardmaker", "armorer", "quarryman", "turner", "seamstress", "argolet", "lord high steward", "silversmith", "harper", "woodmonger", "cantor", "link boy", "lady's maid", "printer", "spinster", "furrier", "drayman", "clockmaker", "skinner", "librarian", "weeper", "prostitute", "plumber", "confectioner", "professor", "wine seller", "constable", "blockcutter", "balancemaker", "quilter", "poleturner", "fowler", "plattner", "clouter", "drycooper", "parker", "ironmonger", "pope", "stonemason", "wetnurse", "silkmaid", "camp cook", "master of the revels", "pardoner", "brazier (occupation)", "besom maker", "sheriff", "writer", "lighter man", "keeper of the privy seal", "gilder", "tile-burner", "stainer", "lutemaker", "foundryman", "accoutrement maker", "tailor", "ferryman", "diamantaire", "artist", "engraver", "spice merchant", "hobbler", "maidservant", "priest", "glover", "landlord", "girdler", "spurrer", "weaver", "farrier", "shipwright", "scribe,seneschal", "waxchandler", "nun", "bard", "metropolitan bishop", "diver", "bath attendent", "troubadour", "ackerman", "fence (criminal)", "drover", "purser", "grocer", "cartographer", "mapmaker", "tenter", "almoner", "tax collector", "thonger", "quack", "tasseler", "silk-maker", "waterman", "astrologer", "lanternmaker", "monk", "cofferer", "bandit", "theologian", "buckle maker", "executioner", "barber-chirurgeon", "arkwright", "pasteler", "oyster raker", "cartwright", "diver (criminal)", "dancer", "broom-dasher", "wood seller", "redsmith", "shrimper", "shingler", "typefounder", "beggar", "bookbinder", "roper", "storyteller", "tile maker", "currier", "tutor", "restaurateur", "poet", "chandler", "leech", "juggler", "chantry priest", "colporteur", "parish priest", "wheeler", "innkeeper", "poacher", "stationer", "waferer", "pattenmaker", "woolman", "shoemaker", "painter", "physician", "sacristan", "alewife", "sail maker", "wagoner", "camp follower", "stablehand", "tinsmith", "harberdasher", "silk-snatcher", "fruiterer", "glassblower", "brewer", "canon", "locksmith", "chicken butcher", "canvasser", "spooner", "embroiderer", "bricklayer", "doctor", "horseleech", "basketmaker", "waterseller", "butcher", "bishop", "buffoon", "chirurgeon", "horse trainer", "hermit", "noble", "meistersinger", "huntsman", "summoner (law)", "nakerer", "boothaler", "treen maker", "carver", "cheesemaker", "builder", "quartermaster", "bailiff", "gunsmith", "mintmaster", "silk-carder", "potboy", "milliner", "cabinetmaker", "lutenist", "charcoalburner", "feltmaker", "ropemaker", "riveter", "lampwright", "stewsman", "chimney sweep", "old-clothes dealer", "prince", "ostiary", "smith", "jeweler", "spinner", "gemcutter", "parchmenter", "coistsell", "clothier", "beerbrewer", "mirrorer", "plumer", "skald", "sawbones", "viking", "fortune teller", "bronzefounder", "knacker", "chancellor", "pioneer (siege)", "bather (profession)", "forester", "swineherd", "sapper", "judge", "stillroom", "lady", "marleywoman", "siever", "servant", "scullion", "toll keeper", "disher", "cutler", "friar", "dresser", "gravedigger", "woodturner", "dean", "pavyler", "primate (religion)", "trobairitz", "goatherd", "beguine", "saddler", "plowman", "nobleman", "cooper", "wheelwright", "stabler", "squire", "miner", "philosopher", "leadworker", "taverner", "alabasterer", "porter", "bowyer", "palmer", "jester", "ivorist", "tinker", "lighterman", "ragpicker", "roofer", "smelter", "militia", "banker", "archbishop", "emperor", "marshal", "fewtrer", "thacker", "silk-dresser", "bonecarver", "lancier", "halberdier", "compasssmith", "vagabond", "coppersmith", "milkmaid", "trencherman", "dung carter", "herbalist", "burglar", "boatman", "rugweaver", "jailer", "accountant", "minter", "cathar perfect", "wool stapler", "rugmaker", "canaller", "mailer", "cellarer", "cowherd", "lapidary", "singer", "saltboiler", "bagger", "nedeller", "webber", "keeper of the rolls", "arbalestier", "dyer", "bricker", "hetheleder", "eggler", "horner", "charlatan", "tanner", "copyist", "boatwright", "pavior", "water carrier", "woolcomber", "cobbler", "abbot", "midwife", "collier", "master of hounds", "courtesan", "diplomat", "fiddler", "bargeman", "seaweed harvester", "sea captain", "town crier", "actor", "crofter", "hayward", "limner", "hurdle maker", "tapestrymaker", "accomptant", "carpenter", "furniture maker", "acater", "napier", "hawker", "tapicer", "siege engineer", "rat catcher", "buttonmaker", "baker", "groom", "sawyer", "mercenary", "bleacher"]
    professions = [x.title() for x in professions]
    choice = random.choice(professions)
    return choice

def choose_age(minAge, maxAge):
    minAge = int(minAge)
    maxAge = int(maxAge)
    choice = random.randint(minAge, maxAge)
    return str(choice)

def choose_sex():
    chance = random.randint(0,1)
    if chance == 1:
        return "male"
    else:
        return "female"

def main():
    charSex = choose_sex()
    charName = choose_name(charSex)
    charProfession = choose_profession()
    charAge = choose_age(14,60)
    print("Sex: " + charSex + "\nName: " + charName + "\nProfession: " + charProfession + "\nAge: " + charAge)

if __name__ == "__main__":
    main()

def printColor(text, color, type):
    CEND      = '\033[0m'
    CRED    = '\033[91m'
    CGREEN  = '\033[32m'
    CYELLOW = '\033[33m'
    CBLUE   = '\033[34m'
    CVIOLET = '\033[35m'
    CBEIGE  = '\033[36m'
    if type == "print":
        if color.lower() == 'red':
            print(CRED + text + CEND)
        elif color.lower() == 'green':
            print(CGREEN + text + CEND)
        elif color.lower() == 'yellow':
            print(CYELLOW + text + CEND)
        elif color.lower() == 'blue':
            print(CBLUE + text + CEND)
        elif color.lower() == 'voilet':
            print(CVIOLET + text + CEND)
        elif color.lower() == 'beige':
            print(CBEIGE + text + CEND)
        elif color.lower() == 'green':
            return CGREEN + text + CEND
    else:
        if color.lower() == 'red':
            return CRED + text + CEND
        elif color.lower() == 'green':
            return CGREEN + text + CEND
        elif color.lower() == 'yellow':
            return CYELLOW + text + CEND
        elif color.lower() == 'blue':
            return CBLUE + text + CEND
        elif color.lower() == 'voilet':
            return CVIOLET + text + CEND
        elif color.lower() == 'beige':
            return CBEIGE + text + CEND
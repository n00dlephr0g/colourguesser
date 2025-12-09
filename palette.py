from colours import *
from ansi import *

class Palette():
    def __init__(self):
        self.palette = {
            # name: (r,g,b),n
            "black": [(0, 0, 0), 0],
            "white": [(255, 255, 255), 0]
        }
        self.maxNameLen = 5
        self.maxAmount = 0
        self.result = (0,0,0)
        self.mix()

    def mix(self) -> tuple:
        rTotal, gTotal, bTotal, nTotal = 0, 0, 0, 0
        for (r, g, b), n in self.palette.values():
            # weighted sum of each colour channel
            rTotal += r*n
            gTotal += g*n
            bTotal += b*n
            # add to the total counter
            nTotal += n
        # normalise the totals
        if nTotal == 0:
            return (0, 0, 0)
        rFinal = rTotal / nTotal
        gFinal = gTotal / nTotal
        bFinal = bTotal / nTotal
        # create final vector, and put in appropriate places
        rgbFinal = (rFinal, gFinal, bFinal)
        self.result = rgbFinal
    
    def show(self, header = "=", footer = "=", seperator = "-"):
        # calc
        numWidth = len(str(self.maxAmount))
        width = self.maxNameLen + 15 + numWidth
        
        if len(header) > 0:
            print(header[0]*width)
        
        # result
        rgb_print(
            " "*width, 
            background=self.result, 
            foreground=auto_compliment(self.result)
        )
        rgb_print(
            hexify(self.result).center(width), 
            background=self.result, 
            foreground=auto_compliment(self.result)
        )
        rgb_print(
            " "*width, 
            background=self.result, 
            foreground=auto_compliment(self.result)
        )
        
        if len(seperator) > 0:
            print(seperator[0]*width)
        
        # print each colour
        for name, (colour, amount) in self.palette.items():
            rgb_print(
                " " +
                format(name, f"{self.maxNameLen}")
                + " | " +
                hexify(colour) 
                + " | " +
                format(amount, f"{numWidth}")
                + " ", 
                background = colour,
                foreground = auto_compliment(colour)
            )
        if len(footer) > 0:
            print(footer[0]*width)


    def add_colour(self, name: str, value: tuple[int]):
        name = name.lower()
        rgb_validate(value)
        if len(name) > self.maxNameLen:
            self.maxNameLen = len(name)
        self.palette[name] = [value, 0]

    def add_hex(self, name: str, hexcode: str):
        self.add_colour(name, hex_to_rgb(hexcode))

    def set_amount(self, name: str, amount: int):
        name = name.lower()
        if amount < 0:
            raise ValueError("Colour amount cannot be less than 0")
        if name not in self.palette.keys():
            raise KeyError(f"Colour '{name}' not in palette")
        if amount > self.maxAmount:
            self.maxAmount = amount
        self.palette[name][1] = amount
        self.mix()
    
    def increment_amount(self, name: str, amount: int):
        if name not in self.palette.keys():
            raise KeyError(f"Colour '{name}' not in palette")
        self.set_amount(name, max(0, self.palette[name][1] + amount))

from colours import *
from ansi import *

class Palette():
    def __init__(self):
        self.components: dict[str:int] = {}
        self.history: list[dict[str:int]] = []
        self.result: tuple[int] = (0,0,0) # floatable values
        self.target: tuple[int] = (0,0,0) # Ease of calculation
        self.maxDist: float = (3*(256**2))**0.5

    # internal methods
    def __mix(self) -> tuple:
        rTotal, gTotal, bTotal, nTotal = 0, 0, 0, 0
        for hex, n in self.components.items():
            (r, g, b) = rgbify(hex)
            # weighted sum of each colour channel
            rTotal += r*n
            gTotal += g*n
            bTotal += b*n
            # add to the total counter
            nTotal += n
        if nTotal == 0:
            # return 0, 0, 0 if nothing
            rgbFinal = (0, 0, 0)
        else:
            # normalise the totals
            rFinal = rTotal / nTotal
            gFinal = gTotal / nTotal
            bFinal = bTotal / nTotal
            # create final vector, and put in appropriate places
            rgbFinal = (rFinal, gFinal, bFinal)
        self.result = rgbFinal
        self.history.append(rgbFinal)
        return self.result

    def __check_hexcode(self, hexcode: str) -> str:
        if not self.has_colour(hexcode):
            raise IndexError("Increment Error: Colour not in palette")
        return hexcode.upper()
    
    def __accuracy(self) -> float:
        # find distance with pythagorean
        r1, g1, b1 = self.result
        r2, g2, b2 = self.target
        distance = ((r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2) ** 0.5
        return (self.maxDist - distance) / self.maxDist
        
    
    # write methods
    def set_component(self, hexcode: str, amount: int = 0):
        amount = max(amount, 0)
        self.components[validate_hex(hexcode)] = amount
        self.__mix()

    def inc_component(self, hexcode: str, step: int):
        amount = self.components[self.__check_hexcode(hexcode)] + step
        self.set_component(hexcode, amount)
        self.__mix()
        
    def del_component(self, hexcode: str):
        self.components.pop(self.__check_hexcode(hexcode))
        self.__mix()
    
    def set_target(self, hexcode: str):
        self.target = rgbify(validate_hex(hexcode))
        
    def set_target_rgb(self, rgb: tuple[int]):
        self.target = validate_rgb(rgb)
    
    def undo(self, repeats: int = 0):
        if repeats < 1:
            raise ValueError("Undo Error: Cannot repeat less than once")
        if repeats > len(self.history):
            raise ValueError("Undo Error: Cannot repeat more than history size")
        for _ in range(repeats):
            self.components = self.history.pop()
        
    # read only methods
    def has_colour(self, hexcode: str | tuple):
        return hexcode.upper() in self.get_colours()
    
    def get_colours(self):
        return list(self.components.keys())
    
    def get_components(self):
        return self.components
    
    def copy(self):
        p = Palette()
        for hexcode in self.components.keys():
            p.set_component(hexcode)
        p.set_target(self.target)
        return p


# Tests 

if __name__ == "__main__":
    p = Palette()
    p.set_target("#8ACD46")
    p.set_component("#0FFFF5", amount= 1)

class Mixer():
    def __init__(self):
        self.palette = {
            "black": [[0, 0, 0], 0],
            "white": [[255, 255, 255], 0],
            "r": [[255, 0, 0], 0],
            "g": [[0, 255, 0], 0],
            "b": [[0, 0, 255], 0],
            "c": [[0, 255, 255], 0],
            "m": [[255, 0, 255], 0],
            "y": [[255, 255, 0], 0]
        }
        self.colour = [0, 0, 0]

    def set_palette(self, color: str, value: list[int]):
        if color in self.palette.keys() and color not in ["black", "white"]:
            self.palette[color][0] = value
    
    def get_palette(self):
        return self.palette
    
    def get_colour(self):
        return self.colour
    
    def mix(self) -> list:
        rTotal, gTotal, bTotal, nTotal = 0
        for values in self.palette.values():
            # compute dot product of each colour, add to tally
            rgb, n = values
            r, g, b = rgb
            rTotal += r*n
            gTotal += g*n
            bTotal += b*n
            nTotal += n
        # normalise the totals
        rFinal = rTotal / nTotal
        gFinal = gTotal / nTotal
        bFinal = bTotal / nTotal
        # create final vector, and put in appropriate places
        rgbFinal = [rFinal, gFinal, bFinal]
        self.colour = rgbFinal
        return rgbFinal
    
    
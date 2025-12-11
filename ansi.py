from colours import *
from palette import Palette

def setForeground(colour: tuple[int]):
    validate_rgb(colour)
    r, g, b = colour
    print(f"\033[38;2;{r};{g};{b}m", end="")
    
def setBackground(colour: tuple[int]):
    validate_rgb(colour)
    r, g, b = colour
    print(f"\033[48;2;{r};{g};{b}m", end="")
    
def reset():
    print("\033[0m", end="")

def rgb_print(text: str, foreground: tuple[int] | None = None, background: list[int] | None = None, end: str = "\n"):
    fg = ""
    bg = ""
    if foreground is not None:
        validate_rgb(foreground)
        r,g,b = foreground
        fg = f"38;2;{round(r)};{round(g)};{round(b)}"
    if background is not None:
        validate_rgb(background)
        r,g,b = background
        bg = f"48;2;{round(r)};{round(g)};{round(b)}"
    if foreground is not None and background is not None:
        fg += ";"
    print(f"\033[{fg}{bg}m{text}", end=end)
    reset()

def printPalette(p: Palette):
    pass




def rgb_validate(rgb: list[int]) -> int:
    if len(rgb) < 3 or len(rgb) > 3:
        raise KeyError("Invalid RGB: Missing or extra values")
    if max(rgb) > 255 or min(rgb) < 0:
        raise ValueError("Invalid RGB: Values out of range")
    return 0

def hex_validate(hexcode: str) -> int:
    if len(hexcode) != 7:
        raise ValueError("Invalid Hexcode: Must contain '#' followed by 6 digits")
    if hexcode[0] != "#":
        raise ValueError("Invalid Hexcode: Must contain '#' followed by 6 digits")
    if 0 < int(hexcode[1:3], 16) < 255 \
    or 0 < int(hexcode[3:5], 16) < 255 \
    or 0 < int(hexcode[5:7], 16) < 255:
        raise ValueError("Invalid Hexcode: Values out of range")
    return 0

def hex_to_rgb(hexcode: str) -> list[int]:
    hex_validate(hexcode)
    return (
        int(hexcode[1:3], 16),  # red
        int(hexcode[3:5], 16),  # green
        int(hexcode[5:7], 16)   # blue
    )
    
def hexify(rgb: list[int]):
    rgb_validate(rgb)
    r, g, b = rgb
    return f"#{format(round(r), "02X")}{format(round(g), "02X")}{format(round(b), "02X")}"

def brightness(rgb):
    rgb_validate(rgb)
    r,g,b = rgb
    y = 0.2126 * r + 0.7152 * g + 0.0722 * b
    return y

def auto_compliment(colour: tuple[int]):
    rgb_validate(colour)
    compliment = (255,255,255)
    if brightness(colour) > 127:
        compliment = (0,0,0) # black
    return compliment
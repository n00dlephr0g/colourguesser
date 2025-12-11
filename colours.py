
def validate_rgb(rgb: tuple[int]) -> tuple[int]:
    if not isinstance(rgb, tuple[int]):
        raise TypeError("Invalid RGB: Must be of type 'tuple[int]'")
    if len(rgb) != 3:
        raise KeyError("Invalid RGB: Missing or extra values")
    if max(rgb) > 255 or min(rgb) < 0:
        raise ValueError("Invalid RGB: Values out of range")
    return tuple(rgb)

def validate_hex(hexcode: str) -> str:
    if not isinstance(hexcode, str):
        raise TypeError("Invalid Hexcode: Not of type 'str'")
    if len(hexcode) != 7 or hexcode[0] != "#":
        raise ValueError("Invalid Hexcode: Must contain '#' followed by 6 digits")
    if 0 < int(hexcode[1:3], 16) < 255 \
    or 0 < int(hexcode[3:5], 16) < 255 \
    or 0 < int(hexcode[5:7], 16) < 255:
        raise ValueError("Invalid Hexcode: Values out of range")
    return hexcode.upper()

def rgbify(hexcode: str) -> tuple[int]:
        validate_hex(hexcode)
        return (
            int(hexcode[1:3], 16),  # red
            int(hexcode[3:5], 16),  # green
            int(hexcode[5:7], 16)   # blue
        )
    
def hexify(rgb: tuple[int]):
    r, g, b = validate_rgb(rgb)
    return f"#{format(round(r), "02X")}{format(round(g), "02X")}{format(round(b), "02X")}"

def get_luma(colour: str | tuple[int]):
    rgb = rgbify(colour)
    r,g,b = rgb
    y = 0.2126 * r + 0.7152 * g + 0.0722 * b
    return y

def auto_contrast(colour: tuple[int]):
    validate_rgb(colour)
    compliment = (255,255,255)
    if get_luma(colour) > 127:
        compliment = (0,0,0) # black
    return compliment
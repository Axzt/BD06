def hex_to_rgb(hex_color):
    if not is_hexadecimal(hex_color):
        raise Exception("not a hex color")
    return (int(hex_color[:2],16), int(hex_color[2:4],16), int(hex_color[4:],16))

def is_hexadecimal(hex_string):
    try:
        if len(hex_string) == 6:
            int(hex_string,16)
            return True
    except Exception:
        return False

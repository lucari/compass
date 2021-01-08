degrees = 0

def on_forever():
    global degrees
    degrees = input.compass_heading()
    if degrees < 22:
        basic.show_arrow(ArrowNames.NORTH)
    elif degrees < 67:
        basic.show_arrow(ArrowNames.NORTH_EAST)
    elif degrees < 112:
        basic.show_arrow(ArrowNames.EAST)
    elif degrees < 157:
        basic.show_arrow(ArrowNames.SOUTH_EAST)
    elif degrees < 202:
        basic.show_arrow(ArrowNames.SOUTH)
    elif degrees < 247:
        basic.show_arrow(ArrowNames.SOUTH_WEST)
    elif degrees < 292:
        basic.show_arrow(ArrowNames.WEST)
    elif degrees < 337:
        basic.show_arrow(ArrowNames.NORTH_WEST)
    else:
        basic.show_arrow(ArrowNames.NORTH)
basic.forever(on_forever)

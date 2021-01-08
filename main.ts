let degrees = 0
basic.forever(function on_forever() {
    
    degrees = input.compassHeading()
    if (degrees < 22) {
        basic.showArrow(ArrowNames.North)
    } else if (degrees < 67) {
        basic.showArrow(ArrowNames.NorthEast)
    } else if (degrees < 112) {
        basic.showArrow(ArrowNames.East)
    } else if (degrees < 157) {
        basic.showArrow(ArrowNames.SouthEast)
    } else if (degrees < 202) {
        basic.showArrow(ArrowNames.South)
    } else if (degrees < 247) {
        basic.showArrow(ArrowNames.SouthWest)
    } else if (degrees < 292) {
        basic.showArrow(ArrowNames.West)
    } else if (degrees < 337) {
        basic.showArrow(ArrowNames.NorthWest)
    } else {
        basic.showArrow(ArrowNames.North)
    }
    
})

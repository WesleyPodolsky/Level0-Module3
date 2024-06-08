def setup():
    # Set the size of your sketch
    size(500, 500)
    
    pass
    
def draw():
    sizeX = 500
    sizeY = 500
    # Starting with the largest ellipse, use a for loop to draw a bullseye with ellipses
    for i in range(5):
        if i %2 ==0:
            fill('#FF0000')
        elif i == i:
            fill('#FFFFFF')
        ellipse(250,250,sizeX,sizeY)
        sizeX = sizeX/1.5
        sizeY = sizeY/1.5
    
        
    # Use an if statement and modulo to alternate the color of your rings
    
    
    pass

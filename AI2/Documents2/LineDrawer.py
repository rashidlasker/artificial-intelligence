
def imageNoise(points, image):
    from random import randint
    for n in range(points):
        r = randint(0, HEIGHT-1)
        c = randint(0, WIDTH-1)
        image[WIDTH*r+c] = 255
#-------------------------------------------------------------------------------------------------
def drawLine(m,b,image):
    for r in range(HEIGHT):
       for c in range(WIDTH):
          index = WIDTH*r+c
          if r == int(m*c) + b:
              image[index] = 255
#-------------------------------------------------------------------------------------------------
HEIGHT = 512
WIDTH = 512
image = [0] * HEIGHT * WIDTH
imageNoise(500, image)
drawLine(0, 200, image)
drawLine(2, 100, image)
newFile = open('/afs/csl.tjhsst.edu/students/2016/2016rlasker/Documents2/linedrawer.ppm', 'w')
newFile.write('P3' + '\n')
newFile.write(str(WIDTH) + ' ' + str(HEIGHT) + '\n')
newFile.write('255' + '\n')
for r in range(HEIGHT):
     for c in range(WIDTH):
        index = WIDTH*r+c
        newFile.write(str(image[index]) + ' ' + str(image[index]) + ' ' + str(image[index]) + ' ')

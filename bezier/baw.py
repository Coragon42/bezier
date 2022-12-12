import cImage, sys, math, numpy

def colorDistance(pix1,pix2):
    '''Returns Euclidean color distance between two Pixels'''
    rdif = pix1.getRed()-pix2.getRed()
    gdif = pix1.getGreen()-pix2.getGreen()
    bdif = pix1.getBlue()-pix2.getBlue()
    return math.sqrt(rdif*rdif+gdif*gdif+bdif*bdif)


def main():
    '''Takes a bitmap and turns it into ppm with only black and white pixels.'''
    file = input('Enter file name: ')
    name = file.split('.')[0]
    img = cImage.FileImage(file)
    width = img.getWidth()
    height = img.getHeight()
    black = cImage.Pixel(0,0,0)
    white = cImage.Pixel(255,255,255)
    baw = cImage.EmptyImage(width,height)
    for x in numpy.arange(width):
        for y in numpy.arange(height):
            pix = img.getPixel(x,y)
            if colorDistance(pix,black) > colorDistance(pix,white):
                baw.setPixel(x,y,white)
            else:
                baw.setPixel(x,y,black)
    namebaw = f'{name}-baw'
    baw.save(namebaw,'ppm')
    win = cImage.ImageWin(namebaw,width,height)
    baw.draw(win)
    win.exitOnClick()

main()
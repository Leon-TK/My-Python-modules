import sys

from skimage import io, color
from skimage import img_as_ubyte

"""Converts a rgb file image to rgb bw image with Cielab lightness"""
"""Tested on .jpg file format"""
"""Place script into your PATH, run python -m RgbToCielabLightness <jpg-file-path>\
    or create symbollink of python.exe with script path (or -m approach) and drag jpg file (win10), but dont forget to set working directory"""

def waitUser():
    input()

def readFile(imageFilePath):
    return io.imread(imageFilePath)
def convertToLab(rgb):
    return color.rgb2lab(rgb)
def eraseAbChannels(labImg):
    labImg[:, :, 1] = 0
    labImg[:, :, 2] = 0
def convertToRgb(labImg):
    return color.lab2rgb(labImg)
def convertToUnit(floatImg):
    return img_as_ubyte(floatImg)

def main():
    imageFilePath = sys.argv[1]

    convertedToLab = convertToLab(readFile(imageFilePath))

    eraseAbChannels(convertedToLab)

    io.imsave("cielabLightness.jpg", convertToUnit(convertToRgb(convertedToLab)))

if __name__ == "__main__":
    try:
        main()
    except:
        waitUser()
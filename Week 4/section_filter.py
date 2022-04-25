"""
This program loads an image and applies the narok filter
to it by setting "bright" pixels to grayscale values.
"""

from simpleimage import SimpleImage

BRT_THRES = 153

def go_grayscale(pixel):
    """
    Turn a pixel into grayscale.
    """
    avg_rgb = (pixel.red + pixel.green + pixel.blue) / 3
    if avg_rgb > BRT_THRES:
        pixel.red = avg_rgb
        pixel.green = avg_rgb
        pixel.blue = avg_rgb

def main():
    image = SimpleImage('images/simba-sq.jpg')

    # Apply the filter
    # TODO: your code here
    for pixel in image:
        # replace a bright pixel with a grayscale equivalent
        # if the average RGB is greater than BRT_THRES
        go_grayscale(pixel)

    image.show()

if __name__ == '__main__':
    main()

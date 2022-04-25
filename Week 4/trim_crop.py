from simpleimage import SimpleImage

def main():
    image = SimpleImage('images/karel.png')
    # image.show()
    trimmed_img = trim_crop_image(image, 30)
    trimmed_img.show()

def trim_crop_image(original_img, trim_size):
    """
    This function returns a new SimpleImage which is a trimmed and
    cropped version of the original image by shaving trim_sz pixels
    from each side (top, left, bottom, right) of the image. You may
    assume trim_sz is less than half the width of the image.

    Inputs:
        - original_img: The original image to process
        - trim_size: The number of pixels to shave from each side
                   of the original image

    Returns:
        A new SimpleImage with trim_sz pixels shaved off each
        side of the original image
    """
    # print the original image's information
    img_width = original_img.width
    img_height = original_img.height
    print("There are %d pixels that form the width of the picture of Karel." % (img_width))
    print("There are %d pixels that form the height of the picture of Karel." % (img_height))
    # initiate a blank image that has the cropped size
    trimmed_img = SimpleImage.blank(img_width-trim_size*2,img_height-trim_size*2)
    # can only scan in this way: for each column (x), go through all
    # the rows (y). if x is smaller than trim_size or larger than
    # img_width - trim_size, then make all rows in this column white pixels
    # (i.e., the ones with RGB (255, 255, 255)); else, make only the
    # first 30 and last 30 rows white pixels.
    # we will use a nested for loop first
    for x in range(img_width):  # iterate through the columns
        for y in range(img_height):
            pixel = original_img.get_pixel(x,y)
            two_sides = (x < trim_size) or (x > img_width - trim_size - 1)
            two_bars = (not two_sides) and ((y < trim_size) or (y > img_height - trim_size - 1))
            if not (two_sides or two_bars):
                trimmed_img.set_pixel(x-trim_size,y-trim_size,pixel)
    return trimmed_img

if __name__ == '__main__':
    main()

from simpleimage import SimpleImage

def main():
    image = SimpleImage('images/simba-sq.jpg')
    image.show()
    bordered_img = add_border(image, 10)
    bordered_img.show()

def set_black(pixel):
    """
    Set a pixel to be black.
    :param pixel: the pixel to set black.
    """
    pixel.red = 0
    pixel.green = 0
    pixel.blue = 0

def add_border(original_img, border_size):
    """
    This function returns a new SimpleImage which is the same as
    original image except with a black border added around it. The
    border should be border_size many pixels thick.

    Inputs:
        - original_img: The original image to process
        - border_size: The thickness of the border to add around the image

    Returns:
        A new SimpleImage with the border added around original image
    """
    # render some pixels to be black
    dim = (original_img.width, original_img.height)
    print(f"The dimensionality of the original image is {dim[0]} pixel(s) wide " + 
          f"and {dim[1]} pixel(s) high.")
    new_dim = (dim[0] + border_size * 2, dim[1] + border_size * 2)
    print(f"The dimensionality of the bordered image is {new_dim[0]} pixel(s) wide " + 
          f"and {new_dim[1]} pixel(s) high.")
    new_w = new_dim[0]
    new_h = new_dim[1]
    bordered_img = SimpleImage.blank(new_w,new_h)
    for x in range(new_w):
        for y in range(new_h):
            current_pixel = bordered_img.get_pixel(x,y)
            top_pos = border_size
            bottom_pos = bordered_img.height - border_size - 1
            on_border = (x < top_pos or x > bottom_pos) \
                        or ((top_pos <= x <= bottom_pos) and \
                        (y < top_pos or y > bottom_pos))
            if on_border:
                set_black(current_pixel)
            else:
                upd_pixel = original_img.get_pixel(x-border_size,y-border_size)
                bordered_img.set_pixel(x,y,upd_pixel)
    return bordered_img

if __name__ == '__main__':
    main()

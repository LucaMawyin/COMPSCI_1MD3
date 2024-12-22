from PIL import Image
from typing import List


def mirror(raw: List[List[List[int]]])-> None:
    """
    Assume raw is image data. Modifies raw by reversing all the rows
    of the data.

    >>> raw = [[[233, 100, 115], [0, 0, 0], [255, 255, 255]],
               [[199, 201, 116], [1, 9, 0], [255, 255, 255]]]
    >>> mirror(raw)
    >>> raw
    [[[255, 255, 255], [0, 0, 0], [233, 100, 115]],
     [[255, 255, 255], [1, 9, 0], [199, 201, 116]]]
    """

    for row in range (len(raw)):

        # Not having //2 mirrors it until halfway and then mirrors the mirror
        for col in range (len(raw[0])//2):

            # Taking first col
            temp = raw[row][col]

            # Swap pixels from outside
            # Working its way in
            raw[row][col] = raw[row][len(raw[row])-1-col]
            raw[row][len(raw[row])-1-col] = temp

def grey(raw: List[List[List[int]]])-> None:
    """
    Assume raw is image data. Modifies raw "averaging out" each
    pixel of raw. Specifically, for each pixel it totals the RGB
    values, integer divides by three, and sets the all RGB values
    equal to this new value

    >>> raw = [[[233, 100, 115], [0, 0, 0], [255, 255, 255]],
               [[199, 201, 116], [1, 9, 0], [255, 255, 255]]]
    >>> grey(raw)
    >>> raw
    [[[149, 149, 149], [0, 0, 0], [255, 255, 255]],
     [[172, 172, 172], [3, 3, 3], [255, 255, 255]]]
    """

    # for each row
    for row in range (len(raw)):

        # for each col
        for col in range (len(raw[0])):

            avgClr = 0

            # Finding avg colour in a pixel
            for rgbVal in range(3):

                avgClr += raw[row][col][rgbVal]

            avgClr //= 3

            # Changing pixel to avg
            for rgbVal in range (3):
                raw[row][col][rgbVal] = avgClr

def invert(raw: List[List[List[int]]])->None:
    """
    Assume raw is image data. Modifies raw inverting each pixel.
    To invert a pixel, you swap all the max values, with all the
    minimum values. See the doc tests for examples.

    >>> raw = [[[233, 100, 115], [0, 0, 0], [255, 255, 0]],
               [[199, 201, 116], [1, 9, 0], [255, 100, 100]]]
    >>> invert(raw)
    >>> raw
    [[[100, 233, 115], [0, 0, 0], [0, 0, 255]],
     [[199, 116, 201], [1, 0, 9], [100, 255, 255]]]
    """
    
    for i in range(len(raw)):

        for j in range (len(raw[0])):

            # Finding min + max
            minVal = 255
            maxVal = 0

            for pixel in range(3):
                # THERES 4 PIXEL VALUES
                # CAN'T INCLUDE ALPHA
                # NEED TO HARD CODE 3 AS RANGE
                # THIS GAVE ME SUCH A HEADACHE

                # NOTE: Pixel can be both max and min

                # Pixel is a min
                if raw[i][j][pixel] < minVal:
                    minVal = raw[i][j][pixel]

                # Pixel is a max
                if raw[i][j][pixel] > maxVal:
                    maxVal = raw[i][j][pixel]

            # Replacing maxes with mins and vice versa
            for pixel in range (3):
                if raw[i][j][pixel] == minVal:
                    raw[i][j][pixel] = maxVal

                elif raw[i][j][pixel] == maxVal:
                    raw[i][j][pixel] = minVal

def merge(raw1: List[List[List[int]]], raw2: List[List[List[int]]])-> List[List[List[int]]]:
    """
    Merges raw1 and raw2 into new raw image data and returns it.
    It merges them using the following rule/procedure.
    1) The new raw image data has height equal to the max height of raw1 and raw2
    2) The new raw image data has width equal to the max width of raw1 and raw2
    3) The pixel data at cell (i,j) in the new raw image data will be (in this order):
       3.1) a black pixel [0, 0, 0], if there is no pixel data in raw1 or raw2
       at cell (i,j)
       3.2) raw1[i][j] if there is no pixel data at raw2[i][j]
       3.3) raw2[i][j] if there is no pixel data at raw1[i][j]
       3.4) raw1[i][j] if i is even
       3.5) raw2[i][j] if i is odd
    """

    newImg = []
    zeroVec = [0,0,0]

    for i in range (max(len(raw1),len(raw2))):

        temp = []

        for j in range (max(len(raw1[0]),len(raw2[0]))):

            # I'M ACTUALLY A GENIUS
            # This is the furthest simplification you can get for the conditionals

            # abcde are variables that represent the truth of a given statement
            a = i < len(raw1)
            b = j < len(raw1[i]) if a else False # Evaluates if raw1[i] exists else False
            c = i < len(raw2)
            d = j < len(raw2[i]) if c else False # Evaluates if raw2[i] exists else False
            e = i % 2 == 0

            # (Only raw1[i][j] exists) or (i is even and raw1[i][j] exists)
            if (a and b) and (not(c and d) or e):
                temp.append(raw1[i][j])

            # (Only raw2[i][j] exists) or (i is odd and raw2[i][j] exists)
            elif (c and d) and (not(a and b) or not e):
                temp.append(raw2[i][j])

            # raw1[i][j] nor raw2[i][j] exist
            else:
                temp.append(zeroVec)

        newImg.append(temp)
    
    return newImg

def compress(raw: List[List[List[int]]])-> List[List[List[int]]]:
    """
    Compresses raw by going through the pixels and combining a pixel with
    the ones directly to the right, below and diagonally to the lower right.
    For each RGB values it takes the average of these four pixels using integer
    division. If is is a pixel on the "edge" of the image, it only takes the
    relevant pixels to average across. See the second doctest for an example of
    this.

    >>> raw = [[[233, 100, 115], [0, 0, 0], [255, 255, 0], [3, 6, 7]],
               [[199, 201, 116], [1, 9, 0], [255, 100, 100], [99, 99, 0]],
               [[200, 200, 200], [1, 9, 0], [255, 100, 100], [99, 99, 0]],
               [[50, 100, 150], [1, 9, 0], [211, 5, 22], [199, 0, 10]]]
    >>> raw1 = compress(raw)
    >>> raw1
    [[[108, 77, 57], [153, 115, 26]],
     [[63, 79, 87], [191, 51, 33]]]

    >>> raw = [[[233, 100, 115], [0, 0, 0], [255, 255, 0]],
               [[199, 201, 116], [1, 9, 0], [255, 100, 100]],
               [[123, 233, 151], [111, 99, 10], [0, 1, 1]]]
    >>> raw2 = compress(raw)
    >>> raw2
    [[[108, 77, 57], [255, 177, 50]],
     [[117, 166, 80], [0, 1, 1]]]
    """

    # Rounding length + width up
    newImgWidth = -(-len(raw)//2)
    newImgLen = -(-len(raw[0])//2)

    # Creating empty image
    newImg = [0]*newImgWidth
    for row in range(len(newImg)):
        newImg[row] = [0]*newImgLen
        for col in range(len(newImg[row])):
            newImg[row][col] = [0]*3
    
    # Compressing pixels 
    # Works by default for even height + width
    for i in range (0,len(raw)-1,2):
        for j in range (0,len(raw[0])-1,2):
            for pixel in range (3):
                newImg[i//2][j//2][pixel] = (raw[i][j][pixel] + raw[i+1][j][pixel] + 
                                             raw[i][j+1][pixel] + raw[i+1][j+1][pixel])//4
    

    if len(raw) % 2 == 1 and len(raw[0]) % 2 == 1:

        # Rows
        for i in range (len(newImg)-1):
            for pixel in range(3):
                newImg[i][len(newImg[i]) - 1][pixel] = (raw[i*2][len(raw[i*2])-1][pixel] + raw[(i*2)+1][len(raw[i*2])-1][pixel])//2
        
        # Columns
        for i in range (len(newImg[0])-1):
            for pixel in range(3):
                newImg[len(newImg) - 1][i][pixel] = (raw[len(raw)-1][i*2][pixel] + raw[len(raw)-1][(i*2)+1][pixel])//2
        
        # Corner
        newImg[len(newImg) - 1][len(newImg[0]) - 1] = raw[len(raw)-1][len(raw[0])-1]
                
    
    # If height is odd but width is even
    elif len(raw) % 2 == 1 and len(raw[0]) % 2 == 0:
        # Columns
        for i in range (len(newImg[0])):
            for pixel in range(3):
                newImg[len(newImg) - 1][i][pixel] = (raw[len(raw)-1][i*2][pixel] + raw[len(raw)-1][(i*2)+1][pixel])//2

    # If width is odd but height is even
    elif len(raw) % 2 == 0 and len(raw[0]) % 2 == 1:
        # Rows
        for i in range (len(newImg)):
            for pixel in range(3):
                newImg[i][len(newImg[i]) - 1][pixel] = (raw[i*2][len(raw[i*2])-1][pixel] + raw[(i*2)+1][len(raw[i*2])-1][pixel])//2

    return newImg

"""
**********************************************************

Do not worry about the code below. However, if you wish,
you can us it to read in images, modify the data, and save
new images.

**********************************************************
"""

def get_raw_image(name: str)-> List[List[List[int]]]:
    
    image = Image.open(name)
    num_rows = image.height
    num_columns = image.width
    pixels = image.getdata()
    new_data = []
    
    for i in range(num_rows):
        new_row = []
        for j in range(num_columns):
            new_pixel = list(pixels[i*num_columns + j])
            new_row.append(new_pixel)
        new_data.append(new_row)

    image.close()
    return new_data

def image_from_raw(raw: List[List[List[int]]], name: str)->None:
    image = Image.new("RGB", (len(raw[0]),len(raw)))
    pixels = []
    for row in raw:
        for pixel in row:
            pixels.append(tuple(pixel))
    image.putdata(pixels)
    image.save(name)
#! /usr/bin/python
#import png
import numpy as np
from PIL import Image



def JuliaSet(k, size):
    # initialise an empty array to store the results
    img_array = np.zeros([size, size,3], int)

    #scales a grid down to fit into the -2 to 2 complex unit square
    c = np.zeros([size, size], complex)
    for x in range(0, size):
        for y in range(0, size):
            c[x, y] = x * 4 / size - 2 + (y * 4 / size - 2)*1j
            y += 1
        x += 1         
   
    for x in range(0, size):
        for y in range(0, size):
            n = 0
            while abs(c[x,y]) < 20 and n < 1023:
                # apply Julia Map dynamic, function can be changed for weirdness
                c[x,y] = c[x,y] ** 2 + k
                #sets the increments in which shaders are applied, letting n=1 takes longer to render but makes better pictures
                n+= 1
            img_array[x,y] = [min(n,255),int(n/4),int(n/8)]
            y += 1
        x += 1   

    return img_array
 
if __name__ == "__main__":

    k = complex(input("Enter complex coordinates to center the Julia Set: ")) #Location of Julia Sets
    size = int(input("Enter the size of the image you want: ")) # size of final image, higher number means better resolution
 
    #don't mess with these lines
    img_array = np.zeros([size, size,3], int )
 
    print ("rendering Julia Set...")
    img_array = JuliaSet(k, size)

    print ("saving JuliaSet" + str(k) + " " + str(size) + ".png")


    newimage = Image.new('RGB', (len(img_array[0]), len(img_array)))  # type, size
    newimage.putdata([tuple(p) for row in img_array for p in row])
    newimage.save('JuliaSet' + str(k) + ' '+ str(size) + '.png')  # takes type from filename extension
    # save to final render to png file
   # png.from_array(img_array,mode='RGB;8').save()

    print ("Done.")
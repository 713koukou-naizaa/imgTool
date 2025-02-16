import cv2
import numpy as np

def resize_nearest_neighbor():
    base_img_path = get_user_base_image_path()
    scale_factor = get_user_scale_factor()

    base_img = cv2.imread(base_img_path) # get base image

    # get base image dimensions
    base_height = base_img.shape[0] # height
    base_width = base_img.shape[1] # width

    # get new dimensions based on scale factor
    new_width = int(base_width * scale_factor)
    new_height = int(base_height * scale_factor)

    print("resizing" + base_img_path + " by " + str(scale_factor))

    # create new empty image with new dimensions
    new_img = np.zeros((new_height, new_width, 3), np.uint8) # 3 for RGB, np.uint8 for 8-bit unsigned integer values (0-255)

    # precompute mapping from new image coordinates to base image coordinates to avoid computing them each time in the nested loops
    # pixel at (i, j) in new image corresponds to pixel at (i/scale_factor, j/scale_factor) in base image
    base_row_indices = [int(i/scale_factor) for i in range(new_height)]
    base_col_indices = [int(j/scale_factor) for j in range(new_width)]
    
    for i in range(new_height):
        for j in range(new_width):
            new_img[i, j] = base_img[base_row_indices[i], base_col_indices[j]] # set new image pixel to base image pixel

    # save image
    new_img_path = input("path to save resized image (path/to/new_img.ext): ")
    new_img = cv2.imwrite(new_img_path, new_img)

    cv2.destroyAllWindows()

    print("resized " + base_img_path + " (" + str(base_width) + "x" + str(base_height) + ") as " + new_img_path + " (" + str(new_width) + "x" + str(new_height) + ")")

def resize_bilinear():
    print("not implemented")

def resize_bicubic():
    print("not implemented")

def resize_lanczos():
    print("not implemented")

def get_user_base_image_path():
    data_is_valid = False
    while True:
        base_img_path = input("path to base image (path/to/base_img.ext): ") # path to base image

        # check validity of base image path
        if cv2.imread(base_img_path) is None:
            print("invalid base image path")
        else:
            data_is_valid = True

        if data_is_valid:
            return base_img_path
        
def get_user_scale_factor():
    data_is_valid = False
    while True:
        scale_factor = float(input("scale factor: ")) # by how much to scale the image
            
        if scale_factor <= 0:
            print("invalid scale factor")
        else:
            data_is_valid = True

        if data_is_valid:
            return scale_factor

def resize_menu():
    print("what algorithm do you want to use?")
    print("0. exit")
    print("1. nearest neighbor (fast, duplicates pixels)")
    print("2. bilinear interpolation (smoother, averages nearby pixels)")
    print("3. bicubic interpolation (quality, uses weighted averages)")
    print("4. lanczos resampling (high quality, preserves details)")

    choice = int(input("choice: "))

    match choice:
        case 0:
            exit()
        case 1:
            resize_nearest_neighbor()
        case 2:
            resize_bilinear()
        case 3:
            resize_bicubic()
        case 4:
            resize_lanczos()
        case _:
            print("invalid choice, please write one of the followings: 0, 1, 2, 3, 4, 5")
            resize_menu()

def horizontal_vertical_mirroring():
    base_img_path = get_user_base_image_path()

    base_img = cv2.imread(base_img_path) # get base image

    # get base image dimensions
    base_height = base_img.shape[0] # height
    base_width = base_img.shape[1] # width

    print("horizontally and vertically mirroring image")

    # create new empty image with same dimensions
    new_img = np.zeros((base_height, base_width, 3), np.uint8) # 3 for RGB, np.uint8 for 8-bit unsigned integer values (0-255)

    # horizontal and vertical mirroring algorithm
    for i in range(base_height):
        mirrored_i = base_height - i - 1 # precompute mirrored i before second loop to avoid calculating it for each pixel (it is now calculated only the number of rows their are)
        for j in range(base_width):
            new_img[i, j] = base_img[mirrored_i, base_width - j - 1] # set pixel of new image to mirrored pixel of base image

    # save image
    new_img_path = input("path to save resized image (path/to/new_img.ext): ")
    new_img = cv2.imwrite(new_img_path, new_img)

    cv2.destroyAllWindows()

    print("horizontally and vertically mirrored " + base_img_path + " as " + new_img_path)

def horizontal_mirroring():
    base_img_path = get_user_base_image_path()

    base_img = cv2.imread(base_img_path) # get base image

    # get base image dimensions
    base_height = base_img.shape[0] # height
    base_width = base_img.shape[1] # width

    print("horizontally mirroring image")

    # create new empty image with same dimensions
    new_img = np.zeros((base_height, base_width, 3), np.uint8) # 3 for RGB, np.uint8 for 8-bit unsigned integer values (0-255)

    # horizontal mirroring algorithm
    for i in range(base_height):
        for j in range(base_width):
            # precomputing mirrired j can't be done because this is the last loop
            new_img[i, j] = base_img[i, base_width - j - 1] # set pixel of new image to mirrored pixel of base image

    # save image
    new_img_path = input("path to save resized image (path/to/new_img.ext): ")
    new_img = cv2.imwrite(new_img_path, new_img)

    cv2.destroyAllWindows()

    print("horizontally mirrored " + base_img_path + " as " + new_img_path)

def vertical_mirroring():
    base_img_path = get_user_base_image_path()

    base_img = cv2.imread(base_img_path) # get base image

    # get base image dimensions
    base_height = base_img.shape[0] # height
    base_width = base_img.shape[1] # width

    print("vertically mirroring image")

    # create new empty image with same dimensions
    new_img = np.zeros((base_height, base_width, 3), np.uint8) # 3 for RGB, np.uint8 for 8-bit unsigned integer values (0-255)

    # vertical mirroring algorithm
    for i in range(base_height):
        mirrored_i = base_height - i -1 # precompute mirrored i before second loop to avoid calculating it for each pixel (it is now calculated only the number of rows their are)
        for j in range(base_width):
            # precomputing mirrired j can't be done because this is the last loop
            new_img[i, j] = base_img[mirrored_i, j] # set pixel of new image to mirrored pixel of base image

    # save image
    new_img_path = input("path to save resized image (path/to/new_img.ext): ")
    new_img = cv2.imwrite(new_img_path, new_img)

    cv2.destroyAllWindows()

    print("vertically mirrored " + base_img_path + " as " + new_img_path)

def mirror_menu():
    print('0. exit')
    print('1. vertical mirroring')
    print('2. horizontal mirroring')
    print('3. horizontal + vertical')

    choice = int(input('choice: '))

    match choice:
        case 0:
            exit()
        case 1:
            vertical_mirroring()
        case 2:
            horizontal_mirroring()
        case 3:
            horizontal_vertical_mirroring()
        case _:
            print("invalid choice, please write one of the followings: 0, 1, 2")
            mirror_menu()

def mainloop():
    print("what do you want to do?")
    print("0. exit")
    print("1. resize")
    print("2. mirror")

    choice = int(input("choice: "))

    match choice:
        case 0:
            exit()
        case 1:
            resize_menu()
        case 2:
            mirror_menu()
        case _:
            print("invalid choce, please write one of the followings: 0, 1")
            mainloop()


def main():
    mainloop()



if __name__ == "__main__":
    main()
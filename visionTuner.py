import cv2
import numpy as np

def resize_nearest_neighbor():
    base_img_path, scale_factor = get_resize_user_input()

    base_img = cv2.imread(base_img_path) # get base image

    # get base image dimensions
    base_height = base_img.shape[0] # height
    base_width = base_img.shape[1] # width

    # get new dimensions based on scale factor
    new_width = int(base_width * scale_factor)
    new_height = int(base_height * scale_factor)

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

def get_resize_user_input():
    while True:
        data_is_valid = False

        base_img_path = input("path to base image (path/to/base_img.ext): ") # path to base image

        # check validity of base image path
        if cv2.imread(base_img_path) is None:
            print("invalid base image path")
        else:
            scale_factor = float(input("scale factor: ")) # by how much to scale the image
            
            if scale_factor <= 0:
                print("invalid scale factor")
            else:
                data_is_valid = True
                print("resizing" + base_img_path + " by " + str(scale_factor))

        if data_is_valid:
            return base_img_path, scale_factor

def resize():
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
            resize()

def mainloop():
    print("what do you want to do?")
    print("0. exit")
    print("1. resize")

    choice = int(input("choice: "))

    match choice:
        case 0:
            exit()
        case 1:
            resize()
        case _:
            print("invalid choce, please write one of the followings: 0, 1")
            mainloop()


def main():
    mainloop()



if __name__ == "__main__":
    main()
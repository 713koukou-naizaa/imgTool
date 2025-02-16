import cv2
import numpy as np

def resize_nearest_neighbor():
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
            break

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



def mainloop():
    print("1. resize nearest neighbor")
    print("2. exit")

    choice = int(input("choice: "))

    match choice:
        case 1:
            resize_nearest_neighbor()
        case 2:
            exit()

def main():
    mainloop()


if __name__ == "__main__":
    main()
from PIL import Image, ImageTk
import numpy as np
from copy import deepcopy


class JPEG2000:
    @staticmethod
    def brightness_shift(img_arr):
        img_arr_copy = img_arr.copy()

        mean_R = np.mean(img_arr_copy[:,:,0])
        mean_G = np.mean(img_arr_copy[:,:,1])
        mean_B = np.mean(img_arr_copy[:,:,2])

        # img_arr_copy[:,:,0] -= mean_R
        # img_arr_copy[:,:,1] -= mean_G
        # img_arr_copy[:,:,2] -= mean_B

        for i in range(len(img_arr_copy)):
            for j in range(len(img_arr_copy[i])):
                red = img_arr_copy[i][j][0] - mean_R
                green = img_arr_copy[i][j][1] - mean_G
                blue = img_arr_copy[i][j][2] - mean_B
                img_arr_copy[i][j][0] = 0.299*red + 0.587*green + 0.114*blue - (0.299*mean_R + 0.587*mean_G + 0.114*mean_B)
                img_arr_copy[i][j][1] = -0.169*red - 0.331*green + 0.5*blue
                img_arr_copy[i][j][2] = 0.5*red - 0.419*green - 0.081*blue

        return img_arr_copy

    @staticmethod
    def rgb_to_yuv(img_arr):
        img_arr_copy = img_arr.copy()
        for i in range(len(img_arr_copy)):
            for j in range(len(img_arr_copy[i])):
                red = img_arr_copy[i][j][0]
                green = img_arr_copy[i][j][1]
                blue = img_arr_copy[i][j][2]
                img_arr_copy[i][j][0] = (red + 2 * green + blue) / 4
                img_arr_copy[i][j][1] = red - green
                img_arr_copy[i][j][2] = blue - green
        return img_arr_copy

    @staticmethod
    def run():
        img = Image.open('./assets/Рохлин.jpg').convert('RGB')
        # img = Image.open('./assets/240x160.jpg').convert('RGB')
        # img = Image.open('./assets/poehaly.jpg').convert('RGB')
        img_arr = np.asarray(img)
        # img_yuv_arr = JPEG2000.rgb_to_yuv(img_arr)
        img_yuv_arr = JPEG2000.brightness_shift(img_arr)
        
        new_img = Image.fromarray(np.array(img_yuv_arr, dtype=np.uint8))
        new_img.save('./assets/whaaaat.png')


JPEG2000.run()
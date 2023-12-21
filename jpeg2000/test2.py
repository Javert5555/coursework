from PIL import Image, ImageTk
import numpy as np
from copy import deepcopy
import pywt


class JPEG2000:

    @staticmethod
    # wavelet transform
    # def dwt_inverse_transform():
    #     image = np.array(Image.open('./try/img_dwt_compress_2.jpg').convert('L'))

    #     # Выполнение DWT
    #     coeffs = pywt.dwt2(image, 'haar')

    #     # Обратное преобразование
    #     reconstructed_image = pywt.idwt2(coeffs, 'haar')

    #     # Сохранение изображения
    #     Image.fromarray(np.uint8(reconstructed_image)).save('./try/img_dwt_decompress_2.jpg')

    @staticmethod
    # wavelet transform
    def dwt_transform():
        # image = np.array(Image.open('./try/img_yuv_compress_1.jpg').convert('L'))
        image = np.array(Image.open('./assets/poehaly.jpg').convert('L'))

        # Выполнение DWT
        # содержащий коэффициенты приближения (approximation) и детализации (detail) для каждого уровня разложения изображения на основе вейвлета Хаара
        coeffs = pywt.dwt2(image, 'haar')
        print('coeffs', coeffs)

        # new_img = Image.fromarray(np.array(coeffs, dtype=np.uint8))
        # new_img.save('./try/output_image1111.jpg')

        # Извлечение коэффициентов приближения и детализации
        # cA, (cH, cV, cD) = coeffs
        # print(cA)

        # Обратное преобразование
        # reconstructed_image = pywt.idwt2((cA, (cH, cV, cD)), 'haar')
        ###################################################################reconstructed_image = pywt.idwt2((coeffs), 'haar')
        # print('reconstructed_image', reconstructed_image)

        # Сохранение изображения
        # Image.fromarray(np.uint8(reconstructed_image)).save('./try/img_dwt_compress_2.jpg')
        #########################################################################Image.fromarray(np.uint8(reconstructed_image)).save('./try/test.jpg')

    @staticmethod
    def rgb_to_yuv(img_arr):
        img_arr_copy = img_arr.copy()
        for i in range(len(img_arr_copy)):
            for j in range(len(img_arr_copy[i])):
                red = img_arr_copy[i][j][0]
                green = img_arr_copy[i][j][1]
                blue = img_arr_copy[i][j][2]
                # img_arr_copy[i][j][0] = (red + 2 * green + blue) / 4
                # img_arr_copy[i][j][1] = red - green
                # img_arr_copy[i][j][2] = blue - green
                img_arr_copy[i][j][0] = 0.299*red + 0.587*green + 0.114*blue
                img_arr_copy[i][j][1] = -0.169*red - 0.331*green + 0.5*blue + 128
                img_arr_copy[i][j][2] = 0.5*red - 0.419*green - 0.081*blue + 128
        return img_arr_copy

    @staticmethod
    def yuv_to_rgb(img_arr):
        img_arr_copy = img_arr.copy()
        for i in range(len(img_arr_copy)):
            for j in range(len(img_arr_copy[i])):
                y = img_arr_copy[i][j][0]
                cb = img_arr_copy[i][j][1]
                cr = img_arr_copy[i][j][2]
                # img_arr_copy[i][j][0] = (red + 2 * green + blue) / 4
                # img_arr_copy[i][j][1] = red - green
                # img_arr_copy[i][j][2] = blue - green
                img_arr_copy[i][j][0] = y + 1.402 * (cr - 128)
                img_arr_copy[i][j][1] = y - 0.3441 * (cb - 128) - 0.7141 * (cr - 128)
                img_arr_copy[i][j][2] = y + 1.772 * (cb - 128)
        return img_arr_copy
    
    @staticmethod
    def decompress(img_arr):
        img_rgb_arr = JPEG2000.yuv_to_rgb(img_arr)

        new_img = Image.fromarray(np.array(img_rgb_arr, dtype=np.uint8))
        new_img.save('./try/img_rgb_decompress_1.jpg')

        return img_rgb_arr

    @staticmethod
    def compress(img_arr):
        img_yuv_arr = JPEG2000.rgb_to_yuv(img_arr)
        
        new_img = Image.fromarray(np.array(img_yuv_arr, dtype=np.uint8))
        new_img.save('./try/img_yuv_compress_1.jpg')

        return img_yuv_arr

    @staticmethod
    def run():
        # img = Image.open('./assets/Рохлин.jpg').convert('RGB')
        # img = Image.open('./assets/240x160.jpg').convert('RGB')
        img = Image.open('./assets/poehaly.jpg').convert('RGB')
        img_arr = np.asarray(img)
        compress_img_arr = JPEG2000.compress(img_arr)
        JPEG2000.dwt_transform()
        decompress_img_arr = JPEG2000.decompress(compress_img_arr)
        # JPEG2000.dwt_inverse_transform()



JPEG2000.run()
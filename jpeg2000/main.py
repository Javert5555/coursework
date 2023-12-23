from PIL import Image, ImageTk
import numpy as np
from copy import deepcopy
import pywt


class JPEG2000:

    @staticmethod
    def quantization(y_array):
        img_arr = y_array

        (h, w) = img_arr.shape
        i_quantization_img = np.empty_like(img_arr)

        max_value = np.amax(img_arr)
        print(max_value)
        min_value = np.amin(img_arr)
        print(min_value)


        step = (max_value - min_value) / 2 ** h
        print(step)

        for i in range(0, w):
            for j in range(0, h):
                i_quantization_img[j][i] = round(img_arr[j][i] / step + 0.5) * step
        coeffs = pywt.dwt2(i_quantization_img, 'haar')
        reconstructed_image_arr = pywt.idwt2((coeffs), 'haar')
        Image.fromarray(np.uint8(reconstructed_image_arr)).save('./try/quant.jpg')
        return i_quantization_img

    @staticmethod
    # wavelet transform
    def dwt_transform(y_arr):
        # Загрузка изображения
        # image_path = './try/yuv.jpg'
        # # image_path = './try/test.jpg'
        # image = Image.open(image_path).convert('L')
        # image_array = np.array(image)
        image_array = y_arr
        print(image_array)

        # Разбиение изображения на тайлы и выполнение wavelet-сжатия
        tiles = []
        # tile_size = round(image_array.shape[0] / 10)  # Размер тайла
        tile_size = 32  # Размер тайла
        # image_array.shape[0]: первый элемент - количество строк, второй элемент - количество столбцов
        for i in range(0, image_array.shape[0], tile_size):
            for j in range(0, image_array.shape[1], tile_size):
                tile = image_array[i:i+tile_size, j:j+tile_size]
                coeffs = pywt.wavedec2(tile, 'haar', level=1)  # Разложение тайла
                # print('coeffs', coeffs)
                # Здесь можно выполнить сжатие коэффициентов

                threshold = 20  # Пороговое значение для сжатия
                coeffs = [pywt.threshold(i, threshold) for i in coeffs]
                # print('coeffs',coeffs)

                # Восстановление тайла
                # reconstructed_tile = pywt.waverec2(coeffs, 'haar')
                reconstructed_tile = pywt.waverec2(coeffs[:-1] + [tuple([None]*len(coeffs[-1]))], 'haar')
                try:
                    tiles.append(reconstructed_tile[:, :])  # Удаление последнего канала
                except:
                    pass
        # print(image_array)

        # Сборка изображения из восстановленных тайлов
        reconstructed_image = np.zeros_like(image_array)
        k = 0
        for i in range(0, image_array.shape[0], tile_size):
            for j in range(0, image_array.shape[1], tile_size):
                print(k, len(tiles))
                reconstructed_image[i:i+tile_size, j:j+tile_size] = tiles[k]
                k += 1
        
        return reconstructed_image


    @staticmethod
    def rgb_to_yuv(img_arr):
        img_arr_copy = img_arr.copy()
        print(len(img_arr_copy[0]))
        for i in range(len(img_arr_copy)):
            for j in range(len(img_arr_copy[i])):
                red = img_arr_copy[i][j][0]
                green = img_arr_copy[i][j][1]
                blue = img_arr_copy[i][j][2]
                img_arr_copy[i][j][0] = 0.299*red + 0.587*green + 0.114*blue
                img_arr_copy[i][j][1] = -0.169*red - 0.331*green + 0.5*blue + 128
                img_arr_copy[i][j][2] = 0.5*red - 0.419*green - 0.081*blue + 128

        # coeffs = pywt.dwt2(img_arr_copy[:,:,0], 'haar')
        # reconstructed_image_arr = pywt.idwt2((coeffs), 'haar')
        # Image.fromarray(np.uint8(reconstructed_image_arr)).save('./try/yuv.jpg')

        return img_arr_copy

    @staticmethod
    def yuv_to_rgb(img_arr):
        img_arr_copy = img_arr.copy()
        for i in range(len(img_arr_copy)):
            for j in range(len(img_arr_copy[i])):
                y = img_arr_copy[i][j][0]
                cb = img_arr_copy[i][j][1]
                cr = img_arr_copy[i][j][2]
                img_arr_copy[i][j][0] = y + 1.402 * (cr - 128)
                img_arr_copy[i][j][1] = y - 0.3441 * (cb - 128) - 0.7141 * (cr - 128)
                img_arr_copy[i][j][2] = y + 1.772 * (cb - 128)
        Image.fromarray(np.uint8(img_arr_copy)).save('./try/compress.jpg')

        return img_arr_copy

    @staticmethod
    def compress(img_arr):
        img_yuv_arr = JPEG2000.rgb_to_yuv(img_arr)
        img_dwt_arr = JPEG2000.dwt_transform(img_yuv_arr[:,:,0])
        quantization_arr = JPEG2000.quantization(img_dwt_arr)
        new_yuv_arr = np.copy(img_yuv_arr)

        for i in range(len(new_yuv_arr)):
            for j in range(len(new_yuv_arr[i])):
                new_yuv_arr[i][j][0] = quantization_arr[i][j]
        JPEG2000.yuv_to_rgb(new_yuv_arr)

        return img_yuv_arr

    @staticmethod
    def run():
        # img = Image.open('./assets/Рохлин.jpg').convert('RGB')
        # img = Image.open('./assets/240x160.jpg').convert('RGB')
        img = Image.open('./assets/700x1000.jpg').convert('RGB')
        img_arr = np.asarray(img)
        compress_img_arr = JPEG2000.compress(img_arr)
        # JPEG2000.dwt_transform()
        # decompress_img_arr = JPEG2000.decompress(compress_img_arr)
        # JPEG2000.dwt_inverse_transform()



JPEG2000.run()
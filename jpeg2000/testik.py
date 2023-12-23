# from PIL import Image

# image_file = "./assets/poehaly1.jpg"
# image = Image.open(image_file)

# compressed_image_file = "./assets/comppoehaly1.jpg"
# image.save(compressed_image_file, quality=50)  # Adjust the quality value as needed

import numpy as np
import pywt

# def dwt(image):
#     # Применяем двумерное дискретное вейвлет-преобразование
#     coeffs = pywt.dwt2(image, 'haar')
#     LL, (LH, HL, HH) = coeffs
    
#     # Объединяем коэффициенты в один массив
#     coeffs_arr = np.concatenate((LL, LH, HL, HH), axis=None)
    
#     return coeffs_arr

# def idwt(coeffs_arr, shape):
#     # Разделяем коэффициенты на четыре массива
#     print(np.split(coeffs_arr, 4))
#     LL, LH_HL_HH = np.split(coeffs_arr, 4)
#     LH, HL, HH = np.split(LH_HL_HH, 3)
    
#     # Применяем обратное двумерное дискретное вейвлет-преобразование
#     coeffs = (LL.reshape(shape), (LH.reshape(shape), HL.reshape(shape), HH.reshape(shape)))
#     reconstructed_image = pywt.idwt2(coeffs, 'haar')
    
#     return reconstructed_image

# # Пример использования
# image = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
# coeffs_arr = dwt(image)
# reconstructed_image = idwt(coeffs_arr, image.shape)


import pywt
import numpy as np
import cv2

# # загрузка изображения
# img = cv2.imread('./assets/esv0XJxDf2E.jpg', 0)

# # применение двумерного дискретного вейвлет-преобразования
# coeffs = pywt.dwt2(img, 'haar')

# # разделение коэффициентов на четные и нечетные
# LL, (LH, HL, HH) = coeffs

# # уменьшение размерности LL до 1/4 от исходного
# LL = cv2.resize(LL, (int(LL.shape[1]/2), int(LL.shape[0]/2)))

# # приведение размеров остальных коэффициентов к размеру LL
# LH = cv2.resize(LH, (LL.shape[1], LL.shape[0]))
# HL = cv2.resize(HL, (LL.shape[1], LL.shape[0]))
# HH = cv2.resize(HH, (LL.shape[1], LL.shape[0]))

# # обратное преобразование
# coeffs = LL, (LH, HL, HH)
# img_dwt = pywt.idwt2(coeffs, 'haar')

# # сохранение сжатого изображения
# cv2.imwrite('compressed_image.jpg', img_dwt)



# def wavelet_compress(image, threshold):
#     # Преобразование Хаара
#     coeffs = pywt.dwt2(image, 'haar')
#     cA, (cH, cV, cD) = coeffs
#     # Применение порога
#     cA = pywt.threshold(cA, threshold*max(cA))
#     cH = pywt.threshold(cH, threshold*max(cH))
#     cV = pywt.threshold(cV, threshold*max(cV))
#     cD = pywt.threshold(cD, threshold*max(cD))
#     # Обратное преобразование Хаара
#     compressed_image = pywt.idwt2((cA, (cH, cV, cD)), 'haar')
#     return compressed_image

# import numpy as np

# # Пример изображения
# image = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# # Сжатие изображения с пороговым значением 30
# compressed_image = wavelet_compress(image, 30)

# print("Оригинальное изображение:")
# print(image)

# print("Сжатое изображение:")
# print(compressed_image)



# import numpy as np
# from PIL import Image

# # Загрузка изображения
# image_path = './assets/esv0XJxDf2E.jpg'
# image = Image.open(image_path)

# # Преобразование изображения в массив пикселей
# image_array = np.array(image)

# # Задание степени квантования
# quantization_step = 8

# # Выполнение квантования
# quantized_image_array = np.round(image_array / (2 ** quantization_step)).astype(np.uint8)

# # Преобразование массива обратно в изображение
# quantized_image = Image.fromarray(quantized_image_array)

# # Сохранение квантованного изображения
# quantized_image.save('quantized_image.jpg')


# import cv2
# import numpy as np

# # загрузка изображения
# img = cv2.imread('./assets/esv0XJxDf2E.jpg', cv2.IMREAD_GRAYSCALE)

# # определение матрицы квантования
# quantization_matrix = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
#                                 [12, 12, 14, 19, 26, 58, 60, 55],
#                                 [14, 13, 16, 24, 40, 57, 69, 56],
#                                 [14, 17, 22, 29, 51, 87, 80, 62],
#                                 [18, 22, 37, 56, 68,109,103, 77],
#                                 [24, 35, 55, 64, 81,104,113, 92],
#                                 [49, 64, 78, 87,103,121,120,101],
#                                 [72, 92, 95, 98,112,100,103, 99]])

# # квантование изображения
# img_quantized = np.zeros_like(img)
# for i in range(0,img.shape[0],8):
#     for j in range(0,img.shape[1],8):
#         img_quantized[i:i+8,j:j+8] = np.round(img[i:i+8,j:j+8]/quantization_matrix)*quantization_matrix

# # сохранение сжатого изображения
# cv2.imwrite('compressed_image.jpg', img_quantized)



import pywt
import numpy as np
from PIL import Image

# Загрузка изображения
image_path = './assets/esv0XJxDf2E.jpg'
# image_path = './try/test.jpg'
image = Image.open(image_path).convert('RGB')
image_array = np.array(image)

# Разбиение изображения на тайлы и выполнение wavelet-сжатия
tiles = []
# tile_size = round(image_array.shape[0] / 10)  # Размер тайла
tile_size = 32  # Размер тайла
# image_array.shape[0]: первый элемент - количество строк, второй элемент - количество столбцов
for i in range(0, image_array.shape[0], tile_size):
    for j in range(0, image_array.shape[1], tile_size):
        tile = image_array[i:i+tile_size, j:j+tile_size]
        coeffs = pywt.wavedec2(tile, 'haar', level=1)  # Разложение тайла
        print('coeffs', coeffs)
        # Здесь можно выполнить сжатие коэффициентов

        threshold = 20  # Пороговое значение для сжатия
        coeffs = [pywt.threshold(i, threshold) for i in coeffs]
        print('coeffs',coeffs)

        # Восстановление тайла
        # reconstructed_tile = pywt.waverec2(coeffs, 'haar')
        reconstructed_tile = pywt.waverec2(coeffs[:-1] + [tuple([None]*len(coeffs[-1]))], 'haar')
        try:
            tiles.append(reconstructed_tile[:, :, :3])  # Удаление последнего канала
        except:
            pass
print(image_array)

# Сборка изображения из восстановленных тайлов
reconstructed_image = np.zeros_like(image_array)
k = 0
for i in range(0, image_array.shape[0], tile_size):
    for j in range(0, image_array.shape[1], tile_size):
        print(k, len(tiles))
        reconstructed_image[i:i+tile_size, j:j+tile_size] = tiles[k]
        k += 1

print(tile_size)

# Сохранение реконструированного изображения
reconstructed_image = Image.fromarray(reconstructed_image)
reconstructed_image.save('reconstructed_image.jpg')
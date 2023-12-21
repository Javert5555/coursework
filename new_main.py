from copy import deepcopy
from numpy.polynomial import Polynomial

import tkinter as tk
# from tkinter import ttk
from tkinter import messagebox
import tkinter.scrolledtext as scrolledtext


gf_table = [1, 2, 4, 8, 16, 32, 64, 128, 29, 58, 116, 232, 205, 135, 19, 38, 76, 152, 45, 90, 180, 117, 234,
 201, 143, 3, 6, 12, 24, 48, 96, 192, 157, 39, 78, 156, 37, 74, 148, 53, 106, 212, 181, 119, 238,
 193, 159, 35, 70, 140, 5, 10, 20, 40, 80, 160, 93, 186, 105, 210, 185, 111, 222, 161, 95, 190, 97,
 194, 153, 47, 94, 188, 101, 202, 137, 15, 30, 60, 120, 240, 253, 231, 211, 187, 107, 214, 177, 127,
 254, 225, 223, 163, 91, 182, 113, 226, 217, 175, 67, 134, 17, 34, 68, 136, 13, 26, 52, 104, 208, 189,
 103, 206, 129, 31, 62, 124, 248, 237, 199, 147, 59, 118, 236, 197, 151, 51, 102, 204, 133, 23, 46,
 92, 184, 109, 218, 169, 79, 158, 33, 66, 132, 21, 42, 84, 168, 77, 154, 41, 82, 164, 85, 170, 73,
 146, 57, 114, 228, 213, 183, 115, 230, 209, 191, 99, 198, 145, 63, 126, 252, 229, 215, 179, 123, 246,
 241, 255, 227, 219, 171, 75, 150, 49, 98, 196, 149, 55, 110, 220, 165, 87, 174, 65, 130, 25, 50, 100,
 200, 141, 7, 14, 28, 56, 112, 224, 221, 167, 83, 166, 81, 162, 89, 178, 121, 242, 249, 239, 195, 155,
 43, 86, 172, 69, 138, 9, 18, 36, 72, 144, 61, 122, 244, 245, 247, 243, 251, 235, 203, 139, 11, 22,
 44, 88, 176, 125, 250, 233, 207, 131, 27, 54, 108, 216, 173, 71, 142, 1]

def get_mult(num1, num2):
    index1 = gf_table.index(num1)
    index2 = gf_table.index(num2)
    final_index = (index1 + index2) % (len(gf_table) - 1)
    return gf_table[final_index]

# res = 2
# nums = [2,4,8,16]
# for i in range(1, len(nums)):
#     res = get_mult(res, nums[i])

def from_int_to_bin(num, need_length):
    bin_num = list(reversed([int(i) for i in list(bin(num).split('0b')[1])]))
    while len(bin_num) != need_length:
        bin_num.append(0)
    return bin_num

def from_bin_to_int(bin_num):
    int_num = int('0b' + ''.join([str(i) for i in list(reversed(bin_num))]), 2)
    return int_num


def get_pols_div(dividend, divisor, m):
    dividend_values = list(reversed([0] * m + dividend))
    divisor_indeces = list(reversed([gf_table.index(i) for i in divisor]))
    # print('dividend_values', dividend_values)
    # print('divisor_indeces', divisor_indeces)
    # проходимся по длине начального сообщения, так как дальше будет остаток от деления
    for i in range(len(dividend)):
        temp_divisor_indeces = deepcopy(divisor_indeces)
        if dividend_values[i] != 0:
            degree_difference = gf_table.index(dividend_values[i]) - temp_divisor_indeces[0]
            # print(degree_difference)
            temp_divisor_indeces = [(i + degree_difference) % (len(gf_table) - 1) for i in temp_divisor_indeces]
            # print('temp_divisor_indeces', temp_divisor_indeces)

            
            temp_index = 0
            for j in range(i, i + len(divisor_indeces)):
                first = 0
                if(dividend_values[j] != 0):
                    first = gf_table[gf_table.index(dividend_values[j])]
                dividend_values[j] = first ^ gf_table[temp_divisor_indeces[temp_index]]
                # if(dividend_values[j] != 0):
                    # dividend_values[j] = gf_table.index(dividend_values[j])
                temp_index = temp_index + 1
            # print('dividend', [i for i in dividend_values])

            # если индекс последнего ненулевого символа (степень x при данном коэффициенте)
            # остатка от деления меньше длины делителя (максимальной степени x в полиноме делителе)
            # то выходим из цикла и возвращаем остаток от деления
            # или если вообще не находим ненулевого символа
            try:
                index_las_symbol = len(dividend_values) - 1 - dividend_values.index(next(filter(lambda x: x != 0, dividend_values)))
                if (index_las_symbol + 1 < len(divisor_indeces)):
                    break
            except:
                break
    
    # print('dividend_values', dividend_values)

    remainder_div = list(reversed([i for i in dividend_values[-m:]]))

    return remainder_div


def get_pols_mult(pol1, pol2):
    # получаем индексы значений из нашего поля
    pol1_indeces = [gf_table.index(i) for i in pol1]
    # print(pol2)
    pol2_indeces = [gf_table.index(i) for i in pol2]
    
    # получаем массив подмассивов, в каждом подмассиве будут храниться элементы из поля,
    # которые будут ялвяться коэффициентами при некоторых степенях x 
    coefficients_values = [[] for _ in range(len(pol1_indeces) + len(pol2_indeces) - 1)]
    # print('coefficients_values', coefficients_values)
    for i in range(len(pol1_indeces)):
        for j in range(len(pol2_indeces)):
            # coefficients_values[i+j].append((pol1_indeces[i] + pol2_indeces[j]) % (len(gf_table) - 1))
            coefficients_values[i+j].append(gf_table[(pol1_indeces[i] + pol2_indeces[j]) % (len(gf_table) - 1)])
    
    # здесь складываем (xor) наши коэффициенты (по правилам действий в полях галуа)
    coefficients = []
    for coefficient_values in coefficients_values:
        temp_coeff = 0
        for j in range(len(coefficient_values)):
            temp_coeff ^= coefficient_values[j]
        coefficients.append(temp_coeff)

    # в итоге возвращаем массив с финальными коэффициентами при при некоторых степенях x
    return coefficients

def get_gen_pol(m):
    if (m == 0):
        return [1]
    pols = [[gf_table[i], 1] for i in range(1, m + 1)]
    temp_pol = pols[0]
    for i in range(1, m):
        temp_pol = get_pols_mult(temp_pol, pols[i])
    return temp_pol

# def get_pol_with_redundant_symbols(pol, m):
#     return [0] * m + pol

def split_text_into_arrays(text, k):
    # Преобразование текста в 10 систему счисления
    # decimal_representation = [ord(char) for char in text]
    decimal_representation = get_init_text_split(text)
    

    
    # Разбиение на массивы длиной k
    arrays = [decimal_representation[i:i + k] for i in range(0, len(decimal_representation), k)]
    
    # Добавление нулей в конец последнего массива, если его длина меньше k
    if len(arrays[-1]) < k:
        arrays[-1].extend([0] * (k - len(arrays[-1])))

    # print(arrays)
    
    return arrays

def join_arrays_to_string(arrays):
    # print(len(arrays[0])) # 255
    result = ' '.join([' '.join([str(num) for num in subarray]) for subarray in arrays])
    
    return result

def get_init_text_split(init_text):
    print('init_squence_int', init_text)
    binary_sequence = ''.join([''.join([bin(ord(char))[2:].rjust(12, '0')]) for char in init_text])
    print('binary_sequence111', binary_sequence)
    result = [int(binary_sequence[i:i+8].ljust(8, '0'), 2) for i in range(0, len(binary_sequence), 8)]
    print('arrays', result)
    return result

def encode(init_text, k_val):
    # m = 4
    initial_text = init_text
    n = len(gf_table) - 1
    # k = 100
    k = k_val
    m = n - k
        
    gen_pol = get_gen_pol(m)
    # print(gen_pol)
    # initial_text = "DON'T PANIC"
    if (m == 0):
        print(123)
        return {
            'initial_text': initial_text,
            'code_words_sequence': join_arrays_to_string(split_text_into_arrays(initial_text, n)),
            'gen_pol': ''
        }

    new_initial_text = split_text_into_arrays(initial_text, k)
    # print('new_initial_text', new_initial_text)
    new_initial_text_code_words = []
    for initial_code_text in new_initial_text:
        remainder_div = get_pols_div(initial_code_text, gen_pol, m)
        code_word = remainder_div + initial_code_text
        new_initial_text_code_words.append(code_word)

    print('new_initial_text_code_words', new_initial_text_code_words)
    return {
        'initial_text': initial_text,
        'code_words_sequence': join_arrays_to_string(new_initial_text_code_words),
        'gen_pol': Polynomial(gen_pol)
    }

# def get_init_text_split(init_text):
#     print('init_squence_int', init_text)
#     binary_sequence = ''.join([''.join([bin(ord(char))[2:].ljust(12, '0')]) for char in init_text])
#     print('binary_sequence111', binary_sequence)
#     result = [int(binary_sequence[i:i+8].ljust(8, '0'), 2) for i in range(0, len(binary_sequence), 8)]
#     print('arrays', result)
#     return result


def get_init_text(num_arrays, len_to_get_letter, len_to_get_number):
    print(num_arrays)
    # 000001100100000001101111000001101110000000100111000001110100000000100000000001110000000001100001000001101110000001101001000001100011000000001010
    binary_sequence = ''.join([''.join([bin(num)[2:].rjust(len_to_get_number, '0') for num in num_array]) for num_array in num_arrays])
    # binary_sequence = ''.join([[''.join(reversed(bin(num)[2:][::-1].zfill(len_to_get_letter))) for num in num_array] for num_array in num_arrays])
    print('binary_sequence', binary_sequence)

    binary_sequences = [binary_sequence[i : i + len_to_get_letter] for i in range(0, len(binary_sequence), len_to_get_letter)]
    print('binary_sequences', binary_sequences)
    text = [chr(int('0b' + ''.join(remove_consecutive_zeros(list(binary_sequence))), 2)) for binary_sequence in binary_sequences]
    print('text', text)
    # result = [int(binary_sequence[i:i+len_to_get_number].ljust(len_to_get_number, '0'), 2) for i in range(0, len(binary_sequence), len_to_get_number)]
    # print('arrays', result)
    # return result

def remove_consecutive_zeros(arr):
    num_array = deepcopy(arr)
    i = len(num_array) - 1
    while i >= 0:
        if num_array[i] == 0:
            del num_array[i]
        else:
            break
        i -= 1
    return num_array

def from_num_sequence_to_arrays(num_sequence, n, m):
    # делим на "кодовые слова" длиной 255
    num_array = [int(num) for num in num_sequence.split()]
    num_arrays = [num_array[i + m : i + n] for i in range(0, len(num_array), n)]
    # print(num_arrays)
    return num_arrays

def decode(text, k):
    n = len(gf_table) - 1
    m = n - k
    len_to_get_letter = 12
    len_to_get_number = 8
    num_arrays = from_num_sequence_to_arrays(text, n, m)
    # удаляем из массивов незначащие нули
    num_arrays_without_useless_zeros = [remove_consecutive_zeros(num_array) for num_array in num_arrays]
    print(num_arrays_without_useless_zeros)
    # print('num_arrays_without_useless_zeros', num_arrays_without_useless_zeros)
    init_text = get_init_text(num_arrays_without_useless_zeros, len_to_get_letter, len_to_get_number)

# [200, 13, 224, 220, 9, 192, 232, 8, 0, 224, 12, 32, 220, 13, 32, 198, 10]
# 000001100100000001101111000001101110000000100111000001110100000000100000000001110000000001100001000001101110000001101001000001100011000000001010
text = '224 3 18 6 64 111 6 224 39 7 64 32 7 0 97 6 224 105 6 48 10 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'
decode(text, 252)

# при m=4 g=[116, 231, 216, 30, 1]

class SecondWindow(tk.Toplevel):
    def __init__(self, master=None, result=None):
        super().__init__(master)
        self.title('Коды рида соломона')
        self.minsize(1320, 660)

        self.f_left = tk.Frame(self)
        self.f_left.pack(side='left')
        self.f_left.pack(padx=(10, 10))

        self.f_right = tk.Frame(self)
        self.f_right.pack(side='left')
        self.f_right.pack(padx=(10, 10))

        self.label1 = tk.Label(self.f_left, text=result['title1'])
        self.label1.pack(side='top')
        self.label1.pack(pady=10)

        self.text_code_words = scrolledtext.ScrolledText(self.f_left, wrap=tk.WORD, height=10)
        self.text_code_words.pack(side='top')
        self.text_code_words.insert(tk.END, result['initial_text'])
        
        self.label2 = tk.Label(self.f_left, text=result['title2'])
        self.label2.pack(side='top')
        self.label2.pack(pady=10)

        self.text_code_words_with_mistake = scrolledtext.ScrolledText(self.f_left, wrap=tk.WORD, height=10)
        self.text_code_words_with_mistake.pack(side='top')
        self.text_code_words_with_mistake.insert(tk.END, result['code_words_sequence'])
        
        self.label3 = tk.Label(self.f_left, text=result['title3'])
        self.label3.pack(side='top')
        self.label3.pack(pady=10)

        self.text_code_words_without_mistake = scrolledtext.ScrolledText(self.f_left, wrap=tk.WORD, height=10)
        self.text_code_words_without_mistake.pack(side='top')
        self.text_code_words_without_mistake.insert(tk.END, result['gen_pol'])
        
     
class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x540')
        self.minsize(600, 540)
        self.title('Коды рида соломона, окно ввода данных')

        self.f_top = tk.Frame(self)
        self.f_top.pack()

        self.f_bottom = tk.Frame(self)
        self.f_bottom.pack(side='left')
        self.f_bottom.pack(padx=(20, 0))

        self.f_btn = tk.Frame(self)
        self.f_btn.pack(side='right')

        self.label_initial_text = tk.Label(self.f_top, text='Введите текст, который надо закодировать: ')
        self.label_initial_text.pack(side='top')
        self.label_initial_text.pack(pady=(10, 0))

        self.initial_text = scrolledtext.ScrolledText(self.f_top, wrap=tk.WORD, height=20, width=55)
        self.initial_text.pack(side='top')
        self.initial_text.pack(pady=(10, 0))

        self.label_k = tk.Label(self.f_top, text='Введите k, длину информационных слов')
        self.label_k.pack(side='top')
        self.label_k.pack(pady=(10, 0))

        self.k = scrolledtext.ScrolledText(self.f_top, wrap=tk.WORD, height=2, width=5)
        self.k.pack(side='top')
        self.k.pack(pady=(10, 0))

        self.len_params = tk.Label(self.f_top, text=f'Длина кодовых слов: {len(gf_table) - 1}.')
        self.len_params.pack(side='top')
        self.len_params.pack(pady=(10, 0))


        button_1 = tk.Button(self.f_btn, text='Получить результат', font='Times 12', command=self.get_all_inputs_and_get_solution)
        button_1.pack(side='bottom')
        button_1.pack(padx=(0, 20))

    def open_window(self, result):
        self.new_window = SecondWindow(self, result=result)
    
    def get_all_inputs_and_get_solution(self):
        try:
            self.initial_text_var = self.initial_text.get("1.0","end")
            if (self.initial_text_var.strip() == ''):
                messagebox.showwarning(title="Предупреждение", message="Введите текст, который надо закодировать")
                return
            self.k_var = self.k.get("1.0","end")
            if (self.k_var.strip() not in [str(i) for i in range(256)]):
                messagebox.showwarning(title="Предупреждение", message="Введите k / Неверно укеазано k")
                return
            if (int(self.k_var.strip()) > len(gf_table) - 1):
                messagebox.showwarning(title="Предупреждение", message="k > n")
                return
        except:
            messagebox.showwarning(title="Предупреждение", message="Что-то пошло не так")
            return

        self.result = encode(self.initial_text_var, int(self.k_var.strip()))

        self.open_window({
            'title1': 'Начальный текст:',
            'initial_text': self.result['initial_text'],
            'title2': 'Последовательность кодовых слов:',
            'code_words_sequence': self.result['code_words_sequence'],
            'title3': 'Порождающий полином:',
            'gen_pol': self.result['gen_pol']
        })

if __name__ == "__main__":
    main = Main()
    main.mainloop()
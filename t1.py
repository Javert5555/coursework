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

# def get_pols_div(dividend, divisor, m):
#     dividend_values = list(reversed([0] * m + dividend))
#     dividend_indeces = list(reversed([0] * m + [gf_table.index(i) for i in dividend]))
#     divisor_indeces = list(reversed([gf_table.index(i) for i in divisor]))
#     print('dividend_indeces', dividend_indeces)
#     print('divisor_indeces', divisor_indeces)
#     # проходимся по длине начального сообщения, так как дальше будет остаток от деления
#     for i in range(len(dividend)):
#         temp_divisor_indeces = deepcopy(divisor_indeces)
#         if (dividend_indeces[i] > temp_divisor_indeces[0]):
#             degree_difference = dividend_indeces[i] - temp_divisor_indeces[0]
#             print(degree_difference)
#             temp_divisor_indeces = [(i + degree_difference) % (len(gf_table) - 1) for i in temp_divisor_indeces]
#             print('temp_divisor_indeces', temp_divisor_indeces)
#         else:
#             degree_difference = temp_divisor_indeces[0] - dividend_indeces[i]
#             print(degree_difference)
#             temp_divisor_indeces = [(i - degree_difference) % (len(gf_table) - 1) for i in temp_divisor_indeces]
#             print('temp_divisor_indeces', temp_divisor_indeces)
        
#         temp_index = 0
#         for j in range(i, i + len(divisor_indeces) - 1):
#             dividend_indeces[j] = gf_table[dividend_indeces[j]] ^ gf_table[temp_divisor_indeces[temp_index]]
#             if(dividend_indeces[j] != 0):
#                 dividend_indeces[j] = gf_table.index(dividend_indeces[j])
#             temp_index += 1
#         print('dividend', [gf_table[i] for i in dividend_indeces])
    
#     print(dividend_indeces)

#     result_dividend = [hex(gf_table[i]) for i in dividend_indeces[-m:]]

#     print(result_dividend)

def get_pols_div(dividend, divisor, m):
    dividend_values = list(reversed([0] * m + dividend))
    # dividend_indeces = list(reversed([0] * m + [gf_table.index(i) for i in dividend]))
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
    # Преобразование десятичных чисел в 16 систему счисления
    hex_arrays = [[hex(num)[2:].zfill(2) for num in subarray] for subarray in arrays]
    # print(hex_arrays)
    
    # Объединение массивов в строку
    result = ' '.join([' '.join(subarray) for subarray in hex_arrays])
    
    return result

def get_init_text_split(init_squence_int):
    binary_sequence = ''.join([''.join(reversed(bin(ord(num))[2:][::-1].zfill(12))) for num in init_squence_int])
    print(binary_sequence)
    result = [int(binary_sequence[i:i+8].ljust(8, '0'), 2) for i in range(0, len(binary_sequence), 8)]
    return result

def get_solution(init_text, k_val):
    # m = 4
    initial_text = init_text
    n = len(gf_table) - 1
    # k = 100
    k = k_val
    m = n - k
        
    gen_pol = get_gen_pol(m)
    # print(gen_pol)
    # print('gen_pol', Polynomial(gen_pol))
    # initial_text = "DON'T PANIC"
    # initial_text = "DON'T PANIC"
    # initial_text = "dBADFSASDASDFVHBAa"*10
    # initial_text = "dBADFSVHBAa"*10
    if (m == 0):
        print(123)
        return {
            'initial_text': initial_text,
            'code_words_sequence': join_arrays_to_string(split_text_into_arrays(initial_text, n)),
            'gen_pol': ''
        }

    new_initial_text = split_text_into_arrays(initial_text, k)
    print('new_initial_text', new_initial_text)
    new_initial_text_code_words = []
    for initial_code_text in new_initial_text:

        # print(new_initial_text)
        # initial_text = "DON'T PANICajsbdfoinjsaipdfo"
        # initial_code_text = [int(hex(ord(letter)), 16) for letter in initial_text]
        # print('initial_code_text', initial_code_text)

        # initial_code_text_indices = [gf_table.index(i) for i in initial_code_text]
        # print('initial_code_text_indices', initial_code_text_indices)

        # ага, ну да несистематическое кодовое слово, расскажешь
        # non_sys_code_text = get_pols_mult(gen_pol, initial_code_text)
        # print('non_sys_code_text', non_sys_code_text)
        # 
        # print('-----------')
        # initial_code_text_with_redundant_symbols = get_pol_with_redundant_symbols(initial_code_text, m)
        # print('initial_code_text_with_redundant_symbols', initial_code_text_with_redundant_symbols)

        remainder_div = get_pols_div(initial_code_text, gen_pol, m)
        # print('remainder_div', remainder_div)

        code_word = remainder_div + initial_code_text
        new_initial_text_code_words.append(code_word)
        # print('code_word', [hex(i).split('0x')[1] for i in code_word])
        # print(get_pols_div([67, 86, 136, 68], [6, 11, 7], 2))


        # p1 = get_pols_mult([2, 1], [4, 1])
        # p2 = get_pols_mult(p1, [8, 1])
        # p3 = get_pols_mult(p2, [16, 1])
        # print(p3)
        # print(len(gf_table))
    print('new_initial_text_code_words', new_initial_text_code_words)
    return {
        'initial_text': initial_text,
        'code_words_sequence': join_arrays_to_string(new_initial_text_code_words),
        'gen_pol': Polynomial(gen_pol)
    }

# get_solution()


# print(gf_table.index(30))
# one = from_int_to_bin(1, 8)
# print(one)
# one = from_bin_to_int(one)
# print(one)




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

        self.result = get_solution(self.initial_text_var, int(self.k_var.strip()))

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
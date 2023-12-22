# from HammingCode import HammingCode
# from ConvolutionalCode import ConvolutionalCode
# from InterleaverObj import InterleaverObj
import tkinter as tk
# from tkinter import ttk
from tkinter import messagebox
import tkinter.scrolledtext as scrolledtext

from rs.RS import RS

class SecondWindow(tk.Toplevel):
    def __init__(self, master=None, result=None):
        super().__init__(master)
        self.title('Коды рида соломона')
        self.minsize(720, 660)

        self.f_left = tk.Frame(self)
        self.f_left.pack(side='top')
        self.f_left.pack(padx=(10, 10))

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

class ThirdWindow(tk.Toplevel):
    def __init__(self, master=None, result=None):
        super().__init__(master)
        self.title('Коды рида соломона')
        self.minsize(720, 260)

        self.f_left = tk.Frame(self)
        self.f_left.pack(side='top')
        self.f_left.pack(padx=(10, 10))

        self.f_right = tk.Frame(self)
        self.f_right.pack(side='left')
        self.f_right.pack(padx=(10, 10))

        self.label1 = tk.Label(self.f_left, text=result['title1'])
        self.label1.pack(side='top')
        self.label1.pack(pady=10)

        self.text_code_words = scrolledtext.ScrolledText(self.f_left, wrap=tk.WORD, height=10)
        self.text_code_words.pack(side='top')
        self.text_code_words.insert(tk.END, result['init_text'])
        
     
class MainRS(tk.Tk):
    def __init__(self, master):
        super().__init__()
        self.geometry('1280x480')
        self.minsize(1280, 480)
        self.title('Коды рида соломона, окно ввода данных')

        self.f_left = tk.Frame(self)
        self.f_left.pack(side='left')
        self.f_left.pack(padx=(40, 0))

        self.f_right = tk.Frame(self)
        self.f_right.pack(side='right')
        self.f_right.pack()

        self.f_bottom = tk.Frame(self)
        self.f_bottom.pack(side='bottom')
        self.f_bottom.pack(padx=(20, 0))
        self.f_bottom.pack(pady=(10, 10))

        self.f_btn_1 = tk.Frame(self.f_left)
        self.f_btn_1.pack(side='bottom')
        self.f_btn_1.pack(pady=(20, 20))

        self.f_btn_2 = tk.Frame(self.f_right)
        self.f_btn_2.pack(side='bottom')
        self.f_btn_2.pack(pady=(20, 20))

        self.label_initial_text_to_code = tk.Label(self.f_left, text='Введите текст, который надо закодировать: ')
        self.label_initial_text_to_code.pack(side='top')
        self.label_initial_text_to_code.pack(pady=(10, 0))

        self.initial_text_to_code = scrolledtext.ScrolledText(self.f_left, wrap=tk.WORD, height=20, width=55)
        self.initial_text_to_code.pack(side='top')
        self.initial_text_to_code.pack(pady=(10, 0))
        # -----------------------------------------------------------------------------------------------
        self.label_initial_text_to_decode = tk.Label(self.f_right, text='Введите текст, который надо декодировать: ')
        self.label_initial_text_to_decode.pack(side='top')
        self.label_initial_text_to_decode.pack(pady=(10, 0))

        self.initial_text_to_decode = scrolledtext.ScrolledText(self.f_right, wrap=tk.WORD, height=20, width=55)
        self.initial_text_to_decode.pack(side='top')
        self.initial_text_to_decode.pack(pady=(10, 0))

        self.label_k = tk.Label(self.f_bottom, text='Введите k, длину информационных слов')
        self.label_k.pack(side='top')
        self.label_k.pack(pady=(10, 0))

        self.k = scrolledtext.ScrolledText(self.f_bottom, wrap=tk.WORD, height=2, width=5)
        self.k.pack(side='top')
        self.k.pack(pady=(10, 0))

        self.len_params = tk.Label(self.f_bottom, text=f'Длина кодовых слов: {len(RS.get_gf_table()) - 1}.')
        self.len_params.pack(side='top')
        self.len_params.pack(pady=(10, 0))


        button_1 = tk.Button(self.f_btn_1, text='Закодировать', font='Times 12', command=self.get_code_text)
        button_1.pack(side='bottom')
        button_1.pack(padx=(0, 20))

        button_2 = tk.Button(self.f_btn_2, text='Декодировать', font='Times 12', command=self.get_decode_text)
        button_2.pack(side='bottom')
        button_2.pack(padx=(0, 20))

    def open_second_window(self, result):
        self.new_window = SecondWindow(self, result=result)

    def open_third_window(self, result):
        self.new_window = ThirdWindow(self, result=result)
    
    def get_code_text(self):
        try:
            self.initial_code_text_var = self.initial_text_to_code.get("1.0","end")
            if (self.initial_code_text_var.strip() == ''):
                messagebox.showwarning(title="Предупреждение", message="Введите текст, который надо закодировать")
                return
            self.k_var = self.k.get("1.0","end")
            if (self.k_var.strip() not in [str(i) for i in range(256)]):
                messagebox.showwarning(title="Предупреждение", message="Введите k / Неверно укеазано k")
                return
            if (int(self.k_var.strip()) > len(RS.get_gf_table()) - 1):
                messagebox.showwarning(title="Предупреждение", message="k > n")
                return
        except:
            messagebox.showwarning(title="Предупреждение", message="Что-то пошло не так")
            return

        self.result = RS.encode(self.initial_code_text_var, int(self.k_var.strip()))

        self.open_second_window({
            'title1': 'Начальный текст:',
            'initial_text': self.result['initial_text'],
            'title2': 'Последовательность кодовых слов:',
            'code_words_sequence': self.result['code_words_sequence'],
            'title3': 'Порождающий полином:',
            'gen_pol': self.result['gen_pol']
        })
    
    def get_decode_text(self):
        try:
            self.initial_text_to_decode_var = self.initial_text_to_decode.get("1.0","end")
            if (self.initial_text_to_decode_var.strip() == ''):
                messagebox.showwarning(title="Предупреждение", message="Введите текст, который надо закодировать")
                return
            self.k_var = self.k.get("1.0","end")
            if (self.k_var.strip() not in [str(i) for i in range(256)]):
                messagebox.showwarning(title="Предупреждение", message="Введите k / Неверно укеазано k")
                return
            if (int(self.k_var.strip()) > len(RS.get_gf_table()) - 1):
                messagebox.showwarning(title="Предупреждение", message="k > n")
                return
        except:
            messagebox.showwarning(title="Предупреждение", message="Что-то пошло не так")
            return

        self.result = RS.decode(self.initial_text_to_decode_var, int(self.k_var.strip()))

        if (self.result == 'cant convet to numbers'):
            messagebox.showwarning(title="Ошибка", message="Введены некорректные данные на декодирование")
            return

        self.open_third_window({
            'title1': 'Декодированный текст:',
            'init_text': self.result['init_text'],
        })

class App:
    def __init__(self, master):
        self.master = master
        self.button1 = tk.Button(self.master, text="Код Рида — Соломона", command=self.open_window1)
        self.button1.pack(padx=(10, 10))
        self.button1.pack(pady=(10, 10))

        self.button2 = tk.Button(self.master, text="Сжатие JPEG2000", command=self.open_window2)
        self.button2.pack()

    def open_window1(self):
        # subwindow1 = tk.Toplevel(self.master)
        # subwindow1.title("SubWindow 1")
        app = MainRS(self)

    def open_window2(self):
        window2 = tk.Toplevel(self.master)
        # Добавьте код для создания окна 2

if __name__ == "__main__":
    # main = MainRS()
    # main.mainloop()
    root = tk.Tk()
    app = App(root)
    root.mainloop()
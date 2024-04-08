import tkinter as tk
from tkinter import filedialog

def switch_language(text):
    switched_text = ''
    language_map = {
        'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н',
        'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х', ']': 'ъ',
        'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р',
        'j': 'о', 'k': 'л', 'l': 'д', ';': 'ж', "'": 'э',
        'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т',
        'm': 'ь', ',': 'б', '.': 'ю',
        'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't',
        'н':  'y',  'г':  'u',  'ш':  'i',
        'щ':  'o',  'з':  'p',  'х':  '[',  'ъ':  ']',
        'ф':  'a',  'ы':  's',  'в':  'd',
        'а':  'f',  'п':  'g',  'р':  'h',
        'о':  'j',  'л':  'k',  'д':  'l',
        'ж':  ';',  'э':  "'",
        'я':  'z',  'ч':  'x',  'с':  'c',
        'м':  'v',  'и':  'b',  'т':  'n',
        'ь':  'm',  ',':  ',',  '.': '.'
    }
    for char in text:
        if char.lower() in language_map:
            switched_text += language_map[char.lower()].upper() if char.isupper() else language_map[char.lower()]
        else:
            switched_text += char
    return switched_text

def switch_text(event=None):
    input_text = input_entry.get("1.0", tk.END)
    switched_text = switch_language(input_text)
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, switched_text)

def save_text_to_file():
    text_to_save = output_text.get("1.0", tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_to_save)

def load_text_from_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            loaded_text = file.read()
            input_entry.delete("1.0", tk.END)
            input_entry.insert(tk.END, loaded_text)
            switch_text() # Вызываем функцию переключения языка после загрузки текста

root = tk.Tk()
root.geometry("480x400")
root.title("Switch Board")

input_label = tk.Label(root, text="Ведите текст:")
input_label.pack()

input_entry = tk.Text(root, height=5, width=50)
input_entry.pack()

output_label = tk.Label(root, text="Изменённый текст:")
output_label.pack()

output_text = tk.Text(root, height=5, width=50)
output_text.pack()

save_button = tk.Button(root, text="Сохранить файл", command=save_text_to_file)
save_button.pack()

load_button = tk.Button(root, text="Загрузить файл", command=load_text_from_file)
load_button.pack()

def copy_text():
    root.clipboard_clear()
    root.clipboard_append(output_text.get("1.0", tk.END))

def paste_text():
    input_entry.insert(tk.END, root.clipboard_get())

def clear_text():
    input_entry.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

clear_button = tk.Button(root, text="Очистить всё", command=clear_text)
clear_button.pack()


copy_button = tk.Button(root, text="Скопировать текст", command=copy_text)
copy_button.pack()

paste_button = tk.Button(root, text="Вставить текст", command=paste_text)
paste_button.pack()

root.configure(bg="#C9F2FF")  # Нежно-голубой цвет фона

input_label.configure(bg="#C9F2FF")  # Нежно-голубой цвет фона для метки ввода
input_entry.configure(bg="white")  # Белый цвет фона для области ввода

output_label.configure(bg="#C9F2FF")  # Нежно-голубой цвет фона для метки вывода
output_text.configure(bg="white")  # Белый цвет фона для области вывода

clear_button.configure(bg="#FFC0CB")  # Розоватый цвет кнопки очистки текста

save_button.configure(bg="#90EE90") # Зеленоватый цвет кнопки сохранения текста

load_button.configure(bg="#FFDAB9") # Оранжевый цвет кнопки загрузки текста

copy_button.configure(bg="#87CEEB")  # Светло-голубой цвет кнопки копирования текста

paste_button.configure(bg="#87CEEB")  # Светло-голубой цвет кнопки вставки текста


switch_text() # Вызываем функцию переключения языка после загрузки текста из файла

root.bind("<Key>", switch_text)

root.mainloop()


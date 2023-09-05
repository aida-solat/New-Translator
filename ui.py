import tkinter as tk
from translate_script import translate_text
from tkinter import ttk


def main():
    app = tk.Tk()
    app.title('Translation Application')

    main_frame = ttk.Frame(app, padding='10')
    main_frame.grid(row=0, column=0, sticky=tk.W + tk.E + tk.N + tk.S)

    ttk.Label(main_frame, text='Text to translate:').grid(
        row=0, column=0, sticky=tk.W)
    input_text = tk.StringVar()
    ttk.Entry(main_frame, width=40, textvariable=input_text).grid(
        row=0, column=1, sticky=tk.W)

    ttk.Label(main_frame, text='Language code:').grid(
        row=1, column=0, sticky=tk.W)
    input_lang = tk.StringVar()
    ttk.Entry(main_frame, width=5, textvariable=input_lang).grid(
        row=1, column=1, sticky=tk.W)

    ttk.Button(main_frame, text='Translate', command=lambda: translate_button_click(
        input_text.get(), input_lang.get())).grid(row=2, column=1, sticky=tk.E)

    ttk.Label(main_frame, text='Translated text:').grid(
        row=3, column=0, sticky=tk.W)
    translated_text = tk.StringVar()
    ttk.Label(main_frame, textvariable=translated_text).grid(
        row=3, column=1, sticky=tk.W)

    def translate_button_click(text, lang_code):
        translated = translate_text(text, lang_code)
        translated_text.set(translated)

    app.mainloop()


if __name__ == '__main__':
    main()

# Создать программно файл в текстовом формате, записать в него построчно данные, вводиимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка
with open('text_5_1.txt', 'w', encoding='utf-8') as f:
    while True:
        line = input('Введите новую строку - ')
        if not line:
            break
        #f.write(f'{line}\n')
        print(line, file=f)
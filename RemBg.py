import os
import pathlib
from pathlib import Path
from rembg import remove
from PIL import Image

input_path  = input(Path('Введите путь к фото в формате png: '))
output_path = input_path
extension = Path(input_path)

if extension.suffix == '.png':

    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)
    print('Готово!, файл сохранен по пути: ' + output_path)

else:
    print('Упс... ошибОчка')


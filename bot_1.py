from PIL import Image
import pytesseract

# Укажите путь к файлу tesseract, если вы работаете на Windows
pytesseract.pytesseract.tesseract_cmd = r'{{sensitive_data}}'

# Откройте изображение
image_path = '{{sensitive_data}}'  # Укажите путь к вашему изображению
image = Image.open(image_path)

# Используйте pytesseract для извлечения текста из изображения
text = pytesseract.image_to_string(image, lang='rus')  # Укажите нужный язык, например, 'rus' для русского

# Выведите распознанный текст
print(text)
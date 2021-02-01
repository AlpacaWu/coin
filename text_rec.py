import pytesseract
from PIL import Image
img = Image.open('chicken.jpg')
text = pytesseract.image_to_string(img, lang='chi_tra+eng')
print(text)
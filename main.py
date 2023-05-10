import cv2 as cv
import numpy as np

# img = cv.imread("images/test.png")
# print (img.shape)


# Укажите путь к изображению
image_path = "images/test.png"

# Загрузите изображение с помощью функции imread()
image = cv.imread(image_path)

# Проверьте, удалось ли загрузить изображение
if image is not None:
    # Показать изображение с помощью функции imshow()
    cv.imshow("Изображение", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("Не удалось загрузить изображение")
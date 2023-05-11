import cv2 as cv
import numpy as np

# определяем камеру с помощью opencv
vid = cv.VideoCapture(0)
  
while(True):
    # берем видео с камеры
    ret, frame = vid.read()

    # отображаем
    cv.imshow('frame', frame)
    
    # проверяем, была ли нажата клавиша 'q'
    if cv.waitKey(1) & 0xFF == ord('q') or cv.waitKey(1) & 0xFF == 27:
        break

    # проверяем, закрыта ли окно пользователем
    if cv.getWindowProperty('frame', cv.WND_PROP_VISIBLE) < 1:
        break

# после цикла освобождаем камеру
vid.release()

# уничтожаем все окна
cv.destroyAllWindows()









# # img = cv.imread("images/test.png")
# # print (img.shape)


# # Укажите путь к изображению
# image_path = "images/test.png"

# # Загрузите изображение с помощью функции imread()
# image = cv.imread(image_path)

# # Проверьте, удалось ли загрузить изображение
# if image is not None:
#     # Показать изображение с помощью функции imshow()
#     cv.imshow("Изображение", image)
#     cv.waitKey(0)
#     cv.destroyAllWindows()
# else:
#     print("Не удалось загрузить изображени
  
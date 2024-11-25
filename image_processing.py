import glob
from PIL import Image
#функция считывания всех изображений из папки, на вход передается путь к файлу.
#вторая часть пути является формат файла, символ ** обозначает любое название файла в подкаталоге с этим окончанием
def init_files(path):  
    input_img = []
    for name in glob.glob(path + '/**.jpg'):
        input_img.append(Image.open(name).convert('RGB'))
    return input_img

#функция обработки изображений на вход подаются попарно изображения, полученные ранее
def processing_image(first_image, second_image): 
    pixel_mask = first_image.load() #доступ к пикселям первого изображения для их изменения

    for k in range(first_image.size[0]): #ширина
        for l in range(first_image.size[1]): #высота
            if first_image.getpixel((k, l))==second_image.getpixel((k, l)): #при совпадении пикселей они остаются неизменными
                pixel_mask[k, l] = first_image.getpixel((k, l)) 
            else:
                pixel_mask[k, l] = (0, 0, 0) # в случае отличия пиксель окрашивается в черный цвет
    return first_image #возвращается измененное первое изображение

list_img = init_files("fsdfsdfs") #указание пути к папке, где лежат файлы
for i in range(len(list_img)-1): #так как все изображения хранятся в списке
    image = processing_image(list_img[i], list_img[i+1]) #обрабатываем оба изображения
    list_img[i+1] = image #перезаписываем следующее изображение, так как второе изображение уже в себе несет первое
list_img[-1].show() #вывод самого последнего изображения из списка
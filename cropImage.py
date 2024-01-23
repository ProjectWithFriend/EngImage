from PIL import Image


def cropImage():
    for i in range(11, 12):
        img = Image.open('./images/cpe-page-{}.jpg'.format(i))

        for col in range(0, 2):
            for row in range(0, 4):
                box = (200 + (col * 1966), 200 + (row * 1377), 1966 + (col * 1966), (row * 1377) + 1377)
                img2 = img.crop(box)
                img2.save('croppedImages/cpe-page-{}-{}-{}.jpg'.format(i, col, row))

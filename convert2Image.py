from pdf2image import convert_from_path


def convert2Image():
    for i in range(118, 135):
        pages = convert_from_path('cpe.pdf', 500, first_page=i, last_page=i, thread_count=16)
        pages[0].save('images/cpe-page-{}.jpg'.format(i), 'JPEG')
        print("Page {} converted".format(i))

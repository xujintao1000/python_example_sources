import fitz
import re
import os

file_path = r'C:\xxx\practice.PDF'
dir_path = r'C:\xxx' # 存放图片的文件夹

def pdf2pic(path, pic_path):
    checkXO = r"/Type(?= */XObject)"
    checkIM = r"/Subtype(?= */Image)"
    pdf = fitz.open(path)
    lenXREF = pdf._getXrefLength()
    imgcount = 0
    for i in range(1, lenXREF):
        text = pdf._getXrefString(i)
        isXObject = re.search(checkXO, text)
        isImage = re.search(checkIM, text)
        if not isXObject or not isImage:
            continue
        imgcount += 1
        pix = fitz.Pixmap(pdf, i)
        new_name = f"img_{imgcount}.png"
        if pix.n < 5:
            pix.writePNG(os.path.join(pic_path, new_name))
        else:
            pix0 = fitz.Pixmap(fitz.csRGB, pix)
            pix0.writePNG(os.path.join(pic_path, new_name))
            pix0 = None
        pix = None

pdf2pic(file_path, dir_path)
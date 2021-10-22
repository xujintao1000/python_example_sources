"""
添加水印
使用说明：添加水印到指定文件里的所有pdf文件
"""

import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from copy import copy


def create_watermark(content):
    """水印信息"""
    # 默认大小为21cm*29.7cm
    file_name = "mark.pdf"
    c = canvas.Canvas(file_name, pagesize=(30 * cm, 30 * cm))
    # 移动坐标原点(坐标系左下为(0,0))
    c.translate(10 * cm, 5 * cm)

    img = PhotoImage

    c.drawImage("watermark.png", 10 * cm, 15 * cm)

    # # 设置字体
    # c.setFont("Helvetica", 30)
    # # 指定描边的颜色
    # c.setStrokeColorRGB(0, 1, 0)
    # # 指定填充颜色
    # c.setFillColorRGB(0, 1, 0)
    # # 旋转45度,坐标系被旋转
    # c.rotate(30)
    # # 指定填充颜色
    # c.setFillColorRGB(0, 0, 0, 0.1)
    # # 设置透明度,1为不透明
    # # c.setFillAlpha(0.1)
    # # 画几个文本,注意坐标系旋转的影响
    # for i in range(5):
    #     for j in range(10):
    #         a=10*(i-1)
    #         b=5*(j-2)
    #         c.drawString(a*cm, b*cm, content)
    #         c.setFillAlpha(0.1)
    # 关闭并保存pdf文件
    c.save()
    return file_name


def add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out):
    """把水印添加到pdf中"""
    pdf_output = PdfFileWriter()
    input_stream = open(pdf_file_in, 'rb')
    pdf_input = PdfFileReader(input_stream, strict=False)

    # 获取PDF文件的页数
    pageNum = pdf_input.getNumPages()

    # 读入水印pdf文件
    pdf_watermark = PdfFileReader(open(pdf_file_mark, 'rb'), strict=False)
    # 给每一页打水印
    for i in range(pageNum):
        page = pdf_input.getPage(i)
        page.mergePage(pdf_watermark.getPage(0))
        page.compressContentStreams()  # 压缩内容
        pdf_output.addPage(page)
    pdf_output.write(open(pdf_file_out, 'wb'))


# 插入水印
def check_if_rotate(pdf_file_in):
    pdf_output = PdfFileWriter()
    input_stream = open(pdf_file_in, 'rb')
    pdf_input = PdfFileReader(input_stream, strict=False)

    # 获取PDF文件的页数
    pageNum = pdf_input.getNumPages()

    # 读入水印pdf文件
    # pdf_watermark = PdfFileReader(open(pdf_file_mark, 'rb'), strict=False)
    # 给每一页打水印
    for i in range(pageNum):
        page = pdf_input.getPage(i)

        height = int(pdf_input.getPage(i).mediaBox[3])
        width = int(pdf_input.getPage(i).mediaBox[2])
        print('height: %d, width: %d' % (height, width))

        if height > width:
            page = pdf_input.getPage(i).rotateCounterClockwise(90)
        else:
            page = pdf_input.getPage(i)

        pdf_output.addPage(page)
    pdf_output.write(open("temp.pdf", 'wb'))

def rotate_method3(pdf_file_in, pdf_file_mark, pdf_file_out):
    watermark_paf = PdfFileReader(pdf_file_mark)
    watermark_page = watermark_paf.getPage(0)

    pdf_reader = PdfFileReader(pdf_file_in)
    pdf_writer = PdfFileWriter()

    print("pdf_reader.getNumPages()", pdf_reader.getNumPages())
    for page in range(pdf_reader.getNumPages()):
        original_page = pdf_reader.getPage(page)

        height = int(original_page.mediaBox[3])
        width = int(original_page.mediaBox[2])
        print('height: %d, width: %d' % (height, width))
        page = copy(original_page)

        if height > width:
            page = page.rotateClockwise(90)
            new_page = copy(watermark_page)
            page.mergePage(new_page)
            pdf_writer.addPage(page)

        # page = page.rotateClockwise(180)
        page2 = copy(original_page)
        new_page2 = copy(watermark_page)
        page2.mergePage(new_page2.rotateClockwise(90))
        pdf_writer.addPage(page2)

        page3 = copy(original_page)
        new_page3 = copy(watermark_page)
        page3.rotateClockwise(270)
        new_page3.rotateClockwise(270)
        page3.mergePage(new_page3)
        pdf_writer.addPage(page3)

        # new_page = copy(watermark_page)
        # new_page.mergePage(page)
        # pdf_writer.addPage(new_page)

    with open(pdf_file_out, "wb") as out:
        pdf_writer.write(out)


def method2(pdf_file_in, pdf_file_mark, pdf_file_out):
    watermark_paf = PdfFileReader(pdf_file_mark)
    watermark_page = watermark_paf.getPage(0)

    pdf_reader = PdfFileReader(pdf_file_in)
    pdf_writer = PdfFileWriter()

    for page in range(pdf_reader.getNumPages()):
        original_page = pdf_reader.getPage(page)
        new_page = copy(watermark_page)
        new_page.mergePage(original_page)
        pdf_writer.addPage(new_page)
    with open(pdf_file_out, "wb") as out:
        pdf_writer.write(out)


if __name__ == '__main__':
    pdf_file_in = '1.pdf'
    pdf_file_out = "rotateNew.pdf"
    # pdf_file_mark = 'watermark2.pdf'
    pdf_file_mark = 'water2.pdf'
    #
    # check_if_rotate(pdf_file_in)
    # add_watermark("temp.pdf", pdf_file_mark, pdf_file_out)
    rotate_method3("temp.pdf", pdf_file_mark, pdf_file_out)

import os
import fitz

pdf_dir = []
root = os.getcwd()
PDF_file = root+"\\PDF"


def get_file():
    docunames = os.listdir(PDF_file)
    for docuname in docunames:
        if os.path.splitext(docuname)[1] == '.pdf':  
            pdf_dir.append(docuname)


def conver_img():
    for pdf in pdf_dir:
        doc = fitz.open(PDF_file+'\\'+pdf)
        print("正在处理："+pdf)
        pdf_name = os.path.splitext(pdf)[0]
        if (os.path.exists(PDF_file+'\\'+pdf_name)) == False:
            os.mkdir(PDF_file+'\\'+pdf_name)
        page_num = 0
        for pg in range(doc.pageCount):
            page_num += 1
            page = doc[pg]
            rotate = int(0)
            zoom_x = 8.0
            zoom_y = 8.0
            trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
            pm = page.get_pixmap(matrix=trans, alpha=False, colorspace='rgb')
            pm.save(PDF_file+'\\'+pdf_name+'\\'+('%02d' % page_num)+'.png')


if __name__ == '__main__':
    get_file()
    conver_img()


from PIL import Image
import os
import fitz
root = os.getcwd()
imgRoot = root+"\\PDF"
pdfRoot = root+"\\outputPDF"


def combine2Pdf(folderPath, pdfFilePath):
    scale = 10
    files = os.listdir(folderPath)
    pngFiles = []
    sources = []
    for file in files:
        if 'png' in file:
            pngFiles.append(folderPath + file)
    pngFiles.sort()
    for file in pngFiles:
        pngFile = Image.open(file)
        if pngFile.mode != '1':
            pngFile = pngFile.convert("1")
            pngFile.save(file)

    doc = fitz.open()
    for img in pngFiles:
        imgdoc = fitz.open(img)
        pdfbytes = imgdoc.convert_to_pdf()
        imgpdf = fitz.open("pdf", pdfbytes)
        doc.insert_pdf(imgpdf)
    if os.path.exists(pdfFile):
        os.remove(pdfFile)
    doc.save(pdfFile)
    doc.close()


if __name__ == "__main__":
    if (os.path.exists(pdfRoot)) == False:
        os.mkdir(pdfRoot)
    filelist = os.listdir(imgRoot+"\\")
    for filename in filelist:
        if(filename.endswith(".pdf")):
            filelist.remove(filename)
    for filename in filelist:
        print("正在处理："+filename)
        folder = imgRoot+"\\"+filename+"\\"
        pdfFile = pdfRoot+"\\"+filename+".pdf"
        combine2Pdf(folder, pdfFile)

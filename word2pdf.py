from win32com.client import Dispatch
import os

root = os.getcwd()
pdfRoot = root+"\\PDF"
wordRoot = root


def doc2pdf(filePath, file):
    print("正在转换:", file)
    word = Dispatch('Word.Application')
    doc = word.Documents.Open(filePath)
    outFile = pdfRoot + "\\" + file.split('.')[0] + ".pdf"
    doc.SaveAs(outFile, FileFormat=17)
    doc.Close()
    word.Quit()


if __name__ == "__main__":
    if (os.path.exists(pdfRoot)) == False:
        os.mkdir(pdfRoot)
    filelist = os.listdir(wordRoot)
    for file in filelist:
        if (file.endswith(".doc") or file.endswith(".docx")) and ("~$" not in file):
            filePath = wordRoot+"\\"+file
            doc2pdf(filePath, file)

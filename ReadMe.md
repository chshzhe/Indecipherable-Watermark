# 一键WORD转PDF

## Feature

1. PDF里面是图片，无法被直接编辑去水印
2. 图片采用单色像素，水印去除难度极大
3. 一键搞定，方便快捷

<img src="ReadMe.assets/1.png" alt="1" width="150" height="150" />

## Install

- 需要使用`Microsoft Word`

## How to use？

1. 把需要转换的Word文件(后缀为`.docx`或者`.doc`)放入这个`Project`文件夹 **OR** 将`word2pdf.exe`、`pdf2img.exe`、`img2pdf.exe`和`RunCode.bat`放入你需要转换的Word目录下

2. 双击打开`RunCode.bat`自动执行程序

3. 程序运行完毕，打开该目录下的`outputPDF`的文件夹，就是生成的PDF文件

## How to work？

1. `RunCode.bat`按如下次序依次调用三个程序；
2. `word2pdf.exe`把当前目录下（不包括子目录）所有Word文件转为RGB色彩的PDF，保存在`./PDF`里，文件名为`<Word_name>.pdf`；
3. `pdf2img.exe`把`./PDF`里所有PDF文件导出为PNG文件，分别保存在`./PDF/<Word_name>/<Page_Number>.png`里，考虑到实际需求，这里限制导出页数不超过99张（可以根据需要扩容到任意多张）；
4. `img2pdf.exe`把`./PDF/<Word_name>`下的所有图片转化为单色图并覆盖保存，再将这些单色图合成PDF保存在`./outputPDF/<Word_name>.pdf`里。

## Developer

- **chshzhe**

  Github: https://github.com/chshzhe/Indecipherable-Watermark


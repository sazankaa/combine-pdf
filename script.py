from pypdf import PdfWriter
from pathlib import Path

#pdfsフォルダの中身を順に取り出し、名前でソートしリストとして返す。

dir =Path("./pdfs")

def makekdir(): # dir つくる
    if not dir.exists():
        print("There is not './pdfs'")
        question = input("Make Dirctory ? (y or n)\n") 
        if question == 'y':
            dir.mkdir()
            print("Iretene!") 
        elif question == 'n':
            print("hoooooom...")
        else:
            print("Enter y or n!")
        exit(1)


makekdir()

if not list(dir.glob('*.pdf')):
    print("No files.")
    exit(2) 

files = sorted(dir.iterdir())

print(f"Page's number > {len(files)}")

#書き込みオブジェクトの作成
writer = PdfWriter()

for pdf in files:
    #pdfをwriterに順に追加していく
    writer.append(pdf)

writer.write(str(input("MERGED file name > ")) + ".pdf")
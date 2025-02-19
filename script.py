from pypdf import PdfWriter
from pathlib import Path

#pdfsフォルダの中身を順に取り出し、名前でソートしリストとして返す。

p =Path("./pdfs")

if not p.exists():
    print("pdfsディレクトリがありません。")
    dirflag = input("ディレクトリを作りますか？(y or n)\n")
    if dirflag == 'y':
        p.mkdir()
    exit(1)

if not list(p.glob('*.pdf')):
    print("ファイルなくね？")
    exit(2) 

files = sorted(p.iterdir())

print(f"全ページ数は{len(files)}でしたね。")

#書き込みオブジェクトの作成
writer = PdfWriter()

for pdf in files:
    #pdfをwriterに順に追加していく
    writer.append(pdf)

name = input("書き込み後のファイル名は如何様に?\n")
writer.write(str(name) + ".pdf")
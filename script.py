from pypdf import PdfWriter
from pathlib import Path

#pdfsフォルダの中身を順に取り出し、名前でソートしリストとして返す。
files = sorted(Path("./pdfs").iterdir())

#書き込みオブジェクトの作成
writer = PdfWriter()

for pdf in files:
    #pdfをwriterに順に追加していく
    writer.append(pdf)

writer.write("MERGED.pdf")
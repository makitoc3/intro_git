import os, tkinter, tkinter.filedialog, tkinter.messagebox

# ファイル選択ダイアログの表示
root = tkinter.Tk()
root.withdraw()
fTyp = [("","*")]
iDir = os.path.abspath(os.path.dirname(__file__))
tkinter.messagebox.showinfo('RHデータ処理プログラム','処理ファイルを選択してください！')
file = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)

# ファイルをオープンする
file = open(bathfile)

# 一行ずつ読み込んでは表示する
for line in file:
  print line

# ファイルをクローズする
test_data.close()

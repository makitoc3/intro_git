import serial
ser = serial.Serial('/dev/tty.',9600,timeout=None)  # デバイス名とボーレートを設定しポートをオープン 
ser.write("hello")      # 出力
ser.close()             # ポートのクローズ
ser = serial.Serial('/dev/ttyS0', timeout=0.1)  # timeoutを秒で設定（default:None)ボーレートはデフォルトで9600
c = ser.read()  # 1文字読み込み
str = ser.read(10)  # 指定も字数読み込み ただしtimeoutが設定されている婆は読み取れた分だけ
line = ser.readline()  # 行終端'?n'までリードする
ser.close()

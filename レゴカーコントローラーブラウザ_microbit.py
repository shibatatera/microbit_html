from microbit import *

# サーボモーター レゴカーのタイヤ２つ動かす
# pin0の値が大きいと前進 小さいと後退。pin1のタイヤは逆回転する

uart.init(baudrate=115200)
pin0.set_analog_period(20)
pin1.set_analog_period(20)

while True:
    if uart.any():
        data = uart.readline()
        try:
            # 送られてきた "102,52" のような文字列をカンマで分割
            parts = data.decode().strip().split(',')
            
            if len(parts) == 2:
                # 数値に変換してそれぞれのピンに出力
                val0 = int(parts[0])
                val1 = int(parts[1])
                pin0.write_analog(val0)
                pin1.write_analog(val1)
        except:
            pass
    sleep(10)
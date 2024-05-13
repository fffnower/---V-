import pyautogui
import time

# 给个时间把焦点调整到输入框
times = 5

while True:
    
    print('使用微软IME中文输入模式，设置SHIFT为中英文切换；')
    text = input(f'输入文字，并在{times}秒内切换的需粘贴的焦点位置：' )
    time.sleep(times)

    # 以中文方式开始
    chinese = True

    for char in text:
        unicode_chars = char.encode('unicode-escape').decode()
        # unicode_chars = '\uxxxx'

        if unicode_chars[:2] == r'\u':
            for code in f'vuc{unicode_chars[2:]}':
                pyautogui.press(code)
            pyautogui.press(' ')
        else:
            pyautogui.press('shift')
            chinese = not chinese 
            pyautogui.typewrite(char)

        if chinese != True:
            pyautogui.press('shift')
            chinese = not chinese 

    print('-----------------------------------------------')

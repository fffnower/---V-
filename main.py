import pyautogui
import time

# 改为input()方法
text = '这是一个测试。 this is a test.' 

# 给个时间把焦点调整到输入框
time.sleep(3)

# 以中文方式开始
chinese = True

for char in text:
    unicode_chars = char.encode('unicode-escape').decode()
    # print(char, unicode_chars)
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

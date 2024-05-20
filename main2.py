import win32gui
import win32api
import win32con
import win32process
import time

while True:
    times = 3
    text_to_type = input(f'输入文字，并在{times}秒内切换到需粘贴的输入框：' )

    print(f'\'复制\'成功！')
    # 调整焦点的时间
    for i in range(times, 0, -1):
        print(f'在{i}秒内将焦点切换到输出位置！')
        time.sleep(1)

    # 获取当前活动窗口的句柄
    hwnd_foreground = win32gui.GetForegroundWindow()

    # 获取窗口的线程ID
    thread_id, process_id = win32process.GetWindowThreadProcessId(hwnd_foreground)

    # 获取当前线程ID
    self_thread_id = win32api.GetCurrentThreadId()

    # 将输入焦点附加到当前线程
    win32process.AttachThreadInput(thread_id, self_thread_id, True)

    # 获取具有输入焦点的控件句柄
    hwnd_focus = win32gui.GetFocus()

    # 取消附加的线程
    win32process.AttachThreadInput(thread_id, self_thread_id, False)

    # hwnd_focus 现在包含焦点控件的句柄
    # print(f'焦点控件句柄: {hwnd_focus}')

    # 设置焦点到活动句柄
    win32gui.SetForegroundWindow(hwnd_focus)

    # 输出文本
    for char in text_to_type:
        win32api.SendMessage(hwnd_focus, win32con.WM_CHAR, ord(char), 0)

    print('\'粘贴\'成功！')
    print('-----------------------------------------------')

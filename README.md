# 1. 基于微软IME特性的模拟中文输出脚本(main.py)

### 1.  原理
微软IME的 V 模式输入 可用于输入中文格式的数字、日期、时间、公式等。 它还支持输入 Unicode 和 GB-18030 码位。 处于双拼音模式时，可以通过按 Shift + V 触发 V 模式。 在 “IME 设置 > 高级”中找到此[功能](https://support.microsoft.com/zh-cn/windows/microsoft-%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-ime-9b962a3b-2fa4-4f37-811c-b1886320dd72)。

![image](https://github.com/fffnower/---V-/assets/32289652/94cf3af5-7c02-4e30-83cb-c2161ab2d9b1)

### 2. 前置条件：
  - 使用微软IME全拼（双拼确实可以用 Shift + v 触发v模式，但是不能进行vucxxxx的Unicode码输入）
  - 使用Shift进行中英文切换
  - 输出窗口以中文方式开始

### 3. 应用场景
  - 当有些例行公事的答题网站，居然锁了粘贴时。。。

# 2. 调用Windows API进行中文输出脚本(main2.py)

### 1.  原理
  - 获取活动窗口句柄直接输出

### 2. 前置条件：
  - 管理员权限运行

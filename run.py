# -------------------------------------------------
# A simple script for hanging up the Warcraft
#
# Author：Wang Ke
#
# Notes: 1.Warcraft restarts every 5 hours.
#        2.Please make sure the Room window is the last one to open.
#
# ---------------------------------------------------

import win32gui
import win32con
import time
import pyautogui
hang_time=5 # hours
if __name__ == '__main__':
    handle1 = win32gui.FindWindow("Qt5152QWindowIcon", "RPG - 魔兽争霸官方对战平台")
    while (1):
        # Start Warcraft
        win32gui.SetForegroundWindow(handle1)
        a = pyautogui.locateOnScreen(r'.\start.png')
        x, y = pyautogui.center(a)
        print(x, y)
        pyautogui.click(x, y,clicks=2,duration=1)
        # Hang up
        hang_time = hang_time * 60 * 60
        time.sleep(hang_time)
        # Close Warcraft
        handle2 = win32gui.FindWindow("Warcraft III", None)
        # win32gui.ShowWindow(handle2, win32con.SW_SHOWMINIMIZED)
        press_list = [121, 69, 81]
        for i in press_list:
            win32gui.PostMessage(handle2, win32con.WM_KEYDOWN, i, 0)
            # win32gui.PostMessage(handle, win32con.WM_KEYUP, i, 0)
        time.sleep(3)  # waiting to close war3
        win32gui.PostMessage(handle2, win32con.WM_KEYDOWN, 79, 0)
        time.sleep(5)
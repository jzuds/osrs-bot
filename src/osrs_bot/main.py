import os
import Xlib.display
from pyvirtualdisplay.display import Display
disp = Display(visible=True, size=(1366, 768), backend="xvfb", use_xauth=True)
disp.start()
import pyautogui


def main():
    pyautogui._pyautogui_x11._display = Xlib.display.Display(os.environ['DISPLAY'])
    print(pyautogui.size(), pyautogui.position())

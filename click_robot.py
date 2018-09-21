import win32api, win32con

import time


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def get_pos():
    return win32api.GetCursorPos()


last_pos = pos = get_pos()
while True:
    time.sleep(120)
    pos = get_pos()
    if last_pos == pos:
        print("Last pos %s ; At this moment pos %s; Robot worked." % (last_pos, pos))
        click(10, 10)
        last_pos = get_pos()
    else:
        print("Last pos %s ; At this moment pos %s; Robot doesn't have to work." % (last_pos, pos))
        last_pos = pos


# add logic for break.
# add logic for keyboard status check
# add time log

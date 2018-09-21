import win32api, win32con

import time
import datetime

time_format = "%Y-%m-%d %H:%M:%S"


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def get_pos():
    return win32api.GetCursorPos()


def time_to_str(time_v="now"):
    if time_v == "now":
        now_time_struct = time.localtime(time.mktime(time.localtime()))
        return time.strftime(time_format, now_time_struct)
    else:
        now_time_struct = time.localtime(time_v)
        return time.strftime(time_format, now_time_struct)


def time_value(time_str="now"):
    if time_str == "now":
        return time.mktime(time.localtime())
    else:
        time_str = time.strftime(time_format.split(' ')[0] + " ", datetime.date.today().timetuple()) + time_str
        return time.mktime(time.strptime(time_str, time_format))


start_time = "09:00:00"
end_time = "20:36:00"
last_pos = pos = get_pos()
while True:
    now = time_value()
    if time_value(start_time) < now < time_value(end_time):
        time.sleep(20)
        pos = get_pos()
        if last_pos == pos:
            print("%s: Last pos %s ; At this moment pos %s; Robot worked." % (time_to_str(now), last_pos, pos))
            click(10, 10)
            last_pos = get_pos()
        else:
            print("%s: Last pos %s ; At this moment pos %s; Robot doesn't have to work." %
                  (time_to_str(now), last_pos, pos))
            last_pos = pos

# add logic for break.
# add logic for keyboard status check
# add time log


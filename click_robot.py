import win32api
import win32con
import time
import datetime
import configparser
import os


config = configparser.ConfigParser()
conf_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'conf', 'setting')
config.read(conf_dir)

time_format = config.get("log", "time_format")
start_time = config.get("robot", "start_time")
end_time = config.get("robot", "end_time")


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


last_pos = pos = get_pos()
while True:
    time.sleep(120)
    now = time_value()
    if time_value(start_time) < now < time_value(end_time):
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
# config file management

# class ClickRobot(object):
#
#
#

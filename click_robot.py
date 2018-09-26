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


class ClickRobot(object):
    start_time = ""
    end_time = ""
    break_start = ""
    break_end = ""
    pos = ""
    last_pos = ""

    def __init__(self):
        self.start_time = config.get("robot", "start_time")
        self.end_time = config.get("robot", "end_time")
        self.break_start = config.get("robot", "break_start")
        self.break_end = config.get("robot", "break_end")
        self.last_pos = self.pos = self.get_pos()

    def click(self, x, y):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

    def get_pos(self):
        return win32api.GetCursorPos()

    def run(self):
        while True:
            time.sleep(120)
            now = time_value()
            if time_value(self.start_time) < now < time_value(self.break_start) or time_value(
                    self.break_end) < now < time_value(self.end_time):
                self.pos = self.get_pos()
                if self.last_pos == self.pos:
                    print("%s: Last pos %s ; At this moment pos %s; Robot worked." %
                          (time_to_str(now), self.last_pos, self.pos))
                    self.click(10, 10)
                    self.last_pos = self.get_pos()
                else:
                    print("%s: Last pos %s ; At this moment pos %s; Robot doesn't have to work." %
                          (time_to_str(now), self.last_pos, self.pos))
                    self.last_pos = self.pos
            elif now < time_value(self.start_time) or now > time_value(self.end_time) or time_value(
                    self.break_start) < now < time_value(self.break_end):
                print("%s: Last pos %s ; At this moment pos %s; Robot is having a break." %
                      (time_to_str(now), self.last_pos, self.pos))


def time_to_str(time_v="now"):
    if time_v == "now":
        now_time_struct = time.localtime(time.mktime(time.localtime()))
        return time.strftime(time_format, now_time_struct)
    else:
        # TODO:time_v check
        now_time_struct = time.localtime(time_v)
        return time.strftime(time_format, now_time_struct)


def time_value(time_str="now"):
    if time_str == "now":
        return time.mktime(time.localtime())
    else:
        # TODO:time_str check
        time_str = time.strftime(time_format.split(' ')[0] + " ", datetime.date.today().timetuple()) + time_str
        return time.mktime(time.strptime(time_str, time_format))


# add logic for keyboard status check

if __name__ == "__main__":
    robot = ClickRobot()
    robot.run()

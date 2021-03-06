import json

from PyQt5.QtCore import *


class AgentStats:
    def __init__(self):
        self.program_start_time = QDateTime.currentDateTime()

        # 登陆成功时间点
        self.login_time_points = []
        self.logout_time_points = []

        # 重新创建nam
        self.refresh_time_points = []
        self.poll_timeout_count = 0

        self.recv_message_count = 0
        self.send_message_count = 0
        self.recv_message_length = 0
        self.send_message_length = 0
        self.send_message_error_count = 0
        return

    def toJson(self):
        def time2str(t):
            if t is None: return ''
            return t.toString()

        stats = {
            "start_time": time2str(self.program_start_time),
            "login_times": len(self.login_time_points),
            "logout_times": len(self.logout_time_points),
            "refresh_count": len(self.refresh_time_points),
            "poll_timeout_count": self.poll_timeout_count,
            "recv_count": self.recv_message_count,
            "recv_length": self.recv_message_length,
            "send_count": self.send_message_count,
            "send_length": self.send_message_length,
            "send_error_count": self.send_message_error_count,
            "first_login_time": time2str(self.firstLoginTime()),
            "last_login_time": time2str(self.lastLoginTime()),
            "last_logout_time": time2str(self.lastLogoutTime()),
        }
        res = json.JSONEncoder(ensure_ascii=False).encode(stats)
        return res

    def toText(self):
        res = ''
        return res

    # 登陆事件
    def onLogin(self):
        self.login_time_points.append(QDateTime.currentDateTime())
        return

    # 登出事件
    def onLogout(self):
        self.logout_time_points.append(QDateTime.currentDateTime())
        return

    def onRefresh(self):
        self.refresh_time_points.append(QDateTime.currentDateTime())
        return

    def onPollTimeout(self):
        self.poll_timeout_count += 1
        return

    def onRecvMessage(self, msg):
        self.recv_message_count += 1
        self.recv_message_length += len(msg)
        return

    def onSendMessage(self, msg):
        self.send_message_count += 1
        self.send_message_length += len(msg)
        return

    def onSendMessageError(self):
        self.send_message_error_count += 1
        return

    def firstLoginTime(self):
        n = len(self.login_time_points)
        if n == 0: return None
        return self.login_time_points[0]

    def lastLoginTime(self):
        n = len(self.login_time_points)
        if n == 0: return None
        return self.login_time_points[n - 1]

    def lastLogoutTime(self):
        n = len(self.logout_time_points)
        if n == 0: return None
        return self.logout_time_points[n - 1]

    def pollTimeoutCount(self):
        return self.poll_timeout_count

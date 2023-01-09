"""
    Environment: class share common methods and attributes
    across different software windows (Inherite to use)

    html: class holds repeated html tags and styling for the UI
"""

import os
from ftplib import FTP

class Environment:
    def __init__(self) -> None:
        self.app_version = "5.02"
        self.app_release_date = "Sept 5th, 2022"

        self.screen_w = 0
        self.screen_h = 0

        self.ftp = FTP()
        self.working_dir = "user/appmeta"
        self.local_path = str(os.getcwd())
        self.temp_path = self.local_path + "\Data\prxUserMeta\\"
        self.img_dir = self.local_path + "\\data\\User\\appmeta"

        self.sys_path = "system_ex/app"

        self.setting_path = ""
        self.local_path = self.local_path.replace("\\", "/")

        self.IP = "not accepted"
        self.Port = 21

        self.all_CUSA = []
        self.all_CUSA_ex = []
        self.all_CUSA_sys = []
        self.Game = {}
    
    def get_update_release_date(self) -> None:
        return self.app_release_date

    def get_update_version(self) -> None:
        return self.app_version

    def set_screen_size(self, w, h) -> None:
        self.screen_w = w
        self.screen_h = h

    def get_settings(self) -> None:
        self.userFont = "Arial"
        self.userPort = "1337"
        self.userIp = ""
        self.userIPath = self.local_path
        self.userDPath = self.local_path
        self.userHB = "False"
        try:
            with open("Data/Pref/pref.ini") as file:
                content = file.readlines()
                self.userFont = content[0][2:-1]
                self.userPort = content[1][2:-1]
                self.userIp = content[2][3:-1]
                self.userIPath = content[3][6:-1]
                self.userDPath = content[4][6:-1]
                self.userHB = content[5][3:].strip()
        except Exception as e:
            self.logs(str(e), "Warning")

class html:
    def __init__(self) -> None:
        self.start = "<html><head/><body>"
        self.end = "</p></body></html>"

    def a_tag(self, href: str, txt: str, color: str, size: int, cstm_style: str = "", align: str = "center") -> str:
        ##############################################
        ####             HTML Link
        ##############################################
        return f'{self.start}<p align="{align};"><a href="{href}"><span style="text-decoration: underline; font-size:{size}pt; color:{color}; {cstm_style}">{txt}</span></a>{self.end}'

    def span_tag(self, txt: str, color: str, size: int, align="center", weight=700) -> str:
        ##############################################
        ####             HTML Text
        ##############################################
        return f'{self.start}<p align="{align}"><span style=" font-size:{size}pt; font-weight:{weight}; color:{color};">{txt}</span>{self.end}'

# class User_Prefrence(Environment):
#     # user settings and prefs here
#     def __init__(self) -> None:
#         super().__init__()


    
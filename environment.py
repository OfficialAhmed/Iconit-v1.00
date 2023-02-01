"""
    Common: class share common methods and attributes
    across different software windows (Inherite to use)

    html: class holds repeated html tags and styling for the UI
    constant: class holds constant vars. Only getters
"""
import os, datetime
from ftplib import FTP

from Module.Database.Generate import Database
from Module.Settings import Main as Settings
from Module.Widget.Shared import Widget

class Common:
    """
        * A Bridge class to connect between multiple ones
        
        Class attributes accessable anywhere (SHARABLE ACCROSS CHILDS)
            - (Change attribute value) via setters
            - (Access attribute value) via direct call i.e. 'class_name.attr_name'
        
        init attributes are child specific.
        Childs of this class have a copy of those attributes (NOT SHARABLE ACCROSS CHILDS)
            - (Change attribute value) via self assignment & setters
            - (Access attribute value) via self call
    """

    #__________  if Settings.json not found use these _________#
    # FIXME: reconstruct this block to call the defaults from settings moduel (self.default_settings)
    app_path = os.getcwd()
    # cached_port = "21"
    # cached_font = "Arial"
    # cached_ip = "192.168.1.1"
    # cached_language = "English"
    # cached_icons_path = os.getcwd()
    # cached_download_path = os.getcwd()
    # cached_toggled_homebrew = "False"

    default_settings = {"font":"Arial", "port":"21", "ip":"", "icons_path":app_path, "download_path":app_path, "homebrew":"False", "language":"English"}
    
    #__________  shared attrs _________#
    screen_w = 0
    screen_h = 0
    ui = None
    window = None

    # Store connection for GoldHen one connection 
    connection = None 

    all_game_ids = {}
    selected_mode = None

    current_game_id = ""
    browsed_icon_path = ""
    browsed_bg_img_path = ""

    upload_type = ""
    is_sys_icon = False

    def __init__(self) -> None:
        self.app_version = "5.06 BETA"
        self.app_release_date = "Jan 27th, 2023"

        self.game = {}
        self.game_ids = {}
        self.sys_game_ids = []
        self.external_game_ids = []
        self.screen_w = Common.screen_w
        self.screen_h = Common.screen_h

        self.ip = Common.default_settings.get("ip")
        self.port = Common.default_settings.get("port")
        self.cached_ip = Common.default_settings.get("ip")
        self.cached_font = Common.default_settings.get("font")
        self.cached_port = Common.default_settings.get("port")
        self.cached_language = Common.default_settings.get("language")
        self.cached_icons_path = Common.default_settings.get("icons_path")
        self.cached_download_path = Common.default_settings.get("download_path")
        self.cached_toggled_homebrew = Common.default_settings.get("homebrew")

        self.app_root_path = f"{Common.app_path}\\"
        self.data_path = f"{self.app_root_path}Data\\"
        self.pref_path = f"{self.data_path}Pref\\"
        self.temp_path = f"{self.data_path}Cache\\"
        self.language_path = f"{self.data_path}Language\\"
        self.appmeta_path = f"{self.data_path}User\\appmeta\\"
        self.metadata_path = f"{self.temp_path}Icons\\metadata\\"
        self.database_file = f"{self.temp_path}Database.json"
        self.cache_path = f"{self.metadata_path}game\\"
        self.game_cache_file = f"{self.cache_path}games.json"
        self.undetected_games_file = f"{self.app_root_path}GAMES MADE CACHING SLOWER.txt"
        self.setting_path = ""


        self.ftp = FTP()
        self.html = html()
        self.widgets = Widget()
        self.constant = Constant()
        self.settings = Settings()
        self.settings.set_paths(self.app_root_path, self.temp_path)
        self.settings.init()

        self.database = Database(self.database_file)

        self.ps4_system_icons_dir = self.constant.PS4_SYS_ICONS
        self.ps4_internal_icons_dir = self.constant.PS4_INT_ICONS
        self.ps4_external_icons_dir = self.constant.PS4_EXT_ICONS

        self.backup_path = f"{self.constant.ICONS_BACKUP_NAME}\\"

        self.logging = self.html.internal_log_msg("ps4", self.ip, 12, "font-weight:600; font-style:italic;")
        self.fetch_settings_cache()


    def fetch_settings_cache(self) -> None:
        self.settings.set_defaults(self.default_settings)
        settings_cache = self.settings.update_local_cache(self.temp_path)

        ip = settings_cache.get("ip")
        hb = settings_cache.get("homebrew")
        font = settings_cache.get("font")
        port = settings_cache.get("port")
        lang = settings_cache.get("language")
        Ipath = settings_cache.get("icons_path")
        Dpath = settings_cache.get("download_path")
        Common.cached_ip, self.cached_ip = ip, ip
        Common.cached_font, self.cached_font = font, font
        Common.cached_port, self.cached_port = port, port
        Common.cached_language, self.cached_language = lang, lang
        Common.cached_icons_path, self.cached_icons_path = Ipath, Ipath
        Common.cached_toggled_homebrew, self.cached_toggled_homebrew = hb, hb
        Common.cached_download_path, self.cached_download_path = Dpath, Dpath        


    def logs(self, description, Type):
        try: error_file = open("Logs.txt", "a")
        except: error_file = open("Logs.txt", "w+")

        error_file.write(
            f"{str(datetime.datetime.now())}| _DEV {Type}: {str(description)} \n"
        )


    def get_server_directories(self) -> tuple:
        " This is a solution since PS4 ftp doesnt support nlst()."
        result = []
        self.ftp.retrlines("LIST ", lambda line : result.append(line.split(" ")[-1]))
        return tuple(result)


    def download_data_from_server(self, file_name, file_path_with_extension) -> None:
        with open(file_path_with_extension, "wb") as downloaded_file:
            self.ftp.retrbinary("RETR " + file_name, downloaded_file.write, 65536)


    def get_translation(self, lang, window_to_translate):
        # func call from Settings module
        return self.settings.get_translation(lang, window_to_translate)


    def get_language(self):
        return Common.cached_language

    def set_language(self, lang):
        Common.cached_language = lang

    def get_window(self):
        return Common.window

    def set_window(self, ptr):
        Common.window = ptr

    def set_ui(self, ptr):
        Common.ui = ptr

    def get_ui(self):
        return Common.ui

    def set_ftp(self, ptr):
        Common.connection = ptr

    def get_ftp(self):
        return Common.connection
        
    def set_browsed_bg_img_path(self, path:str):
        Common.browsed_bg_img_path = path

    def get_browsed_bg_img_path(self):
        return Common.browsed_bg_img_path

    def set_is_sys_icon(self, sys:bool):
        Common.is_sys_icon = sys

    def get_is_sys_icon(self):
        return Common.is_sys_icon

    def set_upload_type(self, t:str):
        Common.upload_type = t

    def get_upload_type(self):
        return Common.upload_type

    def set_current_game_id(self, id:str):
        Common.current_game_id = id

    def get_current_game_id(self):
        return Common.current_game_id
        
    def set_browsed_icon_path(self, path:str):
        Common.browsed_icon_path = path

    def get_browsed_icon_path(self):
        return Common.browsed_icon_path

    def set_game_ids(self, ids:dict):
        Common.all_game_ids = ids

    def get_all_game_ids(self):
        return Common.all_game_ids

    def set_selected_mode(self, mode:str):
        Common.selected_mode = mode

    def get_selected_mode(self):
        return Common.selected_mode

    def set_ip_port(self, ip, port) -> None:
        """ Make Ip and Port sharable between classes """
        self.ip, self.port = ip, port
        Common.default_settings["ip"], Common.default_settings["port"] = ip, port

    def get_ip(self):
        return Common.default_settings.get("ip")

    def get_port(self):
        return int(Common.default_settings["port"])
        
    def set_screen_size(self, w, h) -> None:
        self.screen_w, Common.screen_w = w, w
        self.screen_h, Common.screen_h = h, h


class html:
    def __init__(self) -> None:
        self.start = "<html><head/><body>"
        self.end = "</p></body></html>"
        self.constant = Constant()


    def p_tag(self, cstm_style, txt=None) -> str:
        """  generate Paragraph """
        return f'<p align="center" style="{cstm_style}">{txt}</p>'


    def a_tag(self, href:str, txt:str, color:str, size:int, cstm_style: str = "", align: str = "center", font="Arial") -> str:
        """  generate Link """
        return f'{self.start}<p align="{align}"><a href="{href}"><span style="text-decoration: underline; font-size:{size}pt; color:{color}; {cstm_style}; font-family: {font}">{txt}</span></a>{self.end}'
        

    def span_tag(self, txt:str, color:str, size:int, align:str = "center", weight = 700, font="Arial") -> str:
        """  generate Text """
        return f'{self.start}<p align="{align}"><span style=" font-size:{size}pt; font-weight:{weight}; color:{color}; font-family: {font}">{txt}</span>{self.end}'


    def tooltip_tag(self, txt:str) -> str:
        return f"<p style='color:Black'>{txt}</p>"


    def bg_image(self, url:str) -> str:
        return f"background-image: url({url});"


    def border_image(self, url:str) -> str:
        return f"border-image: url({url});"


    def internal_log_msg(self, state, msg, size=10, custome_style="") -> str:
        """ generate a logging line as <p> tag"""
        color = {
            "error":self.constant.get_color("red"),
            "warning":self.constant.get_color("orange"),
            "success":self.constant.get_color("green"),
            "ps4":self.constant.get_color("white")
        }

        style = f"margin: 0px; -qt-block-indent:0; text-indent:0px; font-size:{size}pt; color:{color[state]}; {custome_style}"
        return self.p_tag(style, f"[{state.upper()}] : {msg}")


class Constant:
    """ Read-only class """

    PS4_INT_ICONS = "user/appmeta/"
    PS4_EXT_ICONS = "user/appmeta/external/"
    PS4_SYS_ICONS = "system_ex/app/"
    PS4_ICON_SIZE = (512, 512)
    PS4_PRONOUNCIATION_FILE = "pronunciation.xml"

    ICONS_BACKUP_NAME = "Backup"
    HASH_COLOR = {
        "red":"#e83c3c",
        "green":"#55ff00",
        "white":"#ffffff",
        "orange":"#ffaa00",
    }


    def __init__(self) -> None:
        # init the self parameter
        pass


    def __setattr__(self, __name: str, __value: any) -> None:
        raise AttributeError(f"READ-ONLY: Class 'Constant' allow getters only. Occured while trying to set [{__name}]")
        

    def get_color(self, x:str) -> str:
        return Constant.HASH_COLOR[x]

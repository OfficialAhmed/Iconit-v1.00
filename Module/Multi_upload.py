"""
    Class: 
    Handles the generation of required NO. of icons and uploading them to PS4.

    Desc:
    Upon icons generation sucess, upload to PS4. Otherwise, keep them stored to retry on user next login
"""

import os, json, PIL
import Common.Uploader as Uploader

from environment import Common
from ftplib import FTP
from PIL import Image

class Main(Common):
    
    def __init__(self) -> None:
        super().__init__()
        
        self.ftp:FTP = self.get_ftp()
        self.game_ids:dict = self.get_ids()
        self.uploader = Uploader.Main()


    def last_process(self, last_group_path:str = "") -> str|None:
        """
            Save/Load process file with the group path 
        """

        # If path passed (write), else (read)
        if last_group_path:
            with open(self.last_baked_group_file, "w+") as file:
                file.write(last_group_path)
        
        else:
            with open(self.last_baked_group_file) as file:
                return file.readline()


    def continue_upload(self, continue_btn_widget, upload_btn_widget, state_widget):
        """
            Unfinished process detected, allow user to continue uploading the rest of baked icons
        """

        self.generate_icons_from_baked(state_widget, upload_btn_widget, self.last_process())
        continue_btn_widget.setEnabled(False)


    def upload_baked_icons(self, game_directory:str, icons:list):
        """
            Upload set of generated icons for the game. One call per game
        """

        self.ftp.cwd(f"/{game_directory}")

        for icon in icons:
            icon_dir = f"{self.icons_cache_path}{icon}"
            self.uploader.upload_to_server(icon_dir, icon)


    def generate_icons_from_baked(self, state_widget, upload_btn_widget, group_path):
        """
            Baked icons are ready. 
            Make required NO. of icons for each baked icon in the selected group
        """

        state_widget.setText("UPLOADING... PLEASE WAIT")
        self.last_process(group_path)

        self.selected_group_icons = json.load(open(group_path))
        baked_icons = os.listdir(self.baked_path)
        icons_to_upload = []

        for current_icon_id in self.selected_group_icons:
            
            # Process only successfull baked icons
            if f"{current_icon_id}.png" not in baked_icons:
                continue
            
            icon = Image.open(f"{self.baked_path}{current_icon_id}.png")
            resized_icon = icon.resize(self.constant.get_ps4_icon_size(), PIL.Image.ANTIALIAS)

            self.current_game_icons = self.game_ids.get(current_icon_id).get("icons")
            
            # Iterate through the icons required for the current game
            for current_image in self.current_game_icons:
                
                # iconXX (png/dds) format only
                if ".png" not in current_image and ".dds" not in current_image:
                    continue

                if "icon" not in current_image:
                    continue


                icon_cache_path = f"{self.icons_cache_path}{current_image}"
                icon_cache_path_no_extension = icon_cache_path[:-4]

                if ".png" in current_image:
                    resized_icon.save(icon_cache_path)

                elif ".dds" in current_image:
                    # Creat a temp .png, then convert it to .dds

                    resized_icon.save(f"{icon_cache_path_no_extension}.png")
                    self.uploader.png_to_dds(f"{icon_cache_path_no_extension}.png", self.icons_cache_path)

                icons_to_upload.append(current_image)

            try:
                game_directory = self.get_ps4_game_location(current_icon_id)
                self.upload_baked_icons(game_directory, icons_to_upload)

                # Move baked icon to cache for local view upon upload success
                self.uploader.update_local_icon(f"{self.baked_path}{current_icon_id}.png", current_icon_id)
                state_widget.setText("DONE!")

            except Exception as e:
                self.log_to_external_file(str(e), "upload - baked mask")            
                state_widget.setText("ERROR - READ logs.txt")

        upload_btn_widget.setEnabled(False)
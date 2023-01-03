import json
from src.fileWrapper import FileWrapper 

class Settings:

    SETTINGS_FILE_PATH = "settings.json"

    fwSettings = object 

    def __init__(self):

        self.fwSettings = FileWrapper(Settings.SETTINGS_FILE_PATH, 'w+')

        if (not self.fwSettings.fileIsOk):
            #bad situation. What would we do?
            return
            pass
        #otherfise all good
        json_str = self.fwSettings.readLinesToStr()
        if len(json_str) == 0:
            #probably file was cleared or just created
            pass
        else:
            try:
                data = json.loads(json_str)
            except:
                pass

        #если файл существует - читать. Иначе создать и записать в него простейшие настройки

#         {
#           "options_file_path": "",
#           "banner_file_path": ""
#         }

        pass
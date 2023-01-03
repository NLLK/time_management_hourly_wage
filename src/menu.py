from src.fileWrapper import FileWrapper
from src.options import Options
class Menu:

    BANNER_FILE_PATH = "media/menu/banner.txt"
    OPTIONS_FILE_PATH = "media/menu/options.txt"
    fwBanner = FileWrapper(BANNER_FILE_PATH)
    options = Options()

    def showMenu(self):
        self.fwBanner.printFile(False)
        #self.
        #print(hasattr(options.Options, "simple_td_t1_t2")) #check if this module have this function
        #bar = getattr(options.Options, "simple_td_t1_t2")  #run modules function
        #bar()
        pass
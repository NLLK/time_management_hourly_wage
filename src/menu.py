from src.fileWrapper import FileWrapper

class Menu:

    BANNER_FILE_PATH = "media/menu/banner.txt"
    fwBanner = FileWrapper(BANNER_FILE_PATH)

    def showMenu(self):
        self.fwBanner.printFile(False)
        #print(hasattr(options.Options, "simple_td_t1_t2")) #check if this module have this function
        #bar = getattr(options.Options, "simple_td_t1_t2")  #run modules function
        #bar()
        pass
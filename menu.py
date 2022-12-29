import options

class Menu:
    def showMenu():
        print(hasattr(options.Options, "simple_td_t1_t2")) #check if this module have this function
        bar = getattr(options.Options, "simple_td_t1_t2")  #run modules function
        bar()
        pass
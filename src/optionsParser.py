import options

class OptionsParser:

    SYMBOL_COMMENT = '#'
    SYMBOL_FUNCION = '>'
    SYMBOL_DESCRIPTION = '\"'

    SYMBOLS_LIST = \
                    [   
                        SYMBOL_COMMENT, #comment. We write in python, aren't we?
                        SYMBOL_FUNCION, #function name
                        SYMBOL_DESCRIPTION #description
                    ]
    

    def check(self, text):
        #check for wrong symbols
        #check for currect symbol order ([#], >, \n, "")
        return 0

    def parse(self, text:str):
        if self.check(text) != 0:
            return -1

        optionsList: list(options.Options.Option) = []

        currOption: options.Options.Option = options.Options.Option()
        reading_option = False
        for line in text:
            firstSymbol = line[0]
            if firstSymbol in OptionsParser.SYMBOLS_LIST:
                if firstSymbol == OptionsParser.SYMBOL_COMMENT:
                    continue #skip comments
                if firstSymbol == OptionsParser.SYMBOL_FUNCION:
                    #the start of option description. The first line is method name
                    string = line[1:]
                    string.strip()
                    currOption.functionName = string
                    
            

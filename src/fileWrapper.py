class FileWrapper:
    mFile = object

    def __init__(self, filePath) -> None:
        self.mFile = open(filePath, encoding='utf8')
        pass

    def __del__(self):
        self.close()

    def close(self):
        self.mFile.close()

    def readLine(self):
        pass

    def seekToStart(self):
        #self.mFile.seek(0, 0)
        pass

    def printFile(self, skipLine: bool):
        self.seekToStart()

        if (skipLine):
            print()

        for line in self.mFile:
            print(line, end='')  
        
        print()
        pass




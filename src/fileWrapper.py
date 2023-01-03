import os.path

class FileWrapper:

    class FileState:
        FILE_OK = 0
        FILE_IS_NOT_OK = -1

    mFile = object
    fileState = FileState.FILE_OK
    fileIsOk = False
    filePath = ""

    def __init__(self, filePath, mode = 'r') -> None:
        self.filePath = filePath

        try:
            self.mFile = open(filePath, encoding='utf8', mode=mode)
        except OSError as e: 
            print(f'Could not open/read file: {filePath}\nReason {e.strerror}')
            self.changeFileState(FileWrapper.FileState.FILE_IS_NOT_OK)
            #abort
            #TODO: make meaningful return
            return
            
        self.changeFileState(FileWrapper.FileState.FILE_OK)
        pass

    def __del__(self):
        self.close()

    def close(self):
        self.mFile.close()

    def changeFileState(self, state):
        if (state == FileWrapper.FileState.FILE_OK):
            self.fileIsOk = True
        else: 
            self.fileIsOk = False
        
        self.fileState = state

    def readLine(self):
        #TODO: try catch
        return self.mFile.readline()

    def readLines(self):
        #TODO: try catch
        return self.mFile.readlines()

    def readLinesToStr(self):
        return ''.join(self.readLines())

    def seekToStart(self):
        pass

    def printFile(self, skipLine: bool):
        if (skipLine):
            print()
            
        #TODO: try catch
        for line in self.mFile:
            print(line, end='')  
        
        print()
        pass




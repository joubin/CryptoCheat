import sys, os, gzip

class MakeWordList():
    """
    Given a path to a wordlist, make a small and portable dictionary and save it in the extras folder.

    I got my list from []
    """
    def __init__(self, path):
        self.path = path
        self.rawData = None
        self.writePath = os.path.dirname(os.getcwd())
        self.extras = self.writePath+'/extras'
        if not os.path.exists(self.extras):
            os.makedirs(self.extras)
        self.__read()
        self.__makeZip()


    def __read(self):
        with open(self.path) as rawFile:
            self.rawData = rawFile.read().split()

        self.rawData = list(set(self.rawData))



    def __makeZip(self):
        with gzip.open(self.extras+'/words.gzip', 'w') as zipFile:
            zipFile.write(str(self.rawData))



if __name__ == "__main__":
    path = raw_input('Print provide a path to your world list: ').strip()
    go = MakeWordList(path)


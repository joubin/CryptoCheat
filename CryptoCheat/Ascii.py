import string

class Ascii:
    """
    This class will figure out a strin of ascii char into a string. 

    Right now I am not taking into considiration ascii vales 1 and 10-19
    """
    def __init__(self, anInput):
        self.ascii = anInput
        self.string = ''
        self.clean = ''
        self.final = ''
        self.__splitToGroupsOfAscii()
        self.__buildString()

    def __mapAsciiToChar(self, ascii):
        return chr(ascii)
        
    def __splitToGroupsOfAscii(self):
        if isinstance(self.ascii, list):
            self.ascii = ''.join([str(i) for i in self.ascii]) # incase you are given an array of ascii chars
            return
        temp = self.ascii
        letters = []
        self.clean = []

        for i in temp:
            letters.append(i)

        while len(letters) != 0:
            string = ''
            if int(letters[0]) == 1:
                for i in range(0,3):
                    string += str(letters.pop(0))
            else:
                for i in range(0,2):
                    string += str(letters.pop(0))
            self.clean.append(int(string))
            string = ''


    def __buildString(self):
        for i in self.clean:
            self.final += self.__mapAsciiToChar(i)

    def get(self):
        print self.clean
        return self.final




test = Ascii('32321041011081083232111')
print test.get()
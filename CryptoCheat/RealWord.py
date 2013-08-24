import gzip, sys, os

class RealWord:
    
    def __init__(self, word):
        self.WordsToTest = word.lower().split()
        self.KnownWords = None
        self.writePath = os.path.dirname(os.getcwd())
        self.extras = self.writePath+ os.sep + 'extras'
        self.wordList = self.extras+ os.sep +'words.gzip'
        try:
            with gzip.open(self.wordList, 'rb') as wordList:
                self.KnownWords = wordList.read()
        except Exception, e:
            print e
            print "Seems like you've deattached the original word list. No matter. run MakeWordList.py and get a basic Word list and Ill clean it up"
            sys.exit(1)



    def RealOrNot(self):
        score = 0
        for word in self.WordsToTest:
            if word in self.KnownWords:
                score += 1
            else:
                score -= 1


        if score > .7: # If 70% of the words in the original sentance is are real words, then it is safe to assume that the other 30% are names or acrynoms. Change this value if you dont agree. 
            return True
        else: 
            return False


if __name__ == '__main__':
    check = RealWord('hello')

    print check.RealOrNot()
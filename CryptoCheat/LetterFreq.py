import string, operator
from RealWord import RealWord

class LetterFreq:
    def __init__(self, text):
        self.text = text.lower()
        self.alphabet = string.lowercase
        self.alphabetUpper = string.uppercase
        self.textLetters = {}
        self.textFreqOrdered = []
        self.punctuation = set(string.punctuation)
        self.freqSets = {
        'press': 'ETAONISRHLDCMUFPGWYBVKJXQZ', 
        'wikipedia': 'ETAOINSHRDLCUMWFGYPBVKJXQZ', 
        'scientific': 'ETAIONSRHLCDUMFPGYBWVKXQJZ', 
        'english': 'ETAOINSRHLDCUMFPGWYBVKXJQZ', 
        'oxford': 'EARIOTNSLCUDPMHGBFYWKVXZJQ', 
        'averages': 'ETAOINSRHLDCUMFPGWYBVKXJQZ', 
        'religious': 'ETIAONSRHLDCUMFPYWGBVKXJQZ', 
        'fiction': 'ETAOHNISRDLUWMCGFYPVKBJXZQ'
        }
        self.rots = []
        self.__CreateAlphabetSet()
        self.__rot()

    
    def __CreateAlphabetSet(self):
        
        for i in self.alphabet:
            self.textLetters[i] = 0
        
        for i in self.text:
            if i != ' ' and i not in self.punctuation:
                self.textLetters[i] = self.textLetters[i] + 1

        self.textFreqOrdered = sorted(self.textLetters.iteritems(), key=operator.itemgetter(1), reverse=True)

                
    def CompareFreq(self):
        for k,v in self.freqSets.items():
            temp = self.text
            for i in xrange(len(v)):
                self.textLetters[self.textFreqOrdered[i][0]] = v[i]

            for i in temp:
                if i != ' ' and i not in self.punctuation:
                    temp = temp.replace(i, self.textLetters[i])
            testWord = RealWord(temp)

            if testWord.RealOrNot() == True:
                return temp.lower()
            else:
                continue


    def __rot(self):
        end = 25
        start = 0
        for i in range(26):
            temp = ''
            for x in range(i,26):
                temp += self.alphabetUpper[x]
            for x in range(0,i):
                temp += self.alphabetUpper[x]
            self.rots.append(temp)

    def BruteForce(self):
        count = 0
        for i in self.rots:
            temp = self.text
            for x in xrange(26):
                self.textLetters[self.alphabet[x]] = i[x]

            for ii in temp:
                if ii != ' ' and ii not in self.punctuation:
                    temp = temp.replace(ii, self.textLetters[ii])

            testWord = RealWord(temp)

            if testWord.RealOrNot() == True:
                return temp.lower()

            count += 1

    def get(self):
        if self.CompareFreq() != None:
            return self.CompareFreq()
        else:
            return self.BruteForce()




    
if __name__ == '__main__':
    words = "yvtug gb vafcver rguavp qvfpevzvangvba naq qevir gur Puvarfr njnl. Nf gur lrnef cnffrq, n envyebnq jnf perngrq bire cnegf bs gur Puvangbja naq shegure cbyvgvpf naq ynjf jbhyq znxr vg rira uneqre sbe Puvarfr jbexref gb fhfgnva n yvivat va Fnpenzragb. Juvyr gur rnfg fvqr bs gur pbhagel sbhtug sbe uvture jntrf naq srjre jbexvat ubhef, znal pvgvrf va gur jrfgrea Havgrq Fgngrf jnagrq gur Puvarfr bhg orpnhfr bs gur oryvrs gung gurl jrer fgrnyvat wbof sebz gur juvgr jbexvat pynff. Gur Puvarfr erznvarq erfvyvrag qrfcvgr gurfr rssbegf. Gurl ohvyg gurve ohvyqvatf bhg bs oevpxf whfg nf gur ohvyqvat thvqryvarf rfgnoyvfurq. Gurl urycrq ohvyq cneg bs gur envyebnqf gung fcna gur pvgl nf jryy nf znxvat n terng pbagevohgvba gb gur genafpbagvaragny envyebnq gung fcnaf gur Havgrq Fgngrf. Gurl nyfb urycrq ohvyq gur yrirrf jvguva Fnpenzragb naq gur fheebhaqvat pvgvrf. Nf n erfhyg, gurl ner n jryy-erpbtavmrq cneg bs Fnpenzragb'f uvfgbel naq urevgntr."
    print LetterFreq(words).get()







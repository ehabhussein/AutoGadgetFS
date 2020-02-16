import random

class Probability():

    def getdifflist(self,full,thelist):
        return list(set(full) - set(thelist))

    def getcharset(self):
        for word in self.readwords:
            for char in word.strip():
                if char not in self.charset:
                    self.charset.append(char)
        self.discardedcharset = self.getdifflist(self.fullkeyboard,self.charset)

    def getcase(self,char):
                if char.isupper():
                    return "U"
                elif char.islower():
                    return "l"
                elif char.isdigit():
                    return "n"
                elif not char.isupper() and not char.islower() and not char.isdigit():
                    return "@"
                else:
                    pass

    def getindexes(self):
        for word in self.readwords:
            word = word.strip()
            self.word_dct[word] = []
            for index,char in enumerate(word.strip()):
                if char.isupper():
                    self.countUpper+=1
                    self.word_dct[word] += 'U'
                    if index not in self.alphaupperindexes:
                        self.alphaupperindexes.append(index)
                elif char.islower():
                    self.countLower +=1
                    self.word_dct[word] += 'l'
                    if index not in self.alphalowerindexes:
                        self.alphalowerindexes.append(index)
                elif char.isdigit():
                    self.countDigits +=1
                    self.word_dct[word] += "n"
                    if index not in self.integerindexes:
                        self.integerindexes.append(index)
                elif not char.isupper() and not char.islower() and not char.isdigit():
                    self.countOther +=1
                    self.word_dct[word] += '@'
                    if index not in self.nonalphanumindexes:
                        self.nonalphanumindexes.append(index)
                self.frequencies[char] = self.frequencies.get(char, 0) + 1
        self.finalcharset = self.getdifflist(self.fullkeyboard,self.discardedcharset)
        self.maxcombinationwordsgenerator = len(self.finalcharset) ** len(self.unusedindexes)

    def frequency_index_vertical(self):
        self.word_list_v = list()
        self.analysis_dct_v = dict()
        for key, val in list(self.word_dct.items()):
            self.word_list_v += [val]
        for l in self.word_list_v:
            for i, w in enumerate(l):
                if not self.analysis_dct_v.get(i):
                    self.analysis_dct_v[i] = dict()
                    if not self.analysis_dct_v[i].get('U'):
                        self.analysis_dct_v[i]['U'] = 0
                    if not self.analysis_dct_v[i].get('l'):
                        self.analysis_dct_v[i]['l'] = 0
                    if not self.analysis_dct_v[i].get('n'):
                        self.analysis_dct_v[i]['n'] = 0
                    if not self.analysis_dct_v[i].get('@'):
                        self.analysis_dct_v[i]['@'] = 0
                self.analysis_dct_v[i][w] += 1

    def frequency_index_horizontal(self):
        self.word_list_h = list()
        self.analysis_dct_h = dict()
        for key, val in list(self.word_dct.items()):
            self.word_list_h += [val]
        for w in self.readwords:
            word = w.strip()
            if not self.analysis_dct_h.get(word):
                self.analysis_dct_h[word] = dict()
                if not self.analysis_dct_h[word].get('U'):
                    self.analysis_dct_h[word]['U'] = 0
                if not self.analysis_dct_h[word].get('l'):
                    self.analysis_dct_h[word]['l'] = 0
                if not self.analysis_dct_h[word].get('n'):
                    self.analysis_dct_h[word]['n'] = 0
                if not self.analysis_dct_h[word].get('@'):
                    self.analysis_dct_h[word]['@'] = 0
            for char in word:
                if char.isupper():
                    self.analysis_dct_h[word]['U'] += 1
                elif char.isdigit():
                    self.analysis_dct_h[word]['n'] += 1
                elif char.islower():
                    self.analysis_dct_h[word]['l'] += 1
                elif not char.isupper() and not char.islower() and not char.isdigit():
                    self.analysis_dct_h[word]['@'] += 1


    def PrefinalAnalysis(self):
        self._charRelationMatrix= dict()
        self.wordweight = dict()
        self.maxweight = 0
        self.cweight = dict()
        for word in self.readwords:
            word = word.strip()
            for i, c in enumerate(word.strip()):
                if not self._charRelationMatrix.get(i):
                    self._charRelationMatrix[i] = dict()
                if not self._charRelationMatrix[i].get(c):
                    self._charRelationMatrix[i][c] = 0
                self._charRelationMatrix[i][c] += 1
        for word in self.readwords:
            word = word.strip()
            if not self.cweight.get(word):
                self.cweight[word] = dict()
            word = word.strip()
            for i, c in enumerate(word):
                if not self.cweight[word].get(c):
                    self.cweight[word][c] = dict()
                if not self.cweight[word][c].get(i):
                    self.cweight[word][c][i] = 0
                self.cweight[word][c][i] += self._charRelationMatrix[i][c]
        for word in self.readwords:
            word = word.strip()
            for i, c in enumerate(word):
                self.maxweight += self.cweight[word][c][i]
            self.maxweight = 0

        if not self.wordweight.get(word):
            self.wordweight[word] = dict()


    def charswithfriendswithwords(self):
        self.charRelationMatrix= dict()
        for word in self.readwords:
            word = word.strip()
            self.charRelationMatrix[word]= dict()
            for i, c in enumerate(word):
                if not self.charRelationMatrix[word].get(c):
                    self.charRelationMatrix[word][c] = dict()
                    self.charRelationMatrix[word][c] = ([z for z,l in enumerate(word) if l == c])


    def smartGenerator(self):
        self.maxweight = 0
        genIndex = list(range(len(max(self.readwords, key=len).strip())))
        self.smartDict = dict()
        self.strippedReadWords = []
        self.genList = ["" for i in genIndex]
        for word in self.readwords:
            word = word.strip()
            for i,c in enumerate(word):
                if not self.smartDict.get(c):
                    self.smartDict[c] = dict()
                if not self.smartDict[c].get(i):
                    self.smartDict[c][i] = dict()
                for ind, ch in enumerate(word):
                    if not self.smartDict[c][i].get(ind):
                        self.smartDict[c][i][ind] = set()
                    self.smartDict[c][i][ind].add(ch)
        indx = random.choice(genIndex)
        genIndex.remove(indx)
        self.genList[indx] = random.choice(list(self._charRelationMatrix[indx].keys()))
        while genIndex:
            indx = random.choice(genIndex)
            randomC = random.choice(list(self._charRelationMatrix[indx].keys()))
            for i, c in enumerate(self.genList):
                if c:
                    if randomC in self.smartDict[c][i][indx]:
                        self.maxweight += self._charRelationMatrix[indx][randomC]
                        self.genList[indx] = randomC
                        genIndex.remove(indx)
                        break
                    else:
                        break
        for word in self.readwords:
            self.strippedReadWords.append(word.strip())
        if "".join(self.genList) in self.strippedReadWords:
            pass
        else:
            if "".join(self.genList) not in self.packets:
                self.packets.append("".join(self.genList))

    def patterngenerator(self):
        self.maxweight = 0
        self.threshold = 0
        self.firstchoice = ""
        genIndex = list(range(len(max(self.readwords, key=len).strip())))
        self.smartDict = dict()
        self.strippedReadWords = []
        self.genList = ["" for i in genIndex]
        self.wordpattern =  list(self.word_dct.values())
        for word in self.readwords:
            word = word.strip()
            for i,c in enumerate(word):
                if not self.smartDict.get(c):
                    self.smartDict[c] = dict()
                if not self.smartDict[c].get(i):
                    self.smartDict[c][i] = dict()
                for ind, ch in enumerate(word):
                    if not self.smartDict[c][i].get(ind):
                        self.smartDict[c][i][ind] = set()
                    self.smartDict[c][i][ind].add(ch)
        self.randompattern = random.choice(self.wordpattern)
        while not self.firstchoice:
            indx = random.choice(genIndex)
            self.firstchoice = random.choice(list(self._charRelationMatrix[indx].keys()))
            if self.getcase(self.firstchoice)== self.randompattern[indx]:
                genIndex.remove(indx)
                self.genList[indx] = self.firstchoice
            else:
                self.firstchoice = ""
        while genIndex:
            if self.threshold == 1000:
                    return
            self.threshold += 1
            indx = random.choice(genIndex)
            randomC = random.choice(list(self._charRelationMatrix[indx].keys()))
            for i, c in enumerate(self.genList):
                if c:
                    if randomC in self.smartDict[c][i][indx] and (self.getcase(randomC) == self.randompattern[indx]):
                        self.maxweight += self._charRelationMatrix[indx][randomC]
                        self.genList[indx] = randomC
                        genIndex.remove(indx)
                        break
                    else:

                        break
        for word in self.readwords:
            self.strippedReadWords.append(word.strip())
        if "".join(self.genList) in self.strippedReadWords:
            pass
        else:
            if "".join(self.genList) not in self.packets:
                self.packets.append("".join(self.genList))


    def randomgenerator(self):
        self.tokens = []
        self.newWord = []
        self.maxweight = 0
        self.genWord = ''
        self.strippedReadWords = []
        self.counter = 0
        for word in self.readwords:
            self.strippedReadWords.append(word.strip())
        while(True):
            self.counter +=1
            if self.counter == self.howmany:
                break
            self.genWord = ''
            for i in range(len(self.unusedindexes)):
                self.genWord += (random.choice(list(self._charRelationMatrix[i].keys())))
            if self.genWord in self.strippedReadWords:
                pass
            else:
                self.newWord.append(self.genWord)
        for word in self.newWord:
            self.packets.append(word)
            for i, c in enumerate(word):
                self.maxweight += self._charRelationMatrix[i][c]
            self.maxweight = 0



    def printgeneralstats(self):
        print("\n\n[+]General Statistics")
        print("Full charset                :",''.join(sorted(self.fullkeyboard)))
        print("Discarded charset           :",''.join(sorted(self.discardedcharset)))
        print("Final charset               :", ''.join(sorted(self.finalcharset)))
        print("Word Length                 :",len(self.unusedindexes))
        print("Lower Case index usage      : %d%%"%(100 * len(self.alphalowerindexes)/len(self.unusedindexes)))
        print("Lower Case index locations  :",sorted(self.alphalowerindexes))
        print("Upper Case index usage      : %d%%"%(100 * len(self.alphaupperindexes)/len(self.unusedindexes)))
        print("Upper Case index locations  :",sorted(self.alphaupperindexes))
        print("Digit index usage           : %d%%"%(100 * len(self.integerindexes)/len(self.unusedindexes)))
        print("Digit index locations       :",sorted(self.integerindexes))
        print("NonAN index usage           : %d%%"%(100 * len(self.nonalphanumindexes)/len(self.unusedindexes)))
        print("NonAN index locations       :",sorted(self.nonalphanumindexes))
        print("Counter statistics          : Uppercase: %d , Lowercase: %d, Digits:%d , NonAlphaNumeric:%d" %(self.countUpper ,self.countLower ,self.countDigits , self.countOther))
       # print("All char Frequencies        : (\'Found Character\'  Repeated How many Times)")
       # for i in (str(sorted(list(self.frequencies.items()), key=lambda x: x[1])).replace("[","").replace("]","").split(",")):
       #     print(i.strip(), end=' ')



    
    


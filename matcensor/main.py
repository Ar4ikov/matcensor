CensorList = eval(open('mat_off/badlist.json', 'r').read())
CensorList = CensorList['badwords'].split(', ')
IgnoreList = eval(open('mat_off/ignorelist.json', 'r').read())
IgnoreList = IgnoreList['ignorelist'].split(', ')

from re import sub as repl

__version__ = '1.0.0'

class MatProtect():

    def __init__(self):
        self.alphabet = ["ф", "пи", "ш", "й","п",
                         "ё", "щ", "ю", "я", "л",
                         "ж", "ц", "ч", "н", "а",
                         "б", "о", "р", "с", "т",
                         "в", "у", "и", "х", "к",
                         "м", "ъ", "ы", "ь", "г",
                         "д", "э", "е", "з"]

        self.slogs = {
            'уу': ['уй', 'уи'],
            'оо': ['о'],
            'цоц': ['сос']
        }

        self.replaceSymols = {
            "а": ["@","a"],
            "б": ["b","6"], "и": ['\|',"u","i","1"],  "р": ["p",'r'], "ш": ["sh",'iii'],
            "в": ["v","b"], "й": ['iy'], "с": ["s",'c'], "щ": ["sh","sh'"],
            "г": ["g"],     "к": ["k"],      "т": ["t"],     "ъ": [],
            "д": ["d"],     "л": ["l",'jl'], "у": ["u",'y'], "ы": [],
            "е": ["e"],     "м": ["m"],      "ф": ["f",'ph'],"ь": [],
            "ё": ["yo"],"н": ["n"],  "х": ["><","h",'x'], "э": [],
            "ж": ["zh", "j"],"о": ["o",'0'], "ц": ["ts",'c'],"ю": ["you"],
            "з": ["z", "3"],"п": ["p", 'ii'], "ч": ["ch",'4'], "я": ["ya"], 'пи': ['3.14']
        }

    def converStr(self,word=None):
        word = repl('\-', '', word)
        word = repl('\_', '', word)
        word = repl('\!', '', word)
        word = repl('\#', '', word)
        word = repl('\%', '', word)
        word = repl('\^', '', word)
        word = repl('\(', '', word)
        word = repl('\)', '', word)
        word = repl('\$', '', word)
        word = repl('\&', '', word)

        return word

    def checkSymbols(self, word=None, libwords=None):
        libword = list(libwords)
        self.symblos = '*'
        for sybmol in list(self.symblos):
            for i in range(0,len(libword)):
                libword = list(libwords)
                libword[i] = sybmol
                if word.count("".join(libword)):
                    return True
        return False

    def replaceSyms(self,word=None):
        for sym in self.alphabet:
            sym_res = self.replaceSymols[sym]
            sym_res = sorted(sym_res, key=sortMethods.sortByLength, reverse=1)
            self.replaceSymols[sym] = sym_res
        for sym in self.alphabet:
            for vars in self.replaceSymols[sym]:
                word = repl(vars, sym, word)

        for slog in self.slogs.keys():
            for slog_repl in self.slogs[slog]:
                word = repl(slog, slog_repl, word)

        return word

    def updateDB(self,db=None,word=None):
        if db == None or word == None:
            return {'status': False, 'error': 'Вы не указали ни одной базы/не было указано слова для внесения'}

        try:
            openList = eval(open('mat_off/'+db+'.json').read())
        except:
            return {'status': False, 'error': 'Данная база не найдена, достуные: ignorelist, badwords'}
        else:
            global IgnoreList
            if word in IgnoreList:
                return {'status': False, 'error': 'Такое слово уже есть в базе данных.'}

            openList[db] = openList[db] + ", " + word

            closeList = open('mat_off/'+db+'.json', 'w')
            closeList.write(str(openList))
            closeList.close()

            CensorList = eval(open('mat_off/badlist.json', 'r').read())
            CensorList = CensorList['badwords'].split(', ')

            IgnoreList = eval(open('mat_off/ignorelist.json', 'r').read())
            IgnoreList = IgnoreList['ignorelist'].split(', ')

            return {'status': True, 'message': 'База данных обновлена и перезагружена!'}

    def checkCensor(self,obj='',split_param=' '):
        splited_list = obj.lower().split(split_param)
        badwords = []
        for word in splited_list:
            word = self.converStr(word)
            if word in IgnoreList:
                break
            if word in CensorList:
                badwords.append(word)
            else:
                word = self.replaceSyms(word=word)
                #print(word)
                if word in CensorList:
                    badwords.append(word)
                else:
                    for mat in CensorList:
                        if word.count(mat):
                            badwords.append(word)
                            break
                        else:
                            response = self.checkSymbols(word=word,libwords=mat)
                            if response == True:
                                badwords.append(word)
                                break
        if len(badwords) > 0:
            return {'status': True, 'badwords': badwords}
        else:
            return {'status': False}

class AntiFlood:
    def __init__(self):
        pass

class sortMethods:
    def sortByLength(inputStr):
        return len(inputStr)
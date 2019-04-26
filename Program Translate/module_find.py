#!/usr/bin/env python3
# Module find word

import listfile as fileloc
import module_history as modHist

def main(word):
    char_word = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    inword_lst = list(word.lower())
    if word == "":
        return None
    if inword_lst[0] in char_word:
        word = word.lower()
        a = Findword(word)
        return a.find()
    else:
        return None

class Findword(object):
    def __init__(self, word):
        self.inword = word
        self.id = None
        self.word = None
        self.wmean = None
        self.group = None
    def find(self):
        openfile = open(fileloc.FOLDER_WORD+self.inword[0]+".txt", "r",encoding="utf8")
        i = 0;
        for line in openfile:
            if i == 0:
                i += 1
                continue
            line = line.split(";")
            line[2] = line[2].replace("\n", "")
            list_word = list(line[1])
            list_word[0] = list_word[0].upper()
            full_word = "".join(list_word)
            self.id = line[0]
            self.word = line[1].lower()
            self.wmean = line[2]
            #self.group = line[3]
            if self.word == self.inword:    # เงื่อนไขเมื่อ ข้อมูลในไฟล์ = ข้อมูลเข้า
                hist = modHist.main()
                hist.add(self.word)
                hist.addhist(self.inword)
                return self.wmean
        openfile.close()
        return None

if __name__ == '__main__':
    main()
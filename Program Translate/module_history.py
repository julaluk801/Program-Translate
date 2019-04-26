#!/usr/bin/env python3
# Module check file of word

import listfile as fileloc
from operator import itemgetter
import datetime

def main():
    return History()

class History(object):
    def __init__(self):
        self.word = None
        self.rank = None
    def add(self, word):
        openfile = open("history.txt", "r+", encoding="utf8")
        for line in openfile:
            list_line = line.split(";")
            if list_line[0] == word:
                pre_edit = ("%s;%s" % (list_line[0], list_line[1]))
                post_edit = ("%s;%s\n" % (list_line[0], (int(list_line[1])+1)))
                change = open("history.txt", encoding='utf8').read().replace(pre_edit, post_edit)
                f = open("history.txt", 'w', encoding="utf8")
                f.write(change)
                f.close()
                openfile.close()
                return
        self.word = word
        self.rank = "1"
        openfile.write("%s;%s\n" % (self.word.lower(), self.rank))
        openfile.close()
    def top(self):
        rank_list = []
        openfile = open("history.txt", "r")
        for line in openfile:
            list_line = line.split(";")
            try:
                score = list_line[1].replace("\n", "")
            except IndexError:
                break
            rank_list.append([list_line[0], score])
        openfile.close()
        for i in rank_list:
            i[1] = int(i[1])
        rank_list = sorted(rank_list, key=itemgetter(1), reverse=True)
        print(rank_list)
        return rank_list
#-------------------------------------------------------------------------------------#
    def addhist(self, word):    
        list_openfile = []
        openfile = open("historyword.txt", "r")
        for line in openfile:
            list_openfile.append(line.split(";"))
        openfile.close()
        for i in range(len(list_openfile)):
            if list_openfile[i] == "":
                list_openfile.pop(i)
            if word == list_openfile[i][0]:
                list_openfile[i][1] = str(datetime.datetime.now()).strip('datetime.datetime')+"\n"
                self.addhist_(list_openfile)
                return
        list_openfile.append([word, (str(datetime.datetime.now()).strip('datetime.datetime')+"\n")])
        self.addhist_(list_openfile)
    def addhist_(self, list_openfile):
        clearfile = open("historyword.txt", "w+")
        clearfile.close()
        openfile = open("historyword.txt", "a+")
        for i in list_openfile:
            openfile.write(i[0]+";"+i[1])
        openfile.close()

#-------------------------------------------------------------------------------------#
    def check(self, word):
        openfile = open("historyword.txt", "r")
        for line in openfile:
            if line == word+"\n":
                return True
            else:
                return False
        openfile.close()
    def printhist(self):
        list_openfile = []
        openfile = open("historyword.txt", "r")
        for line in openfile:
            list_openfile.append(line.split(";"))
        openfile.close()
        list_openfile = sorted(list_openfile, key=itemgetter(1), reverse=True)
        return list_openfile
    def print(self):
        openfile = open("history.txt", "r")
        for line in openfile:
            linenew = line.split(";")
            print(linenew[0])
        openfile.close()
    def clear(self):
        openfile = open("history.txt", "w+")
        openfile.close()
        openfile = open("historyword.txt", "w+")
        openfile.close()

if __name__ == '__main__':
    main()
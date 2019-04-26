#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Module add word for new word

import listfile as fileloc

def main():
    w_word = input("Word: ")
    w_mean = input("Mean: ")
    w_group = int(input("Group: "))
    add = Addword(w_word, w_mean, w_group)
    add.add()

class Addword(object):
    def __init__(self, word, word_mean, group):
        self.id = None
        self.word = word
        self.wmean = word_mean
        self.group = group
    def add(self):
        split_first_word = list(self.word)
        self.checkID(split_first_word)
        openfile = open(fileloc.FOLDER_WORD+split_first_word[0].upper()+".txt", "a")
        openfile.write("%d;%s;%s;%s\n" % (self.id, self.word.lower(), self.wmean, self.group))
        openfile.close()
        print("Add word %s: Completed" % self.word)
    def checkID(self, split_word):
        openfile = open(fileloc.FOLDER_WORD+split_word[0]+".txt", "r")
        for line in openfile:
            self.id = int(line) + 1
            break
        with open(fileloc.FOLDER_WORD+split_word[0]+".txt") as f:
            lines = f.readlines()
        lines[0] = str(self.id)+"\n"
        with open(fileloc.FOLDER_WORD+split_word[0]+".txt", "w") as f:
            f.writelines(lines)
        print(self.id)
        openfile.close()

if __name__ == '__main__':
    main()
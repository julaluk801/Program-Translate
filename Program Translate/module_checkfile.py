#!/usr/bin/env python3
# Module check file of word

import listfile as fileloc

def main():
    print("Start operation: Checkfile")
    checkfile = Checkfile()
    checkfile.checkFile()

class Checkfile(object):
    def __init__(self):
        self.filelist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    def checkFile(self):
        for i in self.filelist:
            openfile = open(fileloc.FOLDER_WORD+i+".txt", "r+",encoding="utf8")
            for line in openfile:
                if line == "":
                    openfile.write("0\n")
                break
            openfile.close()
            print("Check file %s: Founded" % i)

if __name__ == '__main__':
    main()
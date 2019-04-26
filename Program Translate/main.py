#!/usr/bin/env python3
# Module check file of word

# Main of Program
import listfile as fileloc
import module_addword as modAddword
import module_checkfile as modCheckfile
import module_find as modFind
import module_history as modHist

def main():
    print("Start Computer Dictionary")
    print("-------------------------------------------------------")
    print("Staus: checking file")
    st_modCheckfile = modCheckfile.main()
    if st_modCheckfile:
        print("Status: check file Completed")
    else:
        print("Status: check file Error")
    print("Program ready to use")
    print("-------------------------------------------------------")
    while True:
        print("Key for control program")
        print("a = add new word")
        print("f = find word")
        print("h = show history")
        print("ht = show top history")
        print("esc = escape program")
        key_input = input("key: ")
        print("-------------------------------------------------------")
        hist = modHist.main()
        if key_input == "a":
            modAddword.main()
        elif key_input == "f":
            modFind.main()
        elif key_input == "h":
            hist.print()
        elif key_input == "ht":
            hist.top()
        elif key_input == "esc":
            break
        else:
            continue
        print("-------------------------------------------------------")

if __name__ == '__main__':
    main()
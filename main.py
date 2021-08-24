'''
Word Plot
Version 1.0.0

Copyright (C) 2021 Shahibur Rahaman
Licensed under GNU GPLv3
'''

import wordplot
import time
import sys
import matplotlib.pyplot as plt


def  main():
    to_user()
    try:
        while True:
            print("\n> ", end="")
            word = input("Word to be plotted: ").lower()
            if word == "exit;":
                print("Exiting...")
                time.sleep(2)
                sys.exit()
            elif word == "license;":
                show_license()
            else:
                for letter in word:
                    wordplot.plot(letter)
                plt.show()

                wordplot.clear_plots()
    except KeyboardInterrupt:
        print("\nForced Exiting...\n")


def show_license():
    with open("LICENSE", "r") as main_license:
        print(main_license.read())


def to_user():
    print('''
+-------------------------------------------------+
| Welcome to Word Plotter                         |
| Version: 1.0.0                                  |
|                                                 |
| Copyright (C) 2021 Shahibur Rahaman             |
|                                                 |
| For more info and updates visit:                |
| https://github.com/Shahibur50/Word_Plot         |
|                                                 |
| This program comes with ABSOLUTELY NO WARRANTY. |
|                                                 |
| Type "exit;" to exit the program                |
| Type "license;" to see the license              |
+-------------------------------------------------+
''')


if __name__ == "__main__":
    main()

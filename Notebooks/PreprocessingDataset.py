import os
from tkinter import filedialog
#Get folder containing the dataset
def getFolder():
    dirname = filedialog.askdirectory(title='Please select the folder containing the dataset.')
    return dirname

#Change structure so that every
def changeDirectoryStructure():
    dirname = getFolder()
    train_dir = str(dirname) + "/train"
    test_dir = str(dirname) + "/test"
    val_dir = str(dirname) + "/valid"

    print(train_dir)
    print(test_dir)
    print(val_dir)


def main():
    changeDirectoryStructure()

if __name__ == "__main__":
    main()
    
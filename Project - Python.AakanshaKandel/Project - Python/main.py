import usrInput 
import parseFile 

def errorHandle(checkReturn):
    """Handles error conditions returned by checkPath(). 
    If checkReturn is 1 or had a empty list, no valid JSON files 
    were found and the program exists. """

    if checkReturn == 1:
       print("Invalid Path")
       exit()
    if not checkReturn:
       print("No valid files to process.")
       exit() 

def startProcess(tup): 
    """Processes all valid files returned by checkPath, loads raw employee data, validates, cleans it 
    and writed in into a formatted file. It also keeps tracks of how many JSON 
    files were processed and how many employee entries were processed into the 
    new formatted file."""

    numFiles = len(tup)
    numEmps = 0 
    for filePath in tup:
        raw = parseFile.getJSONContent(filePath)
        cleaned = parseFile.processEachEmp(raw) 

        parseFile.generateFormattedFile(cleaned, filePath)
        numEmps += len(cleaned)

    printOutput(numFiles, numEmps)

def printOutput(numFiles, numEmps): 
    """Prints out the str of the number of files processed and 
    "the number of valid employee entries. """

    print("Number of files processed " + str(numFiles))
    print("Number of employee entries " + str(numEmps))

def main():
    """Prompts the user to write a file or directory name,
    checksPath, formats, cleans and outputs new formatted json file,
    by calling numerous function from main.py and usrInput.py"""

    filePath = usrInput.getUsrInput("Enter a file or directory name: ")
    validFiles = usrInput.checkPath(filePath, [])
    errorHandle(validFiles)
    startProcess(validFiles)

if __name__ == "__main__": 
   main()




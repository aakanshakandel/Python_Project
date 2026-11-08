import os 
valid_files = []
def checkPath(filePath, dataFiles):
    """Checks the filepath and ensures that only json files are processed, 
    and already formatted.jason files are skipped."""

    if not os.path.exists(filePath):
        print(filePath + " does not exist.")
        return 1
    elif os.path.isdir(filePath):
        for file in os.listdir(filePath):
            checkPath(os.path.join(filePath, file), dataFiles)
    elif filePath.endswith("_formatted.json"):
        pass
    elif filePath.lower().endswith(".json"):
        dataFiles.append(filePath)
    else: 
        pass
    return tuple(dataFiles) 

def getUsrInput(msg): 
    """Returns what the user wrote when prompted."""
    return input(msg + "")
    

#pick out the formatted.jason, then if it ends with jason then process it. 


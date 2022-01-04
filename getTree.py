import os,os.path;

def safeListDir(path):
    try:
        return os.listdir(path)

    except:
        return []

def getAllFolders(path):
    List=[]
    for i in safeListDir(path):
        cp=path+'/'+i#;print(cp)
        if os.path.isdir(cp)==True:
            List.append(cp)

    return List

def getAllChildFolders(path):
    doneList=[]
    noneList=[]
    noneList.extend(getAllFolders(path))
    while len(noneList)!=0:
        currentList=getAllFolders(noneList[0]);doneList.append(noneList[0])
        noneList.remove(noneList[0]);noneList.extend(currentList)

    return doneList

def getAllChildFilesByFormat(path,formats):
    Folders=getAllChildFolders(path)
    List=[]
    for i in Folders:
        List.extend(getAllFilesByFormat(i,formats))

    return List

def getAllFilesByFormat(path,formats):
    List=[]
    for i in safeListDir(path):         
        cp=path+'/'+i
        if os.path.isfile(cp)==True:          
            if i.split('.')[-1] in formats or len(formats)==0:
                List.append(cp)
                
    return List

#output=getAllChildFilesByFormat('/home/frnr/Music',['mp3'])





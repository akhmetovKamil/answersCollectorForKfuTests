import json
import os

fileName = open("name.txt","r").readline()
fileName = fileName[::-1][2:][::-1]
#fileName = os.getenv('currentEnvVar')
FileNameWithoutHtml = fileName[:-5] if fileName[-1]=='l' else fileName[:-4]
with open("merged.json",'r', encoding='utf-8') as f:
    mergedJson = json.load(f)

with open(FileNameWithoutHtml+".json",'r', encoding='utf-8') as f:
    oldJson = json.load(f)

newJson = {"Elements": list()}

def copyMainJson(mergedJson):
    for i in range(len(mergedJson["Elements"])):
        tempDict=dict()
        tempDict["Number"] = mergedJson["Elements"][i]["Number"]
        tempDict["Question"] = mergedJson["Elements"][i]["Question"]
        tempDict["Answer"] = mergedJson["Elements"][i]["Answer"]
        newJson["Elements"].append(tempDict)
        
copyMainJson(mergedJson)
def checkCopies(question,answer):
    for i in range(len(mergedJson["Elements"])):
        if question==mergedJson["Elements"][i]["Question"]:
            if answer==mergedJson["Elements"][i]["Answer"]:
                return 0
    return 1

lastNumber = newJson["Elements"][-1]["Number"]+1 if len(newJson["Elements"])!=0 else 1
k=0
for i in range(len(oldJson["Elements"])):
    if checkCopies(oldJson["Elements"][i]["Question"],oldJson["Elements"][i]["Answer"]):
        tempDict=dict()    
        tempDict["Number"]=lastNumber+k
        tempDict["Question"] = oldJson["Elements"][i]["Question"]
        tempDict["Answer"] = oldJson["Elements"][i]["Answer"]
        newJson["Elements"].append(tempDict)
        k+=1

with open('merged.json', 'w',encoding="utf-8") as f:
        json.dump(newJson, f, indent=4, ensure_ascii=False)
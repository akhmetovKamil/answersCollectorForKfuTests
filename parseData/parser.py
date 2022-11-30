from bs4 import BeautifulSoup
import codecs
import json
import re
import os

fileName = open("name.txt","r").readline()
#fileName = os.getenv('currentEnvVar')
fileName = fileName[::-1][2:][::-1]
with codecs.open(fileName, "r", "utf_8_sig" ) as htmFile:
    file = htmFile.read()

toJson = {"Elements" : list()}

soup = BeautifulSoup(file,"lxml")
ans_list = soup.find_all("div", class_="que multichoice deferredfeedback complete")

correct_ans_list=list()
for i in range(len(ans_list)):
    grade = ans_list[i].find(class_="grade").string
    grade_list = re.findall(r'\d+', grade)
    state = (grade_list[0]==grade_list[2] and grade_list[1]==grade_list[3])
    if state:
        correct_ans_list.append(ans_list[i])

for i in range(len(correct_ans_list)):
    question = correct_ans_list[i].find("div",class_="formulation clearfix").find("input").find_next_sibling().text
    answer = correct_ans_list[i].find("div",class_="ablock no-overflow visual-scroll-x").find("input",{"checked":"checked"}).find_next_sibling().next_element
    if len(answer.text)<=3 and answer.text[-1]==" ":
        answer = answer.find_next_sibling().text
    else:
        answer=answer.text
    tempDict=dict()
    tempDict["Number"]=i+1
    tempDict["Question"]=question
    tempDict["Answer"]=answer
    toJson["Elements"].append(tempDict)
    
jsonFileName = fileName[:-5] if fileName[-1]=='l' else fileName[:-4]

with open(jsonFileName+".json", 'w',encoding="utf-8") as f:
        json.dump(toJson, f, indent=4, ensure_ascii=False)
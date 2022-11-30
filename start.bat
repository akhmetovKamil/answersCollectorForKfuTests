@echo off
chcp 1251
SetLocal EnableDelayedExpansion


rem Создаем пустой merged.json с разметкой, к которому будем приклеивать все последующие json файлы
cd mergedJSON
del *.json
Set createdMergedFile=merged.json
(
echo {
echo     "Elements": [
echo.        
echo     ]
echo }
)>>"%createdMergedFile%"
cd ..\
del answers.json

rem Копируем все файлы из папки files в главную директорию, чтобы дальше работать с копиями
cd files
for %%i IN (*.html  *.htm) do (
    set fn=%%i
    copy !fn! ..\
)
cd ..\


rem Проходимся циклом по всем html,htm файлам и с каждым запускаем parser.py,mergeJSON.py
for %%i IN (*.html	*.htm) do (
    set fn=%%i
    cd parseData
    call echo !fn! >> "name.txt"
    cd ..\
    move !fn! parseData
    cd parseData
    python parser.py
    del *.html
    del *.htm
    move name.txt ..\mergedJSON
    move *.json ..\mergedJSON
    cd ..\mergedJSON
    python mergeJSON.py
    del name.txt
    cd ..\
)


rem Удаляем ненужные файлы и выводим итоговый answers.json в главную директорию
cd mergedJSON
rename merged.json answers.json
move answers.json ..\
del *json


cls
echo Ready
pause
exit
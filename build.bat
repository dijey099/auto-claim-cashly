@echo off
color 0a

title Build - Auto Claim
mode con:cols=100 lines=220
cls
pyinstaller -c -i icon.ico --clean -F cashly.py
pause
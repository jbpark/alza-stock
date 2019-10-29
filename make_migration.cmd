@echo off
cmd /k "cd /d D:\Anaconda3 & conda activate py35 & cd /d D:\jbdesk\Dropbox\jbmini\project\my\stock\alza-stock & python manage.py makemigrations & python manage.py migrate"
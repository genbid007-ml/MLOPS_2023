This is experimantal MLOPS pipeline

Initial steps
Krish MLOPS pipeline:

https://github.com/genbid007-ml/MLOPS_2023

create a blank env in GitHub and create a folder in your local directory.

Enter into the directory and start vs code by code .

in vs code open command prompt in the new terminal

Create env : conda create -p venv python==3.8 -y
Activate the env: conda activate venv/
conda activate D:\00_Project\MLOPS_2023\venv

cannot push to main branch
(D:\00_Project\MLOPS_2023\venv) D:\00_Project\MLOPS_2023>git push -u origin dev 
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 246 bytes | 246.00 KiB/s, done.      
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
remote: 
remote: Create a pull request for 'dev' on GitHub by visiting:    
remote:      https://github.com/genbid007-ml/MLOPS_2023/pull/new/dev
remote:
To https://github.com/genbid007-ml/MLOPS_2023
 * [new branch]      dev -> dev
branch 'dev' set up to track 'origin/dev'.

Synch with github:
git init
create README.md at local repo
git commit -m "first commit"
git branch -M dev
git remote add origin https://github.com/genbid007-ml/MLOPS_2023
git push -u origin dev 






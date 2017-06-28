#-*- coding: UTF-8 -*-
#添加git仓库
git init#在当前路径下生成.git文件（路径中不能有中文）
#在git中添加文件
git add learngit.py
#在git中提交文件到仓库
git commit -m "wrote a learnfile"
#查看git状态
git status
git diff learngit.py
git diff HEAD -- learngit.py  #查看工作区版本和版本库中文件区别
#查看git日志
git log [--pretty=oneline]
#回退git版本
git reset --hard HEAD^  #上一个版本是HEAD^,上上个版本是HEAD^^,上100个版本HEAD~100
#查看git操作历史
git reflog
#撤销修改
git checkout -- learngit.py #回退到上一次add或commit(使用暂存区覆盖本地内容)
git reset HEAD learngit.py #回到上一次commit(使用版本库覆盖暂存区内容)
#删除文件
git rm test.txt #删除工作区与暂存区的文件
git commit -m "remove test.txt" #将删除提交
git checkout -- test.txt #还原删除文件

#远程仓库
ssh-keygen -t rsa -C "youremail@example.com" #在主目录下生成.ssh与公私钥
git remote add origin git@github.com:USERNAME/REPONAME.git#add repo后将本地关联到远程仓库
git push -u origin master#首次推送使用-u，将本地分支推送至远程，并将本地master与远程master关联起来
git push origin master #推送最新修改

#分支管理
git checkout -b dev #创建并切换至dev分支(= git branch dev + git checkout dev)
git branch #查看当前分支
git remote -v #查看远程分支
git checkout master #切换回master分支
git merge dev #将dev分支合并至当前分支
git branch -d dev #合并完成后删除dev分支
#当需要merge的分支与master分支冲突时,需要手动打开文件,修改冲突后再add commit


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
git log #[--pretty=oneline]只显示一行[--graph]开头字符显示分支变化情况[--abbrve-commit]只显示版本号的前几位


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
git checkout -b dev #创建并切换至dev分支(= git branch dev 创建 + git checkout dev 切换)
git branch #查看当前分支
git remote -v #查看远程分支
git checkout master #切换回master分支
git merge dev #将dev分支合并至当前分支
git branch -d dev #合并完成后删除dev分支
#当需要merge的分支与master分支冲突时,需要手动打开文件,修改冲突后再add commit
git merge --no-ff -m "merge with no-ff" dev#使用--no-ff模式保留合并分支时的信息

#bug分支
git stash #储存当前分支的工作区
git checkout master #切换回master分支
git checkout -b issue-101 #新建bug分支issue-101
git checkout master #修改完成后切换回master分支
git merge --no-ff -m "merged bug fix 101" #合并修改到master并保留信息
git checkout dev #切换回工作分支
git stash list  #查看保存的stash
git stash pop stash@{0}  #将stash@{0}还原到工作现场（=git stash apply 还原 + git stash drop 删除）

#feature分支
git branch -D feature-vulcan #删除一个修改过但未合并的分支

#多人协作
git push origin branch-name  #将本地分支推送至远程分支
#抓取分支
git clone [address] #clone远程master分支
git checkout -b dev origin/dev # 抓取远程dev到本地
#与他人冲突
git pull #获取远程最新代码，本地修改解决冲突后 再行commit push
git branch --set-upstream branch-name origin/branch-name #关联本地分支与远程分支


#打tag
git tag <name> <commit_id> #不填写commit_id默认使用当前最新版本打tag
git tag  #查看所有tag （列出的tag按字母排序）
git show <name> #查看tag具体信息
git tag -a <name>  -m <message> <commit_id>  #-a可以指定标签信息
git tag -s <name>  -m <message> <commit_id>  #-s可以用PGP签名标签(做不到)
#删tag 与 推送tag
git tag -d v0.1  #删除本地tag v0.1
git push origin v0.1 #推送tag v0.100
git push origin --tags #一次性推送所有tag
git push origin :refs/tags/v0.1 #删除本地tag后操作，将远程tag也删除

#自定义Git
#建.gitignore文件，写入需要被忽略的文件 参考：https://github.com/github/gitignore
git add -f learngit.py  #强制添加被忽略的文件
git check-ignore -v learngit.py #检查learngit.py被忽略的原因
git config --global alias.st status #使用st代替status
git config --global alias.unstage 'reset HEAD'  #使用unstage代替reset HEAD
git config --global alias.lg "log --color --graph --pretty=foramt:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrve-commit"
#git的设置存放在.git/config中，全局设置则放在主目录下的.gitconfig中

#搭建git服务器
sudo apt-get install git #通过apt-get安装git
sudo adduser git #新增用户git，以运行git服务
#将所有用户的公钥id_rsa.pub 导入/home/git/.ssh/authorized_keys，一行一个
sudo git init --bare sample.git #在/srv目录下初始化一个git裸仓库sample.git，用户无法登录服务器更改裸仓库，将owner改为git
#安全性方面 禁用shell登录，将/etc/passwd 中"git:x:1001:1001:,,,:/home/git:/bin/bash"改为"git:x:1001:1001:,,,:/home/git:/usr/bin/git-shell"
git clone git@sercer:/srv/sample.git #可以通过git clone 克隆远程仓库了
#管理公钥可使用Gitosis,严格权限控制可使用Gitolite

#注，git官网：http://git-scm.com
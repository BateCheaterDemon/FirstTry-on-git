# Git
SSH/Git+Gitee/Tmux分享 结合VS code

下载代码：

git init

git clone XXX --depth 10 or 100 #(如果代码过大，需要这样)

git submodule update --init --recursive #对于很久的分支，需要这个更新子模块 大公司使用的坑

git status #查看状，确定是否有没有track的子模块



git config --global user.email "XXX"

git config --global user.name "XXX"

查看谁修改了：vscode gitgraph

![image-20241216162118348](C:\Users\BateCheaterDemon\AppData\Roaming\Typora\typora-user-images\image-20241216162118348.png)



git checkout -b [name] #新建分支



git add [file] #暂存修改 git add .

git commit -m "[name]" 提交分支



#发布到远端

git push

 git push --set-upstream origin [XXX]

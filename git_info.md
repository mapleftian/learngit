###git使用说明

1、添加文件，示例，新建readme.txtw文件

```git
Git is a version control system.
Git is free software.
```

2、用命令git add告诉Git，把文件添加到仓库

```git
git add readme.txt
```

3、用命令git commit告诉Git，把文件提交到仓库

```git
git commit -m "wrote a readme file
```

4、add可以添加多个文件，commit一次提交这些文件

5、通过如下命令来查看更新历史记录

```
git log --pretty=oneline test.txt
```

6、使用git reset命令进行版本回退，-x ，x代表回退到前几个版本

```
git reset --hard HEAD-1
```

7、使用git reflog用来记录你的每一次命令

8、使用git status 查看当前git暂存区到状态

9、使用git rm删除git中的文件

10、使用git checkout -- 还原

11、将本地库文件所有内容连接并推送到远程库上

```git
$ git remote add origin git@github.com:michaelliao/learngit.git
$ git push -u origin master 
$ git push origin master
#后续提交
```

12、git pull origin <branch name>同步远程库内容

13、git push origin <branch name> 本地推送到主分支上

14、创建与合并分支
	查看分支：git branch

	创建分支：git branch <name>
	
	切换分支：git checkout <name>
	
	创建+切换分支：git checkout -b <name>
	
	合并某分支到当前分支：git merge <name>
	
	删除分支：git branch -d <name>

15、第一次关联远程库

	要关联一个远程库，使用命令git remote add origin git@server-name:path/repo-name.git；

	关联后，使用命令git push -u origin master第一次推送master分支的所有内容；

	此后，每次本地提交后，只要有必要，就可以使用命令git push origin master推送最新修改；
	

[参考文档地址](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/0013760174128707b935b0be6fc4fc6ace66c4f15618f8d000)
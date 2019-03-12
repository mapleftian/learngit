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


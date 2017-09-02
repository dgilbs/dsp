# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

* show current working directory path: pwd
* creating a directory: mkdir (name)
* deleting a directory: rmdir (name)
* creating a file using `touch` command: touch (name)
* deleting a file: rm (name)
* renaming a file: mv (filename) (new filename)
* listing hidden files: ls -a
* copying a file from one directory to another: cp (filename) (directory)
* returning to the previous directory: cd ..
* open a file: open (filename)
* open a file in Sublime: subl (filename)
* open a whole folder in Sublime: subl *


---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

* `ls`: lists files and directories
* `ls-a`: lists all entries including those starting with a period
* `ls -l`: displays the long format (permissions, links, owner, group, size, time, name)
* `ls -lh`: lists the long format with unit suffixes
* `ls -lah`: lists the long format of all files, including hidden ones, with unit suffixes
* `ls -t`: lists files in the order of time modified, with the most recently modified being listed first
* `ls -Glp`: lists the long format of files with a slash and a different text color for directories

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

* `ls -c`: displays filename with time stamp
* `ls -g`: displays long format without the owner name
* `ls -R`: displays subdirectories as well
* `ls -m`: displays names as a comma-seperated list
* `ls -1`: displays each entry on a line

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs will execute the same command on a number of different items. For instance, if I wanted to use the "cat" command to show all the contents of every .md file in the dsp folder, I can type "ls *.md | xargs cat" and it will list all those files and display their contents

 


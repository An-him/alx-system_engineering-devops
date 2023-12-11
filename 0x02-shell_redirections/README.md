Shell, I/O Redirection
What do the commands head, tail, find, wc, sort, uniq, grep, tr do
How to redirect standard output to a file
How to get standard input from a file instead of the keyboard
How to send the output from one program to the input of another program
How to combine commands and filters with redirections

Special Characters
What are special characters
Understand what do the white spaces, single quotes, double quotes, backslash, comment, pipe, command separator, tilde and how and when to use them

Other Man Pages
How to display a line of text
How to concatenate files and print on the standard output
How to reverse a string
How to remove sections from each line of files
What is the /etc/passwd file and what is its format
What is the /etc/shadow file and what is its format

SCRIPTS AND MEANING/DESCRIPTIONS
0-hello_world
	script that prints “Hello, World”, followed by a new line to the standard output.
1-confused_smiley
	script that displays a confused smiley "(Ôo)'.
2-hellofile
	script that Display the content of the /etc/passwd file.
3-twofiles
	script that displays the content of /etc/passwd and /etc/hosts
4-lastlines
	Display the last 10 lines of /etc/passwd
11-directories
	 a script that counts the number of directories and sub-directories in the current directory.
	The current and parent directories should not be taken into account
	Hidden directories should be counted
12-newest_files
	a script that displays the 10 newest files in the current directory.
	Requirements:
	One file per line
	Sorted from the newest to the oldest
14-findthatword
	Display lines containing the pattern “root” from the file /etc/passwd
15-countthatword
	Display the number of lines that contain the pattern “bin” in the file /etc/passwd
16-whatsnext
	Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.
17-hidethisword
	Display all the lines in the file /etc/passwd that do not contain the pattern “bin”.
20-hiago
	 a script that removes all letters c and C from input.
21-reverse 
	 a script that reverse its input.
8-cwd_state
	script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it 		should be overwritten. If the file ls_cwd_content does not exist, create it.

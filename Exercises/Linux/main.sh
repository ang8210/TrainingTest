# (1) Print out the current directory on the terminal
pwd

# (2) Check whether the file (hello.sh) exists in this directory
#     - True： do (3)
#     - False： Print out "No file!" on the terminal
if [ -f ./'hello.sh' ];then
	cat hello.sh
else
	echo "NO file!"
fi

# (3) Print out the file (hello.sh) content on the terminal

# (4) In order to execute the file (hello.sh) to change the file permission
#     - change the the file permission
#     - execute the file
chmod +x hello.sh
./hello.sh

# (5) Create a new directory name is Byebye and move hello.sh into Byebye
mkdir Byebye
mv hello.sh /home/angela/Desktop/Test/Byebye

# (6) Delete the directory name is Byebye
rm -r Byebye

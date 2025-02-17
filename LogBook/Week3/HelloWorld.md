### Hello World from the Terminal

#### Creating the folder


1. Create a new temporary folder on the Linux machine

   *mkdir tmp*

2. Change into it

   *cd tmp*

3. Clone the repo into this folder

   *git clone https://github.com/etc*


#### Hello World - Python


1. Use nano to create a Python "Hello World" program.

   *$ nano hello.py*

2. Save the program, and run it.

   *python3 hello.py*

3. As python is interpreted, we may need to check the file commands and change them, and re-run

   *$ ls -l hello.py*
   *$ chmod 700 hello.py*
   *$ ./hello.py*

4. We can then finish this by committing to our Git repo

   *$ git add hello.py*
   *$ git commit -m "My Python Program"*


#### Hello World - Java

Instead of being interpreted line by line like Python, instead Java of compiled and executed. Therefore we must remember to have our java classes named the same as our file, as to avoid an error

1. First create the Java file.

   *$ javac Hello.java*

2. Then create the java program.

   *You know what a java hello world print statement is Kane*

3. Then run the program.

   *$ java Hello*


#### Hello World - C

1. First, create C file to store the program

   *$ pico Hello.c*

2. Then, write the hello world program in the file

   *#include <stdio.h>
   main()
   {
   printf(“Hello World!\n”);
   }*

3. Then compile the script so that it is executable

   *$ gcc hello.c*

4. Now we can run the script

   *$ ./a.out*
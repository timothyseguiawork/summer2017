/*
  Program 3: HelloWorldArgs
  07.17.17
*/

/*
  This program will receive 2 bits of data and store them in the second argument, argv.
  argc is an automatically calculated value that represents the total number of arguments stored in argv.
*/

#include <stdio.h>

int main(int argc, char **argv){
  int i;
  for (i=0; i<argc; i++){
    printf("Hello World! argc=%d arg %d is %s\n", argc, i, argv[i]);
  }
  return 0;
}
/*
C:\summer2017\c2017>gcc 03_HelloWorldArgs.c

C:\summer2017\c2017>a.exe hello world
Hello World! argc=3 arg 0 is a.exe
Hello World! argc=3 arg 1 is hello
Hello World! argc=3 arg 2 is world

This shows that the count (argc) of arguments is 3 even though I have only passed 2 arguments.
That's sbecause the program name itself, a.exe is automatically passed as the first argument.
The first argument here has the index number 0, index 1 (hello), index 2 (world)

Notice the two asterisks before argv are important.
char **argv
They indicate that argv is a list of strings. Strictly speaking argv is an 'argument' vector
*/

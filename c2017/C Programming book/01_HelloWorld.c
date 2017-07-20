/*
  Program 1, HelloWorld.c
  07.17.17
*/

#include <stdio.h> // This is a preprocessor directive
//<> around the file name tells the compiler to search for that file in the C 'system' directory.

int main(int argc, char **argv){ // main is the name of the function that runs when the program starts.
  // () after main shows that this is a function with no arguments.
  printf("hello world\n"); //semicolon terminates a statement
  // hello world is a string of charcters passed between () to the printf function and \n displays a new line.
  // printf is a function in 'stdio.h'
  return 0;
}
// this main function is a function that returns an integer.
// this program also includes two arguments

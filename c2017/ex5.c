/*
1.5 Symbolic Constants
07.19.17
*/

#include <stdio.h>
// #define line defines a symbolic name or symbolic constant.
#define name "replacement text"
// the replacement text can be anything, from numbers to characters.
#define LOWER 0 // lower limit of table
#define UPPER 300 // upper limit of table
#define STEP 20 // step size

/* print Fahrenheit-Celsius table */
main(){
  int fahr;
  printf("Fahrenheit-Celsius Table\n");
  for (fahr = LOWER; fahr <= 300; fahr = fahr +20){
    printf(" %3d %6.1f\n", fahr, (5.0/9.0)*(fahr-32));
  }
}

/*
1.4 The For Statement
07.19.17
*/

#include <stdio.h>
/* Print fahrenheit-celsius table */
main(){
  int fahr;
  int reverse;
  // The for statement is a loop, a generalization of the while.
  printf("Fahrenheit-Celsius Table\n");
  for (
    /* the initialization is done once before the loop is propery entered */
    fahr = 0;
    /* this is the condition that controls the loop */
    fahr <= 300;
    /* this condition is evaluated; if it is true, the body of the loop is executed
    else, the loop terminates */
    fahr = fahr + 20
  ){
    printf("%3d %6.1f\n", fahr, (5.0/9.0)*(fahr-32));
  }
  printf("\n");

  // Exercise 1-5. Modify the temp conversion program to print the table in
  // reverse order from 300 to 0.
  printf("Exercise 1-5: Fahrenheit-Celsius Table Reversed\n");
  for (reverse = 300; reverse >= 0; reverse = reverse - 20){
    printf("%3d %6.1f\n", reverse, (5.0/9.0)*(reverse-32));
  }
}

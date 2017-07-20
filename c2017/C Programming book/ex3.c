//Variables and Arithmetic Expressions
//07.18.17

#include <stdio.h>

/*
print Fahrenheit-Celsius table
for fahr = 0, 20, ..., 300.
This is a comment which is ignored by the compiler.
*/

main(){
  /*
    In c, all variables must be declared before they are used, usually at the beginning of the function before
    any executable statements. A declaration announces the properties of variables; it consist sof a type
    name and al ist of variables such as
          int fahr, celsius;
          int lower, upper, step;

    int means that the variables listed are integers.
    float means that they are floating point (fractional).
    C also includes:
          char
          short
          long
          double
  */
  int fahr, celsius;
  /*
    for more accurate results use:
    float fahr, celsius;
    in order to use float arihmetic and negate truncation.
  */
  int lower, upper, step;
  /*
    These are assignment statements, which set the variables to their initial values. Individual statements are terminated by semi-colons.
  */
  lower = 0; //Lower limit of the temp table
  upper = 300; //Upper limit
  step = 20; //Step size

  fahr=lower;
  printf("Fahrenheit-Celsius Table\n"); //exercise 1-3
  while (fahr <= upper){
    /*
      Multiply by 5 and then divide by 9 rather than multiply by 5/9 because everything truncates when it comes down to integer arithmetic.
      printf("%3d %6d\n", fahr, celsius);
      Printing the first number of each line in a field 3 digits wide, and the second in a filed six digits wide.
      printf("%3f %6.1f\n", fahr, celsius)
      same as the last print statement, allows for the printing of that .0 decimal.
    */
    celsius = 5 * (fahr-32) / 9;
    printf("%d\t%d\n", fahr, celsius);
    fahr = fahr + step;
  }
  printf("\n");
  fahr=lower; //reset fahr
  celsius=lower; //reset celsius too
  printf("Celsius-Fahrenheit Table\n");
  while (upper >= fahr){
    celsius = 5 * (fahr-32) / 9;
    printf("%d\t%d\n", fahr, celsius );
    fahr = fahr + step;
  }
}

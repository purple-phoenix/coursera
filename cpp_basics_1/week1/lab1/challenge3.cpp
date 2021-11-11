#include <iostream>
using namespace std;

int main(int argc, char** argv) {
  
  string greeting = argv[1];
  string dayOfWeek = argv[2];
  string month = argv[3];
  int day = atoi(argv[4]);
  int currentWaitMinutes = atoi(argv[5]);
  
  //add code below this line

  printf(
    "%s Today is %s, %s %d.\nThe current wait time is %d minutes.",
  greeting.c_str(),
  dayOfWeek.c_str(),
  month.c_str(),
  day,
  currentWaitMinutes);

  //add code above this line
  
  return 0;
  
}


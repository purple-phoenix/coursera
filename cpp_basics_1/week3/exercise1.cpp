#include <iostream>
using namespace std;

int main(int argc, char** argv) {
  
  int x = stoi(argv[1]);
  
  //add code below this line

  if ((x >= 0 && x <=25) || x >= 75 && x <=100) {
    cout << std::to_string(x) + " is between 0 and 25 or 75 and 100" << endl;
  }

  //add code above this line
  
  return 0;
  
}


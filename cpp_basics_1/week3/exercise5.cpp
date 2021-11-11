#include <iostream>
#include <set>
using namespace std;

int main(int argc, char** argv) {
  
  string x = argv[1];
  
  //add code below this line
  std::set<string> mySet {"a", "e", "i", "o", "u"};
  if(mySet.find(x) != mySet.end()){
    cout << x + " is a vowel" << endl;
  }
  else {
    cout << x + " is not a vowel" << endl;
  }

  //add code above this line
  
  return 0;
  
}


#include <iostream>
using namespace std;

int main() {
  
  string num1;
  string num2;
  cout << "Type the first whole number and then press Enter or Return: ";
  cin >> num1;
  cout << "Type the second whole number and then press Enter or Return: ";
  cin >>num2;
  
  //fix the code below this line

  int sum = std::stoi(num1) + std::stoi(num2);
  string sum_str = std::to_string(sum);
  cout << ( num1 + " + " + num2 + " = " + sum_str ) << endl;

  //fix the code above this line
  
  return 0;
  
}


#include <iostream>
#include <string>
using namespace std;

template <typename T>
T addTwo(T a, T b) {
  return a + b;
}

int main() {
  // add two integers
  cout << addTwo(1, 2) << endl;

  // add two doubles
  cout << addTwo(3.2, 1.9) << endl;

  // add two booleans
  cout << addTwo(false, true) << endl;
}

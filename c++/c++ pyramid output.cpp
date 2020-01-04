#include <iostream>

using namespace std;

//
// Write code to draw an
// upside-down pyramid like so..
//
// * * * * 
//  * * *
//   * *
//    *
//
// The size of the pyramid should
// depend on the user input
//
int main() {

  // 1. Get pyramid height from user
  int ROWS;
  cout << "Enter pyramid height: ";
  cin >> ROWS;

  for (int row=0; row < ROWS; row++)
  {
    // 2. Print spaces before left edge
    for (int i=0; i < row; i++) {
        cout << " ";
    }

    // 3. Print asterisks *
    for (int i=0; i < ROWS - row; i++) {
        cout << "* ";
    }

    // 4. Start new line
    cout << endl;
  }

  cout << "Done." << endl;
  return 0;
}

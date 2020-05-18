#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main()
{
    int num, guess;
    srand(time(0)); //seed random number generator
    num = rand() % 100 + 1; // random number between 1 and 100
    cout << "Guess My Number Game\n\n";

    do
    {
        cout << "Enter a guess between 1 and 100 : ";
        cin >> guess;
        
    if (guess > num) {
      cout << "Too high. Try lower" << endl << endl;
    }
    else if (guess < num) {
      cout << "Too low. Try higher" << endl << endl;
    }

    } while ( num != guess );

  cout << "Congrats! You won!" << endl;

    return 0;
}

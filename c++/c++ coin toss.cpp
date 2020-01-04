#include <iostream>

using namespace std;

int main()
{
    bool heads;

    char guess, playAgain;
    while (tolower(playAgain) != 'n')
    {
        system("CLEAR");

        // Make player guess
        cout << "Let's do a coin toss! Guess 'H' for heads or 'T' for tails." << endl << ">> ";
        cin >> guess;
        cout << endl;

        // 'Toss' the coin by generating random number
        // 0 = tails, 1 = heads
        heads = rand() % 2;

        // Check if the player was right
        if (heads && tolower(guess) == 'h') {
            cout << "You won! The coin landed on heads." << endl << endl;
        }
        else if (!heads && tolower(guess) == 't') {
            cout << "You won! The coin landed on tails." << endl << endl;
        }
        else if (heads && tolower(guess) == 't') {
            cout << "Sorry, you lose. The coin landed on heads." << endl << endl;
        }
        else {
            cout << "Sorry, you lose. The coin landed on tails." << endl << endl;
        }

        cout << "Would you like to play again? (y or n)" << endl << ">> ";
        cin >> playAgain;
    }

    return 0;
}

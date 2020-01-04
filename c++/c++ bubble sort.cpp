#include <iostream>
#include <array>
#include <cstdlib>

using namespace std;

//
// Bubble Sort algorithm sorts a list by checking each pair
// pairs are swapped if the first is greater than the second
//
// ex.
//   ( 5, 1, 4, 2 ) –> ( 1, 5, 4, 2 ) - swap first pair
//
//   ( 1, 5, 4, 2 ) –> ( 1, 5, 2, 4 ) - swap last pair
//
// start from beggining again..
//
//   ( 1, 5, 2, 4 ) –> ( 1, 2, 5, 4 ) - swap middle pair
//
//   ( 1, 2, 5, 4 ) –> ( 1, 2, 4, 5 ) - swap last pair
//
void bubbleSort(int *ar, const int &NUM_ITEMS)
{
  // Loop over each item in array
  for (int i=0; i < NUM_ITEMS - 1; i++) {

    // For each item, check all pairs
    for (int j=0; j < NUM_ITEMS - i - 1; j++) {
      
      // Check if first value is greater than second
      if (ar[j] > ar[j + 1]) {
        // swap them
        int temp = ar[j];
        ar[j] = ar[j + 1];
        ar[j+1] = temp;
      }
    }
  }
}

int main()
{
  const int NUM_ITEMS = 4;
  int ar[NUM_ITEMS];

  for (int i=0; i < NUM_ITEMS; i++) {
    cout << "Enter a number: ";
    cin >> ar[i];
  }

  bubbleSort(ar, NUM_ITEMS);

  cout << endl << "Sorted list.." << endl;

  int i=0;
  for (; i < NUM_ITEMS - 1; i++) {
    cout << ar[i] << ", ";
  }
  cout << ar[i] << endl; // last item
}

import java.util.ArrayList;

class Main {
  private static ArrayList<String> farmAnimals = new ArrayList<String>();
  private static ArrayList<String> pets = new ArrayList<String>();

  public static void main(String[] args) {
    farmAnimals.add("cow");
    farmAnimals.add("pig");
    farmAnimals.add("goat");
    farmAnimals.add("dog");
    farmAnimals.add("chicken");
    farmAnimals.add("rabbit");

    System.out.print("farm animals: ");
    printArrayList(farmAnimals);

    System.out.println("\n");

    pets.add("cat");
    pets.add("dog");
    pets.add("bird");
    pets.add("reptile");
    pets.add("fish");
    pets.add("rabbit");

    System.out.print("pets: ");
    printArrayList(pets);

    System.out.println("\n");

    ArrayList<String> animals = mergeArrayLists(farmAnimals, pets);
    System.out.print("animals: ");
    printArrayList(animals);
  }


  private static ArrayList<String> mergeArrayLists(ArrayList<String> list1, ArrayList<String> list2)
  {
    ArrayList<String> result = new ArrayList<String>();

    int size = list1.size();
    if (list2.size() > size) {
      size = list2.size();
    }

    for(int index = 0; index < size; index++) {
      if (index < list1.size() && !result.contains(list1.get(index))) {
        result.add(list1.get(index));
      }
      if (index < list2.size() && !result.contains(list2.get(index))) {
        result.add(list2.get(index));
      }
    }

    return result;
  }

  
  
  private static void printArrayList(ArrayList<String> al) {
    for(String el : al) {
      System.out.print(el+", ");
    }
  }
}

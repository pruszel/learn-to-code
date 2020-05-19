var zodiac = {
  "ox": [1925, 1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021],
  "rat": [1924, 1936, 1948, 1960, 1972, 1984, 1996, 2008, 2020],
  "tiger": [1926, 1938, 1950, 1962, 1974, 1986, 1998, 2010, 2022],
  "rabbit": [1927, 1939, 1951, 1963, 1975, 1987, 1999, 2011, 2023],
  "dragon": [1928, 1940, 1952, 1964, 1976, 1988, 2000, 2012, 2024],
  "snake": [1929, 1941, 1953, 1965, 1977, 1989, 2001, 2013, 2025],
  "horse": [1930, 1942, 1954, 1966, 1978, 1990, 2002, 2014, 2026],
  "goat": [1931, 1943, 1955, 1967, 1979, 1991, 2003, 2015, 2027],
  "monkey": [1932, 1944, 1956, 1968, 1980, 1992, 2004, 2016, 2028],
  "rooster": [1933, 1945, 1957, 1969, 1981, 1993, 2005, 2017, 2029],
  "dog": [1934, 1946, 1958, 1970, 1982, 1994, 2006, 2018, 2030],
  "pig": [1935, 1947, 1959, 1971, 1983, 1995, 2007, 2019, 2031],
};

var $birthday = document.querySelector(".birthday-input");
var $form = document.querySelector(".birthday-form");


function start() {
  console.log("start");
  if (!$birthday) {
    console.log("Error: can't find '.birthday-input'")
    return;
  }
  $birthday.onkeypress = birthdayEnter;
  $form.onsubmit = formSubmit;
}


function getBirthYear() {
  console.log("getting birth year");
  if (!$birthday) {
    return;
  }
  var birthyear = $birthday.value;
  console.log("got", birthyear);
  return parseInt(birthyear);
}


function getZodiacAnimal(year) {
  console.log("searching for year", year);
  for (var animal in zodiac)
  {
    var years = zodiac[animal];

    if (years.includes(year)) {
      console.log("found", animal);
      return animal;
      break;
    }
    console.log("not", animal);
  }
  return "";
}


function setAnswer(animal) {
  if (!animal) {
    return;
  }
  var $answer = document.querySelector(".answer");
  if ($answer) {
    $answer.innerHTML = animal;
  }
}


function highlightAnimal(animal) {
  if (!animal) {
    return;
  }
  // remove highlight from all other animals
  var $animals = document.querySelectorAll(".animal");
  $animals.forEach(function($animal) {
    $animal.classList.remove("active");
  });
  // apply hightlight to given animal
  var $animal = document.querySelector("#"+animal);
  if ($animal) {
    $animal.classList.add("active");
  }
}


function scrollToAnimal(animal) {
  if (!animal) {
    return;
  }
  var $animal = document.querySelector("#"+animal);
  if ($animal) {
    $animal.classList.add("active");
    window.scroll({
      top: $animal.offsetTop - 10,
      left: 0,
      behavior: 'smooth'
    });
  }
}


function formSubmit(e) {
  e.preventDefault();

  console.log("form submit");
  var birthyear = getBirthYear();
  var animal = getZodiacAnimal(birthyear);
  highlightAnimal(animal);
  scrollToAnimal(animal);
}


function birthdayEnter(e) {
  if (!e) e = window.event;
  var keyCode = e.keyCode || e.which;
  if (keyCode == '13') {
    console.log("presed enter");
    formSubmit(e);
  }
}


start();

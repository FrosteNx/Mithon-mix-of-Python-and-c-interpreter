# Język Mithon

Mithon to język programowania zaprojektowany z myślą o prostocie i wszechstronności. Jest to połączenie dobrze znane każdemu programiscie czyli Python oraz Go.

# Przegląd języka

### Typy proste
Mithon udostępnia 4 typy proste:

1. ```int``` - liczby całkowite
2. ```float``` - liczby zmiennoprzecinkowe
3. ```bool``` - wartość logiczna (prawda/fałsz)
4. ```str``` - ciąg znaków (string)

### Typy złożone
Mithon udostępnia także 3 typy złożone:

1. ```List``` Definiuje listę zawierającą elementy danego typu. ```Składnia: List[type]```, gdzie type określa typ elementów listy.

2. ```Matrix``` Definiuje macierz zawierającą elementy danego typu. ```Składnia: Matrix[type]```, gdzie type określa typ elementów macierzy.

Dla typu ```Matrix``` zdefiniowa jest odmienna logika operatorów:
- "+" dodaje do elementów macierzy
- "-" odejmuje od elementów macierzy
- "*" wymnaża elementy macierzy
- "/" dzieli elementy macierzy
Przykład:
```
Matrix[int] m1 = [1,2]
Matrix[int] m2 = [3,4]

Matrix[int] m3 = m1 + m2 // [4,6]
Matrix[int] m4 = m1 - m2 // [-2,-2]
Matrix[int] m5 = m1 * m2 // [3, 8]
Matrix[float] m6 = m1 / m2 // [0.333, 0.5]

Matrix[int] m0 = m1 + 2 // [3,4]
```
##### Uwaga! Operatory działają dla par typów: ```Matrix[typ1], Matrix[typ2] i typ1 == typ2``` lub ```Matrix[typ1], typ2 zmienna i typ1 == typ2```

3. ```Array``` Definiuje tablice o określonym rozmiarze i typie elementów. ```Składnia: Array[size, type]```, gdzie size określa wielkość tablicy, a type określa typ jej elementów.

##### Uwaga! Dla typów złożonych istnieje możliwość indeksacji.
Składnia:
```
complexType[index]
```
Przykład:
```
List[int] l = [1,2,3]
print(l[0])
```

### Zmienne
Deklaracja zmiennych w Mithonie:

1. dla typów prostych:
```
int a = 4
float b = 0.2
bool isActive = false
str name = "Adam"
```

2. dla typów złożonych:
```
List[int] nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Matrix[int] a = [1, 2]
Array[10, int] a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Możliwe jest również nie podawanie prostego typu zmiennej. Mithon wywnioskuje typ na podstawie podanej wartości. 
```
a = 4 <- zmienna a przyjmie typ 'int'
```

### Stałe
Deklaracja stałych odbywa się poprzez podanie słowa kluczowego ```const```. Wartość początkowa musi zostać podana, a raz nadana nie może zostać zmieniona.
```
const int a = 3
```

### Operatory
1. Arytmetyczne
    - Dodawanie ``` + ```
    - Odejmowanie ``` - ```
    - Mnożene ``` * ```
    - Dzielenie ``` / ```
    - Modulo ``` % ```
2. Porównania
    - Równość ``` == ```
    - Nierówność ``` !=  ```
    - Mniejsze ``` < ```
    - Większe ``` > ```
    - Mniejsze lub równe ``` <= ```
    - Większe lub równe ``` >= ```
3. Logiczne
    - Negacja logiczna ```not```
    - Koniunkcja logiczna ```or```
    - Alternatywa logiczna ```and```

4. Przypisania
    - Przypisanie ``` = ```
    - Dodanie i przypisanie ```+=```
    - Odejmowanie i przypisanie ```-=```
    - Mnożenie i przypisanie ```*=```
    - Dzielenie i przypisanie ```/=```

### Instrukcje sterujące
Mithon obsługuje instrukcje ```if```, ```elif``` oraz ```else``` do warunkowego wykonywania kodu:
```
x = 2
if (x > 0) {
    print("x jest dodatnie")
} elif (x < 0) {
    print("x jest ujemne")
} else {
    print("x jest zerowe")
}
```

### Pętle
Język Mithon wspiera trzy rodzaje pętli:

1. Standardowa pętla ```for```.
Składnia:
```
for (typ zmienna = wartość; warunek; krok pętli) {
	ciało pętli
}
```
Przykład:
```
for (int i = 0; i < 5; i += 1){
	print(i)
}
```

2. Zakresowa pętla ```for```.
Składnia:
```
for ([typ] zmienna in zmienna(kolekcja)) {
	ciało pętli
}
```
Przykład:
```
for (int num in nums) {
	print(num)
}
```

3. Pętla ```while```.
Składnia:
```
while (warunek) {
	ciało pętli
}
```
Przykład:
```
int i = 0;
while (i < 10) {
    print(i);
    i = i + 1;
}
```

### Sterowanie przepływem 
W języku Mithon dostępne są również instrukcje break i continue, które umożliwiają sterowanie przepływem pętli.Są to:
1. ```break```

```
for (int i = 0; i < 10; i += 1) {
    if (i == 5) {
	print(i)
        break
    }
    
}

```
2. ```continue```

```
for (int i = 0; i < 5; i += 1) {
    if (i == 3) {
        continue
    }
print(i)
}

```


### Funkcje 
Definicja funkcji wymaga: słowa kluczowego ```def```, następnie nazwy funkcji, następnie listy parametrów (może być pusta) oraz typu zwranego (zapisywanego po ```->```).
Składnia:
```
def nazwa(argumenty) -> typ{
    ciało funkcji
}
```
Uwaga: typ funkcji może przyjąć wartości None <- funkcja nic nie zwraca.

Przykład:
```
// funkcja generująca ilość poprawnych nawiasowań (z wykorzystaniem rekurencji :)):

def generateParenthesis(int n) -> None{

    def dfs(int left, int right, str s) -> None{

        if (len(s) == n * 2){
            print(s)
        }
			
		if (left < n){
			dfs(left + 1, right, s + "(")
        }

		if (right < left){
            dfs(left, right + 1, s + ")")
        }
    }
		
	dfs(0, 0, "")
}
	
generateParenthesis(2)
```

### Funkcje wbudowane
1. Funkcja ```print``` służy do wyświetlania wartości na standardowym wyjściu. Może przyjmować jedną lub więcej wartości jako argumenty, które są następnie wyświetlane w kolejności podanej w wywołaniu funkcji.
Przykładowe użycie:
```
print("Ala", "ma", 2, "koty")
```
Spodziewany output:
```
Ala ma 2 koty
```
2. Funkcja ```len``` zwraca długość ciągu znaków lub kolekcji. ```len("mama")```
3. Funkcja ```append```  dodaje element do listy. ```append(lista, 10)```
4. Funkcja ```sum``` zwraca sumę elementów w liście ```sum(lista)```
5. Funkcja ```min``` zwraca minmalny element w liście ```min(lista)```
6. Funkcja ```max``` zwraca maksymalny element w liście ```max(lista)```
7. Funkcja ```reverse``` odwraca elementy listy ```reverse(lista)```
8. Funkcja ```remove``` usuwa daną wartość z listy ```remove(lista, 2)```. W przypadku takich samych elementów usuwą pierwsze wystąpienie.
9. Funkcja ```pop``` usuwa ostatni element listy ```pop(lista)```
10. Funkcja ```mean``` oblicza średnią typu złożonego ```mean(lista)```
11. Funkcja ```sort```  sortuje w miejscu elementy listy ```sort(lista[, "ascending" lub "descending"])``` (domyślnie ascending)
12. Funkcja ```sorted``` zwraca posortowaną listę jako nowy obiekt ```sorted(lista[, "ascending" lub "descending"])``` (domyślnie ascending)

### Komentarze
Komentarze w języku Mithon poprzedzone są dwoma slashami. Składnia
```
// Komentarz
```

### Przykładowe programy
1.Obliczanie silnii z podanej liczby n:
```
def factorial(int n) -> int {
    if (n == 0) {
        return 1
    } else {
        return n * factorial(n - 1)
    }
}

int n = 5
int result = factorial(n)
print(result)
```

2.Obliczanie n-tego wyrazu ciągu Fibonacciego:
```
def fibonacci(int n) -> int {
    if (n == 0) {
        return 0
    } elif (n == 1) {
        return 1
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2)
    }
}

int n = 6
int result = fibonacci(n)
print(result) 
```
3.Obliczanie NWD:
```
def gcd(int a, int b) -> int {
    while (b != 0) {
        int temp = b
        b = a % b
        a = temp
    }
    return a
}

int a = 56
int b = 98
int result = gcd(a, b)
print(result)
```

4.Sprawdzenie czy liczba jest liczbą pierwszą:
```
def is_prime(int n) -> bool {
    if (n <= 1) {
        return False
    }
    for (int i = 2; i * i <= n; i += 1) {
        if (n % i == 0) {
            return False
        }
    }
    return True
}

int num = 29
bool result = is_prime(num)
print(result)
```

# Instalacja
```
1. git clone git@github.com:FrosteNx/Mithon-mix-of-Python-and-cpp-interpreter.git
2. cd mithon
3. python3 interpreter.py
```

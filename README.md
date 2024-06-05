# Język Mithon

Mithon to język programowania zaprojektowany z myślą o prostocie i wszechstronności. Jest to połączenie dobrze znane każdemu programiscie czyli Python oraz Go.

# Przegląd języka

### Zmienne
Zmienne w Mithon są deklarowane w następujący sposób:
```
[int | float | bool | str] nazwa_zmiennej = wartość
```
Na przykład:
```
int a = 4
bool isActive = false
str name = "Adam"
```
Możliwe jest również nie podawanie typu zmiennej. Mithon sam się domyśli, jaką zmienną zapisałeś
```
a = 4
```

### Stałe

Stałe są deklarowane przy użyciu słowa kluczowego const. Po zadeklarowaniu ich wartości nie można zmieniać.

```
const int a = 3
```
### Operatory
1. Arytmetyczne
    - Dodawanie ``` + ```
    - Odejmowanie ``` - ```
    - Mnożene ``` * ```
    - Dzielenie ``` / ```
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

### Funkcje 

Funkcje są definiowane przy użyciu słowa kluczowego ```def```, po którym następuje nazwa funkcji, lista parametrów oraz typ zwracany pisany po ``` -> ```.

```
def nazwa(argumenty) -> None{
    ciało funkcji
}
```
Przykładowa funkcja generująca ilość poprawnych nawiasowań (z wykorzystanie rekurencji :)):

```
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

### Instrukcje sterujące

Mithon obsługuje instrukcje ```if```, ```elif``` i ```else``` do warunkowego wykonywania kodu

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

### Typy złożone

### Wbudowane funkcje 

Funkcja ```print``` służy do wyświetlania wartości na standardowym wyjściu. Może przyjmować jedną lub więcej wartości jako argumenty, które są następnie wyświetlane w kolejności podanej w wywołaniu funkcji.
Przykładowe użycie:
```
print("Ala", "ma", 2, "koty")
```
Spodziewany output:
```
Ala ma 2 koty
```


# Instalacja
```
1. git clone git@github.com:FrosteNx/Mithon-mix-of-Python-and-cpp-interpreter.git
2. cd mithon
3. python3 interpreter.py
```

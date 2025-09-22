# calculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Division durch Null nicht erlaubt!")
    return x / y


def main():
    print("Einfacher Python-Taschenrechner")
    print("1. Addieren")
    print("2. Subtrahieren")
    print("3. Multiplizieren")
    print("4. Dividieren")

    choice = input("Wähle (1/2/3/4): ")

    try:
        num1 = float(input("Erste Zahl: "))
        num2 = float(input("Zweite Zahl: "))
    except ValueError:
        print("Ungültige Zahl!")
        return

    try:
        if choice == '1':
            print("Ergebnis:", add(num1, num2))
        elif choice == '2':
            print("Ergebnis:", subtract(num1, num2))
        elif choice == '3':
            print("Ergebnis:", multiply(num1, num2))
        elif choice == '4':
            print("Ergebnis:", divide(num1, num2))
        else:
            print("Ungültige Auswahl")
    except ZeroDivisionError as e:
        print("Fehler:", e)


if __name__ == "__main__":
    main()

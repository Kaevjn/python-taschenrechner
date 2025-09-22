def add(x, y): return x + y
def sub(x, y): return x - y
def mul(x, y): return x * y
def div(x, y):
    if y == 0:
        raise ZeroDivisionError("Division durch Null")
    return x / y

if __name__ == "__main__":
    print("Einfacher Taschenrechner")
    a = float(input("Zahl 1: "))
    b = float(input("Zahl 2: "))
    print("Add:", add(a,b))
    print("Sub:", sub(a,b))
    print("Mul:", mul(a,b))
    try:
        print("Div:", div(a,b))
    except ZeroDivisionError as e:
        print("Fehler:", e)
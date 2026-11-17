def fizzbuzz(number):
    digits = str(number)
    result = ""

    if number % 3 == 0:
        result += "Fizz"

    if "3" in digits:
        result += "Fizz"

    if number % 5 == 0:
        result += "Buzz"

    if "5" in digits:
        result += "Buzz"
    
    return result or digits

def main():
    print()
    print("=" * 35)
    print("       F I Z Z B U Z Z")
    print("        CODING DOJO")
    print("          STAGE 2")
    print()
    print("       By Laura Ezpeleta")
    print("=" * 35)
    print()

    for number in range(1, 101):
        print(fizzbuzz(number))

    print()
    print("-" * 35)
    print("  Sequence completed: 1-100")
    print("-" * 35)

if __name__ == "__main__":
    main()
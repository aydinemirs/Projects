def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():
    try:
        number = int(input("Bir sayı girin: "))
        if is_prime(number):
            print(f"Asal")
        else:
            print(f"Asal değil")
                
    except ValueError:
        print("Bir sayı girin")

if __name__ == "__main__":
    main()


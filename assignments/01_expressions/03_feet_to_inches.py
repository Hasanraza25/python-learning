# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

def main():
    feetInput = float(input('Enter Feet: '))
    conversion = 12 * feetInput
    print(f"That is, {conversion}, inches!")


if __name__ == '__main__':
    main()
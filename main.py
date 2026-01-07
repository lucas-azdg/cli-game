import random

def main():
    print("¡Bienvenido al juego 'Adivina el Número'!")
    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Ingresa un número entre 1 y 100: "))
            attempts += 1
            if guess < number:
                print("Demasiado bajo")
            elif guess > number:
                print("Demasiado alto")
            else:
                print(f"¡Correcto! Lo adivinaste en {attempts} intentos")
                break
        except ValueError:
            print("Por favor ingresa un número válido.")

if __name__ == "__main__":
    main()

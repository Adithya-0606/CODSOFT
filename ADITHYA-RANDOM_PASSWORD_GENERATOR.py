import random
import string

def generate_password(length):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Simple Random Password Generator")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            password = generate_password(length)
            print(f"Generated Password: {password}")
        except ValueError:
            print("Invalid input. Please enter a number.")
        
        another = input("Do you want to generate another password? (yes/no): ").lower()
        if another != 'yes':
            print("Thank you for using the password generator. Goodbye!")
            break

if __name__ == "__main__":
    main()

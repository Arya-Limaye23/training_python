import colorama
from colorama import init, Fore, Back, Style
init(autoreset=True)


def menu():
    print(Fore.MAGENTA + '''╔══════════════════════════════════════════════╗
║                                              ║
║        📚  LIBRARY MANAGEMENT SYSTEM  📚     ║
║                                              ║
╚══════════════════════════════════════════════╝''')
    print(Fore.CYAN + "\n1. Add Book\n2. View Books\n3. Search Book\n4. Register User\n5. Issue Book\n6. Exit ")

while True:
    menu()
    choice = input("Enter your choice :: ")
    if choice == "1":
        print("Add Book")
    elif choice == "2":
        print("View Books")
    elif choice == "3":
        print("Search Book")
    elif choice == "4":
        print("Register User")
    elif choice == "5":
        print("Issue Book")
    elif choice == "6":
        print("Thankyou for using our system!! Visit again!")
        break
    else: 
        print(Fore.RED + "Invalid Choice")
        

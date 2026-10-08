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

def read_book():
    with open("book_data.txt", "r") as f:
        book_data = f.readlines
        return book_data

    

def add_book():
    """This is an ADD BOOK Function. It takes name of the book, author and quantity."""
    book_data = read_book()
    print(Fore.GREEN + " --- ADD BOOK ---")
    while True:
       book_id = input("Enter Book ID : ").strip()
       if book_id.isdigit:
          book_id = int(book_id)
          break
       else:
         print(Fore.RED + "Invalid Book ID. It should be NUMBER ONLY.")
       


    book_name = input("Enter Book Name : ")
    book_author = input("Enter Author's Name : ")
    error_message = Fore.RED + "Invalid value. Please enter a valid value"

    
    while True:
        book_quantity = input("Enter Quantity : ")
        if book_quantity.isdigit and int(book_quantity) != 0:
            book_quantity = int(book_quantity)
            break
        else:
           print(error_message)  
    print(Fore.GREEN + f'{"Book added succesfully."}')       
     
    
    with open("book_data.txt", "a") as f:
        f.write(f"{book_id}, {book_name}, {book_author}, {book_quantity} \n")
          
       





while True:
    menu()
    choice = input("Enter your choice :: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        print("View Books")
    elif choice == "3":
        print("Search Book")
    elif choice == "4":
        print("Register User")
    elif choice == "5":
        print("Issue Book")
    elif choice == "6":
        print(Fore.GREEN + "Thankyou for using our system!! Visit again!")
        break
    else: 
        print(Fore.RED + "Invalid Choice")
        

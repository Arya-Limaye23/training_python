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
    with open("data.txt", "r") as f:
     data = f.readlines()
    return data

    

def add_book():
    """This is an ADD BOOK Function. It takes name of the book, author and quantity."""
    data = read_book()
    print(Fore.GREEN + " --- ADD BOOK ---")
    book_name = input("Enter Book Name : ")
    for i in data:
        if book_name in i:
            print(Fore.GREEN + "The book already exists.")
            print(Fore.RED + "Terminating the function")
            return False

    
    gen_id = (len(data) + 1)
    
    print(Fore.CYAN + "Book ID ::", gen_id)
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
     
    
    with open("data.txt", "a") as f:
        f.write(f"{gen_id}, {book_name}, {book_author}, {book_quantity} \n")

def view_book():
    data = read_book()    
    for i in range(len(data)):
        if len(data) == 0:
            print(Fore.RED + "There is no book in database.")
        else:
            print(f"Book ID : {i[0]} | Book Name : {i[1]} | Author : {i[2]} | Quantity : {i[3]}")


# def update_quantity(book_name, new_quantity):
#     data= read_book()
#     total_quantity = 

          
       





while True:
    menu()
    choice = input("Enter your choice :: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        view_book()
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
        

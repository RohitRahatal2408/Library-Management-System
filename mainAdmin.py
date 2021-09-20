from book import Book
from bookMgmt import BookMgmt

def admin():
    bookMgmt = BookMgmt()
    choice = 0

    
    while(choice != 8):
        print('''\t1.Add New Book
    \t2.View All Books
    \t3.Search Book By Id
    \t4.Search Book By Name
    \t5.Search Book By Author
    \t6.Edit Book
    \t7.Delete Book By Id 
    \t8.Exit ''')

        choice = int(input("Enter your choice:"))

        if(choice == 1):
            id = int(input("Enter book id:"))
            name = input("Enter book name:")
            author = input("Enter book author name:")
            b1 = Book(id, name, author)
            bookMgmt.addNewBook(b1)

        elif (choice == 2):
            bookMgmt.showAllBooks()

        elif (choice == 3):
            id = int(input("Enter the book id:"))
            bookMgmt.searchBookById(id)

        elif(choice == 4):
            name = input("Enter book Name:")
            bookMgmt.searchBookByName(name)

        elif (choice == 5):
            author = input("Enter book author name:")
            bookMgmt.searchBookByAuthor(author)
        elif (choice == 6):
            id = int(input(" Enter book id you want to edit:"))
            bookMgmt.editBook(id)

        elif (choice == 7):
            id = input("Enter book id you want to delete:")
            bookMgmt.deleteBookById(id)

        elif(choice==8):
            print("--------Exit--------")

        


if(__name__ == "__main__"):
 admin()

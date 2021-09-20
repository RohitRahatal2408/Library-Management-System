from book import Book
from bookMgmt import BookMgmt


def user():
    bookMgmt = BookMgmt()
    choice = 0

    while (choice != 7):
        print('''\t1.View All Book
    \t2.Search Book By Id
    \t3.Search Book By Name
    \t4.Search Book By Author name
    \t5.Issue Book 
    \t6.Submit Book 
    \t7.Exit ''')

        choice = int(input("Enter your choice: "))

        if (choice == 1):
            bookMgmt.showAllBooks()

        elif (choice == 2):
            id = int(input("Enter the book id you want to search: "))
            bookMgmt.searchBookById(id)

        elif (choice == 3):
            name = input("Enter book Name you want to search:")
            bookMgmt.searchBookByName(name)

        elif (choice == 4):
            author = input("Enter book author name you want to search:")
            bookMgmt.searchBookByAuthor(author)

        elif (choice == 5):
            id = int(input("Enter the book id which you want to issue:"))
            bookMgmt.issueBook(id)

        elif(choice == 6):
            id = int(input("Enter the book id which you want to submit: "))
            bookMgmt.SubmitBook(id)

        elif(choice==7):
            print("--------Exit--------")


if(__name__ == "__main__"):
    user()

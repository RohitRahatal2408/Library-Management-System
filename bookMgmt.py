from book import Book
from datetime import datetime, timedelta

class BookMgmt:

    def addNewBook(self, b1):
        fp = open("bookdata.txt", "a")
        fp.write(str(b1))
        fp.write("\n")
        fp.close

    def showAllBooks(self):
        try:
            fp = open("bookdata.txt", "r")

        except FileNotFoundError:
            print("File not found...")

        else:
            data = fp.read()
            print(data)
            fp.close()

    def searchBookById(self, id):
        with open("bookdata.txt", "r") as fp:
            for line in fp:
                try:
                    line.index(str(id), 0, 3)
                except:
                    pass
                else:
                    print("Book found...")
                    print(line)
                    break
            else:
                print("Book not found...")

    def searchBookByName(self, name):
        found = False
        with open("bookdata.txt", "r") as fp:
            for line in fp:
                if (name in line):
                    found = True
                    print("Book found...")
                    print(line.split())
            if(found == False):
                print("Book is not found...")

    def searchBookByAuthor(self, author):
        found = False
        with open("bookdata.txt", "r") as fp:
            for line in fp:
                if (author in line):
                    found = True
                    print("Book found...")
                    print(line.split())
            if(found == False):
                print("Book is not found...")

    def editBook(self, id):
        myBook = []
        found = False
        with open("bookdata.txt", "r") as fp:
            for line in fp:
                try:
                    line.index(str(id), 0, 3)
                except:
                    pass
                else:
                    found = True
                    line = line.split(",")
                    ans = input("Do you wish to change the name:")
                    if(ans.lower() == "y"):
                        line[1] = input("Enter new name:")
                    ans = input("Do you wish to change the author name:")
                    if(ans.lower() == "y"):
                        line[2] = input("Enter new author name:")
                    line = ",".join(line)
                    line += "\n"

                finally:
                    myBook.append(line)
        print(myBook)
        if(found):
            with open("bookdata.txt", "w") as fp:
                for book in myBook:
                    fp.write(book)
        else:
            print("Book not found...")

    def deleteBookById(self, id):
        myBook = []
        found = False
        with open("bookdata.txt", "r") as fp:
            for line in fp:
                try:
                    line.index(str(id), 0, 3)
                except:
                    myBook.append(line)
                else:
                    found = True
        if(found):
            with open("bookdata.txt", "w") as fp:
                for book in myBook:
                    fp.write(book)
        else:
            print("Book not found..")

    def issueBook(self,id):
        '''Goto bookdata file and check the status, check
        if status is 1, i.e. available, then we can go 
        for issue book'''
        issue = False
        allBooks = []
        with open('bookdata.txt',"r") as fp:
            for line in fp:                
                line = line.split(",")
                if(id == int(line[0])):
                    print("Book Found...")
                    #Book found
                    #Check if available
                    if(int(line[3]) == 1):
                        #Issue book
                        name = input("Enter the student name:")
                        date_of_issue = input("Enter date of issue (dd-mm-yyyy): ")
                        data = str(id)+","+name+","+date_of_issue
                        print("Book Issued...")
                        print("Please submit within 7 days from issue date to avoid late fine: ")
                        with open("bookissue.txt","a") as fp1:
                            fp1.write(data)
                            fp1.write("\n")
                        issue = True    
                        line[3] = "0\n"
                    else:
                        #Book is already issued
                        print("Book is already issued...")
                line = ",".join(line)
                allBooks.append(line)                
            
        #print(allBooks)
        if(issue):
            with open("bookdata.txt","w") as fp:
                for book in allBooks:
                    fp.write(book)
            
                    

    def SubmitBook(self,id):
        issue = False
        allBooks = []
        with open("bookissue.txt", "r") as fp:
            for line in fp:
                line = line.split(",")
                if(id == int(line[0])):
                    print("Issued Book found...")
                    date_of_issue = line[2]
                    date_of_submit = input("Enter date of submit (dd-mm-yyyy): ")
                    date_of_issue = date_of_issue.split("-")
                    year = int(date_of_issue[2])
                    mm = int(date_of_issue[1])
                    dd = int(date_of_issue[0])
                    date_of_issue = datetime(year, mm, dd)

                    date_of_submit = date_of_submit.split("-")
                    year = int(date_of_submit[2])
                    mm = int(date_of_submit[1])
                    dd = int(date_of_submit[0])
                    date_of_submit = datetime(year, mm, dd)
                    diff = (date_of_submit-date_of_issue)
                    print("Issued", diff, "ago")
                    allowed_span = 7  # days

                    if(diff.days > allowed_span):
                        Fine = 50
                        extra_days = (diff.days)-(allowed_span)
                        Total_fine = (Fine)*(extra_days)
                        print("Late Submission Fine applied", Total_fine)
                    else:
                        print("No Fine")

                    issue = True
                else:
                    allBooks.append(line)

        if(issue):
            with open("bookissue.txt", "w") as fp:
                for book in allBooks:
                    fp.write+str(book)

            allBooks = []
            with open("bookdata.txt", "r") as fp:
                for line in fp:
                    try:
                        line.index(str(id), 0, 6)
                    except:
                        pass
                    else:
                        line = line.split(",")
                        line[3] = "1\n"
                        line = ",".join(line)
                    allBooks.append(line)
            with open("bookdata.txt", "w") as fp:
                for book in allBooks:
                    fp.write(book)

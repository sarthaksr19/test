## OrderBook class

class OrderBook:
    def __init__(self,listOfBooks):                 #constructor to instanciate the object.
        self.books = listOfBooks

    def displayAvailableBooks(self):                ## add OrderBook function to display the books list
        print("Books in the library are: ")
        for index,book in enumerate(self.books):    #using enumerate function to print the index as well as name of the books in the list.
            index += 1
            print(f' {index}.{book}',end="")

    def buyBook(self,bookName):                  ## add function to borrowing the book
        if bookName in self.books:                  ##checking the condtion where book is available in the list or not.
            print(f"You have been issued {bookName} Book. Please keept it safe and sell us when you want")
            self.books.remove(bookName)             ## removing the book name which is being issued.
            return True
        else:                                       ## if book is already being issued then this block of code will run.
            print("Sorry! seems like this book is currently sold out. Please try again after someday!")
            return False

    def sellBook(self,bookName):                  ##function for returning/selling the book
        self.books.append(bookName)                 ## add book in the list when student is returnrd the book.
        print(f"Thank You!! You have successfully selled {bookName} Book")

## customer class

class Customer:
    def requestBook(self):
        self.book = input("Enter the name of a book you want: ")
        return self.book                            ## Return self.book value in bookName argument which is in buyBook function.

    def returnBook(self):
        self.book = input("Enter the book name you want to return: ")
        return self.book                            ## Return self.book value in bookName argument which is in sellBook function.

##insantance the object

availableBooks = OrderBook(["Python","Algorithms","JavaScipts","Html","DSA in Python","Chemistry","Physics","Hindi","Python","Java","Java With DSA","Computer IT","Geography","Flamingo",'Vistas'])   
customer = Customer()

## Menu driven
while(True):
    greetmsg = ''' * * * * * WELOCOME TO BOOK ORDERING e-PORTAL * * * * *
        Please Choose an Action:
        Press 1 for List all the Books
        Press 2 for Buying a Book
        Press 3 for Selling a Book
        Press 4 To Exit the Portal'''
    print(greetmsg)
    try:

        a = int(input("Enter the Action: "))

        if a == 1:
            availableBooks.displayAvailableBooks()
        elif a == 2:
            availableBooks.buyBook(customer.requestBook()) 
        elif a == 3:
            availableBooks.sellBook(customer.returnBook())   
        elif a == 4:
            print("Thanks for Visting!!! Have a Nice Day.")
            exit()
            
        else:
            print("You Entered a wrong choice. Please Choose Correct Action")

    except ValueError as e:
        print("You Entered a Wrong Choice.")





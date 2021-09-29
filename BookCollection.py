from BookCollectionNode import BookCollectionNode
from Book import Book
class BookCollection:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None        

    def getNumberOfBooks(self):
        temp = self.head
        count = 0 
        while temp != None:
            count += 1
            temp = temp.getNext()

        return count   
    
    def insertBook(self,book):
        current = self.head
        previous = None
        stop = False

        #Finding the correct place in the list
        while not stop and current != None:
            if current.getData() > book:
                stop = True
            else:
                previous = current   
                current = current.getNext()
        #Create a Node to store item
        temp = BookCollectionNode(book)

        #Case where insert at the front
        if previous == None:
            temp.setNext(self.head)
            self.head = temp

        else: #Case where not insert at front
            temp.setNext(current)
            previous.setNext(temp)

    def getBooksByAuthor(self,author):
        current = self.head
        output = ""

        while current != None:
            if current.getData().getAuthor().upper() == author.upper():
                output += current.getData().getBookDetails() + "\n"
            current = current.getNext()
        return output

    def getAllBooksInCollection(self):
        current = self.head
        output = ""

        while current != None:
            output += current.getData().getBookDetails() + "\n"
            current = current.getNext()
        return output
            


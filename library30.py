#assignment06
class library:
    def __init__(self,book_name,author,availability=True):
        self.book_name=book_name
        self.author=author
        self.availability=availability
    def checkout(self):
        if self.availability==False:
            print(self.book_name,"book has been checked out!!")
        else:
            print("sorry,",self.book_name,"book is not available!!")
    def returnbook(self):
        if self.availability==True:
            print(self.book_name,"book has been returned!!")
        else:
            print(self.book_name,"book is not returned!!")
    def displaybook(self):
        if self.availability:
            status="Available" if self.availability else "not available"
            print("book name:",self.book_name,"author:",self.author,"status:",status)
        
book1=library("Harry Poter","J.K. Rowling")
book2=library("Five Point Someone","Chetan Bhagat")
book1.displaybook()
book1.checkout()
book2.returnbook()
book2.displaybook()

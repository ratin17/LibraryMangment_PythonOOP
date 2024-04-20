
#Entities: Book, User, Library

# Functionalities: adding user, adding books, borrow, return

class Book:
    
    def __init__(self,cat,id,name,quan):
        self.id=id
        self.name=name
        self.cat=cat
        self.quan=quan


class User:
    
    def __init__(self,id,name,password):
        self.id=id
        self.name=name
        self.password=password
        self.borrowedBooks=[]
        self.returnedBooks=[]


class Library:
    
    def __init__(self,owner,name):
        self.owner=owner
        self.name=name
        self.books=[]
        self.users=[]
    
    def addBook(self,cat,id,name,q):
        book=Book(cat,id,name,q)
        self.books.append(book)
        
        print(f"\n\t{name} Book added ! ")
    
    
    def addUser(self,id,name,password):
        user=User(id,name,password)
        self.users.append(user)
        return user
    
    def borrowBook(self,user,id):
        
        for book in self.books:
            if book.id==id:
                if book in user.borrowedBooks:
                    print("\n\tAlready Borrowed ! ")
                    return
                elif book.quan<1:
                    print("\n\tN available Copies ! ")
                    return
                else:
                    user.borrowedBooks.append(book)
                    book.quan-=1
                    print(f"\n\t{book.name} borrowed successfully ! ")
                    return
        
        print(f"\n\tBook not found ! ")
        
    
    
pl=Library("Khurshida Apu","Phitron Library")
admin=pl.addUser(1,'admin','admin')
rahim=pl.addUser(50,'Rahim','1234')
pybook=pl.addBook('Sci-Fi',15,'Dune',5)

run=True
currentUser=admin

while run:
    
    if currentUser == None:
        print(f"\n\tNo logged in user ! ")
        
        option=input("Login ? Registartion (L/R): ")
        
        if option=='R':
            id=int(input("\tEnter id: "))
            name=input("\tEnter Name: ")
            password=input("\tEnter Password: ")
            
            user=pl.addUser(id,name,password)
            currentUser=user
        
        elif option=='L':
            id=int(input("\tEnter id: "))
            password=input("\tEnter Password: ")
            
            match=False
            for user in pl.users:
                if user.id==id and user.password==password:
                    currentUser=user
                    match=True
                    break
            
            if match==False:
                print(f"\n\tNo user found ! ")
            
    
    else:
        
        if currentUser.name=='admin':
            
            print("Options: \n")
            
            print("1 : Add Book")
            print("2 : Show Users")
            print("3 : Show Books")
            print("4 : Logout")
            
            ch=int(input("\nEnter Option: "))
            
            
            if ch==1:
                cat=input("\tEnter Cat: ")
                id=int(input("\tEnter id: "))
                name=input("\tEnter Name: ")
                q=int(input("\tEnter quantity: "))
                
                pl.addBook(cat,id,name,q)
                
            elif ch==4:
                currentUser=None
            
        else:
            print("Options: \n")
            
            print("1 : Borrow Book")
            print("2 : Return Book")
            print("3 : Show Books")
            print("4 : Show Borrowed Books")
            print("5 : Show Returned Books")
            print("6 : Logout")
    
            ch=int(input("\nEnter Option: "))
            
            
            if ch==1:
                id=int(input("\tEnter id: "))
                pl.borrowBook(currentUser,id)





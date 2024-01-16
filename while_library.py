books = []
while True:
    print("-------------Library Mgmt-----------")
    print("1:Add books\n2:Display books\n3:Issue book\n4:Return book\n5:Exit")
    choice = int(input("enter your choice number="))
    if choice == 1:
        count = int(input("enter count for books for adding="))
        for i in range(1, count + 1):
            title = input(f"enter {i} book title=")
            books.append(title)

    elif choice == 2:
        print("Show all availables books")
        print(books)

    elif choice == 3:
        issuebook = input("enter book title which you want to issue=")
        if issuebook in books:
            books.remove(issuebook)
            print("Issued book successfully")
            print(books)
        else:
            print("Incorrect book title")

    elif choice == 4:
        returnbook = input("enter book title which you want to return=")
        if returnbook not in books:
            books.append(returnbook)
            print("Returned book successfully")
            print(books)
        else:
            print("Incorrect book title")

    elif choice == 5:
        break

    else:
        print("Invalid choice number")

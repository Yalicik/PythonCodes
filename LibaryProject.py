#Switch to nested dictionary
books_dictionary = {}

def list_authors_books():
    author_par = input("Write the searching parameters")
    for v in books_dictionary.values():
        if author_par == v["book’s author"]:
            print(v["book’s name"], v["book’s number"],"\n")


def return_book():
    returnbook_par = input("Write the searching parameters")
    if returnbook_par.isdigit():
        for v in books_dictionary.values():
            if returnbook_par == v["book’s number"]:
                if v["book taken"] == False:
                    print("This book is not taken")
                    break
                elif v["book taken"] == True:
                    v["book taken"] = False
                    print(v["book’s name"], "has been returned")
                    break
            elif returnbook_par != v["book’s number"]:
                print("Can not return book(s). Missing parameter(s).")
            else:
                pass
    else:
        for v in books_dictionary.values():
            if returnbook_par == v["book’s name"]:
                if v["book taken"] == False:
                    print("This book is not taken")
                    break
                elif v["book taken"] == True:
                    v["book taken"] = False
                    print(v["book’s name"], "has been returned")
                    break
            elif returnbook_par != v[["book’s name"]]:
                print("Can not return book(s). Missing parameter(s).")
            else:
                pass


def take_book():
    takebook_par = input("Write the searching parameters")
    take_par_list = takebook_par.split(',')
    p = 0
    if take_par_list[0].isdigit():
        for v in books_dictionary.values():
            if take_par_list[0] == v["book’s number"]:
                if v["book taken"] == True:
                    print("This book is already taken")
                    break
                elif v["book taken"] == False:
                    book_dict = books_dictionary[v["book’s name"]]
                    p += 1
                    v["book taken"] = True
                    if len(take_par_list) == 2:
                        book_dict['id of taker'] = take_par_list[1]
                    print(v["book’s name"], "has given with no problem.")
                    break
            else:
                pass
    else:
        for v in books_dictionary.values():
            if takebook_par == v["book’s name"]:
                if v["book taken"] == True:
                    print("This book is already taken")
                    break
                elif v["book taken"] == False:
                    v["book taken"] = True
                    p += 1
                    print(v["book’s name"], "has given with no problem.")
                    break
            elif takebook_par != v["book’s name"]:
                print("Could not find the book")
    if p == 0:
        print("Can not give book. Missing parameter(s).")


def command_list():
    print(" add book \t |-a| \t adds a new book to the system \n "
          "find book \t |-f| \t this command finds a book at the system \n "
          "list an author’s books \t |-la| \t finds the books of an author which are in the system \n "
          "take book \t |-n| \t give a book to someone \n "
          "return book \t |-r| \t returns a book which have taken by someone \n "
          "list books \t |-l| \t lists every book in the system \n "
          "list taken books \t |-lt| \t lists every taken book in the system \n "
          "list books before/after year \t |-ly| \t lists every book in the system with given dates \n "
          "quit \t |-q| \t quits program \n")


def find_book():
    search_par = input("Write the searching parameters")
    if search_par.isdigit():
        number_to_name = {v["book’s number"]: k for k, v in books_dictionary.items()}
        name = number_to_name.get(search_par, None)
        if name is None:
            print("Can not find book. There is no book like this in this system.")
        else:
            print(books_dictionary[name])

    else:
        result = books_dictionary.get(search_par, None)
        if result is None:
            print("Can not find book. There is no book like this in this system.")
        else:
            print(result)


def list_taken_books():
    o = 0
    for v in books_dictionary.values():
        if v['book taken'] == True:
            book_dict = books_dictionary[v["book’s name"]]
            print(book_dict["book’s name"], book_dict["book’s number"], book_dict['id of taker'], "\n")
        else:
            o += 1
            pass
    if o == len(books_dictionary):
        print("No one has taken books :(")


def add_book():
    print('"book’s name",', '"book’s number",','"book’s category",','"book’s placement",','"book’s author",','"book’s publishment year",')
    book_par = input("Write the books parameters")
    param_list = book_par.split(',')
    if len(param_list) != 6:
        print("Can not add book to the system. Missing parameter(s).")
    else:
        name, number, category, placement, author, year = param_list
        if books_dictionary.get(name, None):
            print("This book already exists.")
            # if dictionary includes the book already return this
        else:
            #Check the number and year is integer
            sub_dict = {
                "book’s name": name.strip(),
                "book’s number": number.replace(' ', ''),
                "book’s category": category.strip(),
                "book’s placement": placement.strip(),
                "book’s author": author.strip(),
                "book’s publishment year": year.replace(' ', ''),
                "book taken": False
            }
            books_dictionary[name] = sub_dict
            print(name," has added to the system")


def list_year():
    year_par = input("Write the year and before after command")
    par_list = year_par.split()
    par_list[0] = par_list[0].replace(',','')
    u = 0
    for v in books_dictionary.values():
        if par_list[0].isdigit():
            if par_list[1] == "before":
                if v['book’s publishment year'] < par_list[0]:
                    print(v["book’s name"], v["book’s number"],"\n")
                else:
                    u += 1
                    pass
            elif par_list[1] == "after":
                if v['book’s publishment year'] > par_list[0]:
                    print(v["book’s name"], v["book’s number"], "\n")
                else:
                    u += 1
                    pass
            else:
                print("Can not list book(s). Improper input.")
        else:
            print("Can not list book(s). Improper input.")
    if u == len(books_dictionary):
        print("There are no books that is published", par_list[1], par_list[0], "in the system.")


def list_books():
    i = 0
    for v in books_dictionary.values():
        print(v["book’s name"], v["book’s number"], v["book’s category"],v["book’s placement"], v["book’s author"],
              v["book’s publishment year"])
        i +=1
    if i == 0:
        print("There are no books in the system.")

while True:
    user_input = input("What would you want to do? (Write help for command list)")
    print("\n")
    if user_input == "add book" or user_input == "-a":
        add_book()
    elif user_input == "find book" or user_input == "-f":
        find_book()
    elif user_input == "list an author’s books" or user_input == "-la":
        list_authors_books()
    elif user_input == "take book" or user_input == "-t":
        take_book()
    elif user_input == "return book" or user_input == "-r":
        return_book()
    elif user_input == "list books" or user_input == "-l":
        list_books()
    elif user_input == "list taken books" or user_input == "-lt":
        list_taken_books()
    elif user_input == "list books before/after year" or user_input == "-ly":
        list_year()
    elif user_input == "help" or user_input == "-h":
        command_list()
    elif user_input == "quit" or user_input == "-q":
        print("See you later :)")
        break
    elif user_input == "":
        pass
    else:
        print("You have entered a command that does not exist. Write ‘help’ to get to know commands.")

from Helper import *

BOOK_ADDED = ' Book Added Successfully'
BOOK_NOT_FOUND = ' Book Not Found'
USER_ADDED = ' User Added Successfully'
USER_DELETED = ' User Deleted Successfully'
USER_NOT_FOUND = ' User Not Found'
USER_EMPTY = ' *** There is no user in the System, start adding some ***'

def display_menu():

    print(' -------------------------------------------------------------------------------------------------')
    print(' |                                         Library System                                        |')
    print(' -------------------------------------------------------------------------------------------------')
    print(' |----- Books                    |----- Users                    |----- Periodicals              |')
    print(' | 1.  Add Book                  | 7.  Add User                  | 11. Add Periodical            |')
    print(' | 2.  Borrow Book               | 8.  Delete User               | 12. Delete Periodical         |')
    print(' | 3.  Delete Book               | 9.  Display Users             | 13. Display Periodicals       |')
    print(' | 4.  Display Books             | 10. Search User               | 14. Search Periodical         |')
    print(' | 5.  Return Book               |                               |                               |')
    print(' | 6.  Search Book               |                               |                               |')
    print(' -------------------------------------------------------------------------------------------------')
    print(' |                                         Press X to Exit                                       |')
    print(' -------------------------------------------------------------------------------------------------')


# [1] Add Book
def add_book():
    get_page_title('Add Book')

    # get the latest ID
    last_id = get_book_last_id()
    print(f' LAST ID:{last_id}')

    isbn = input(' Enter ISBN:')
    # get a list with all ISBNs in the library
    l_isbn = get_isbns()

    # Check if it is used
    is_isbn_used = check_isbn(l_isbn, isbn)
    #print(is_isbn_used)

    # check if isbn is number, the length and if it is already used
    while not isbn.isdigit() or len(isbn) != 13 or is_isbn_used:
        # Print different error message to the user according to the input.
        if is_isbn_used:
            isbn = input(f' Try again, ISBN already in use\n Enter ISBN:')
        elif not isbn.isdigit():
            isbn = input(f' Try again, ISBN has to be only numbers\n Enter ISBN:')
        elif isbn != 13:
            isbn = input(f' Try again, ISBN has to have exactly 13 Digits\n Enter ISBN:')
        else:
            isbn = input(f' Try again,\n Enter ISBN:')

        l_isbn = get_isbns()
        is_isbn_used = check_isbn(l_isbn, isbn)

    # title can contain different characters
    title = input(' Enter Title:')

    # Maybe add a validation here, name is name
    author_reg = "^[A-Za-z ]*[A-Za-z][A-Za-z ]*$"
    flag = False
    author = input(f' TIP >>> Only Letters and spaces are allowed for AUTHOR NAME.\n Enter Author Name:')
    if check_string(author, author_reg):
        flag = True

    while not flag:
        author = input(f' Author Name invalid\n Please Enter only letters and spaces:')
        if check_string(author, author_reg):
            flag = True


    # check if year is number and if it has 4 digits or less
    # Allowing very old books, eg from the year: 989
    year = input(' Enter Year:')
    while not year.isdigit() or len(year) > 4:
        year = input(' Try Again, Enter Year:')

    # Use the latest ID and add 1 to it, e.g 10 + 1 = 11 < new ID to be used.
    new_book = Book(str(int(last_id) + 1), title, year, isbn, author, 'No')

    # Append new object Book to the list of books
    list_of_book.append(new_book)
    print(new_book)
    print(BOOK_ADDED)


# [2] Borrow Book
def borrow_book():
    get_page_title('Borrow Book')
    # get book index first get_book_index

    search_book = input(f' Check if the book is available to borrow:')
    book_index = get_book_index(search_book)
    print(f' {book_index} <<<<<<')

    if book_index != '':
        # Find if book is available
        print(f' {check_book_available(search_book)} <<<')
        b_index = check_book_available(search_book)
        while b_index[0] == 'No':
            print(b_index[1])
            b_index = check_book_available()

        print(b_index[1])

    else:
        print(f' I am lost')

    # Get the user
    search_index = input(f' User ID:')
    u_index =  get_user_index(search_index)

    if u_index != '':
        # Borrow book
        list_users[u_index].borrow_book(list_of_book[b_index[2]])
        # Update book stock
        list_of_book[b_index[2]].set_on_loan(list_users[u_index].get_name())
        print('=========')

        print(f'The book: {list_of_book[b_index[2]].get_title()} has been borrowed by {list_users[u_index].get_name()}')

    else:
        print(f' User index not found')


# [3] Delete Book
def delete_book():
    get_page_title('Delete Book')

    if list_of_book:
        search_book = input(' === TIP --> Deletion is done by book ID, if you do not know the book ID, press x to exit and chose option 4 from the menu to Display Books. ===\n'
                   ' Enter Book ID to be deleted:')

        while not search_book.isdigit() and search_book.lower() != 'x':
            search_book = input(
                ' === TIP --> Deletion is done by book ID, if you do not know the book ID, press x to exit and chose option 4 from the menu to Display Books. ===\n'
                ' Enter Book ID to be deleted:')

        if search_book.lower() != 'x':
            # Call method to get the user index in the list of users
            book_index = get_book_index(search_book)

            if book_index != '':
                if check_del_book(book_index):
                    delete = input(f' ** Delete Book {list_of_book[book_index].get_title()}** ? > [Y or N]')

                    # While user does not enter y or n, while loop keeps going
                    while delete.lower() not in ('y', 'n', 'x'):
                        delete = input(f' Option invalid.\n Please to delete A book {list_of_book[book_index].get_title()} enter [Y or N]')

                    if delete.lower() == 'y':
                        print(f' Book {list_of_book[book_index].get_title()} Deleted Successfully')
                        del list_of_book[book_index]
                    else:
                        print(f' Book {list_of_book[book_index].get_title()} not Deleted')
            else:
                print(f' Book Index not found')

    else:
        print(USER_EMPTY)





























# [4] Display Books
def display_books():
    get_page_title('Display Books')
    for b in list_of_book:
        print(b)


# [5] Return Book
def return_book():
    get_page_title('Return Book')


# [6] Search Book
def search_book():
    get_page_title('Search Book')
    to_search = input(' === TIP --> You can search by ID, Title, Publish Year, ISBN or Author ==='
                      '\n Please Enter the item to be search:')

    list_of_books_found = []
    for b in list_of_book:
        if to_search.lower() in str(b.get_isbn()).lower() \
                or to_search.lower() in str(b.get_item_id()).lower() \
                or to_search.lower() in str(b.get_title()).lower() \
                or to_search.lower() in str(b.get_author()).lower() \
                or to_search.lower() in str(b.get_year()).lower():
            list_of_books_found.append(str(b))

    if not list_of_books_found:
        print(BOOK_NOT_FOUND)
    else:
        for b in list_of_books_found:
            print(b)

    total = len(list_of_books_found)

    place_holder = 'Book'
    if total != 1:
        place_holder = 'Books'
    print(f' The total of: {total} {place_holder} found with the keyword [{to_search.upper()}]')











# [7] Add User
def add_user():
    get_page_title('Add User')

    # get the latest ID
    last_id = get_user_last_id()

    name_reg = "^[A-Za-z ]*[A-Za-z][A-Za-z ]*$"
    flag = False
    name = input(f' TIP >>> Only Letters and spaces are allowed.\n Enter Name:')
    if check_string(name,name_reg):
        flag = True

    while not flag:
        name = input(f' Name invalid\n Please Enter only letters and spaces:')
        if check_string(name, name_reg):
            flag = True

    addr_reg = "^[A-Za-z0-9 ,-]*[A-Za-z0-9][A-Za-z0-9 ,-]*$"
    flag = False
    address = input(f' TIP >>> Only Letters, Spaces, Commas(,) and Dashes(-) are allowed.\n Enter Address:')
    if check_string(address, addr_reg):
        flag = True

    while not flag:
        address = input(f' Name invalid\n Please Enter only Letters, Spaces, Commas(,) and Dashes(-):')
        if check_string(address, addr_reg):
            flag = True

    # Use the latest ID and add 1 to it, e.g 10 + 1 = 11 < new ID to be used.
    new_user = User(str(int(last_id) + 1), name, address)

    list_users.append(new_user)
    print(new_user)
    print(USER_ADDED)


# [8] Delete USer
def delete_user():
    get_page_title('Delete User')

    if list_users:
        user_id = input(' === TIP --> Deletion is done by USer ID, if you do not know the user ID, press x to exit and chose option 9 from the menu to search the User ID. ===\n'
                   ' Enter User ID to be deleted:')

        while not user_id.isdigit() and user_id.lower() != 'x':
            user_id = input(
                ' === TIP --> Deletion is done by USer ID, if you do not know the user ID, press x to exit and chose option 9 from the menu to search the User ID. ===\n'
                ' Enter User ID to be deleted:')

        if user_id.lower() != 'x':
            # Call method to get the user index in the list of users
            user_index = get_user_index(user_id)

            if user_index != '':

                if check_del_user(user_index):
                    delete = input(f' ** Delete User {list_users[user_index].get_name()}** ? > [Y or N]')

                    # While user does not enter y or n, while loop keeps going
                    while delete.lower() not in ('y', 'n', 'x'):
                        delete = input(f' Option invalid.\n Please to delete User {list_users[user_index].get_name()} enter [Y or N]')

                    if delete.lower() == 'y':
                        print(f' User {list_users[user_index].get_name()} Deleted Successfully')
                        del list_users[user_index]
                    else:
                        print(f' User {list_users[user_index].get_name()} User not Deleted')

            else:
                print(f' User ID not found')

    else:
        print(USER_EMPTY)


# [9] Display Users
def display_users():
    get_page_title('List of Users')

    if list_users:
        for u in list_users:
            print(f'{u}\n')
    else:
        print(USER_EMPTY)


# [10] Search User
def search_user():
    get_page_title('Search User')

    if list_users:
        search_user = input(' === TIP --> You can search User by ID, Name or Address. ==='
                          '\n Please Enter a user data to be search:')

        list_of_users_found = []
        for u in list_users:
            if search_user.lower() in str(u.get_name()).lower() \
                    or search_user.lower() in str(u.get_id()).lower() \
                    or search_user.lower() in str(u.get_address()).lower():
                        list_of_users_found.append(str(u))

        if not list_of_users_found:
            print(USER_NOT_FOUND)
        else:
            for u in list_of_users_found:
                print(u)
        total = len(list_of_users_found)

        place_holder = 'user'
        if total != 1:
            place_holder = 'users'

        print(f' The total of: {total} {place_holder} found with the keyword [{search_user.upper()}]')

    else:
        print(USER_EMPTY)
























# [11] Add Periodical
def add_periodical():
    get_page_title('Add Periodical')


# [12] Delete Periodical
def delete_periodical():
    get_page_title('Delete Periodical')


# [13] Display Periodicals
def display_periodicals():
    get_page_title('Display Periodicals')


# [14] Search Periodical
def search_periodical():
    get_page_title('Search Periodical')


def menu_control():
    # Ask the user to choose a number on the menu
    opt = input(' Please enter a option:')

    # Program terminates when user enters [x] or [X]
    while opt.upper() != 'X':

        # [1] Add Book
        if opt == '1':
            add_book()

        # [2] Borrow Book
        elif opt == '2':
            borrow_book()

        # [3] Delete Book
        elif opt == '3':
            delete_book()

        # [4] Display Books
        elif opt == '4':
            display_books()

        # [5] Return Book
        elif opt == '5':
            return_book()

        # [6] Search Book
        elif opt == '6':
            search_book()

        # [7] Add User
        elif opt == '7':
            add_user()

        # [8] Delete USer
        elif opt == '8':
            delete_user()

        # [9] Display Users
        elif opt == '9':
            display_users()

        # [10] Search User
        elif opt == '10':
            search_user()

        # [11] Add Periodical
        elif opt == '11':
            add_periodical()

        # [12] Delete Periodical
        elif opt == '12':
            delete_periodical()

        # [13] Display Periodicals
        elif opt == '13':
            display_periodicals()

        # [14] Search Periodical
        elif opt == '14':
            search_periodical()

        # Invalid Option
        else:
            print(' === Option Invalid, Please try again ===\n')

        display_menu()
        opt = input(' Please enter a option:')

display_menu()
menu_control()

prog_end = ' === The system has terminated ===\n'
print(f'{prog_end.upper()}')
# ===================================================================================

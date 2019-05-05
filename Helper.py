from items import *

# Print the title of the pager where the user is navigating.
def get_page_title(page_title):
    print(' ' + page_title + '\n ' + len(page_title) * '=')


# Get the latest ID used
def get_latest_id(choice=None):
    list_of_ids = []
    if choice == 'for_user':
        for u in list_users:
            list_of_ids.append(u.get_id())

    else:
        # Getting all books ID
        for b in list_of_book:
            list_of_ids.append(b.get_item_id())

        # Getting all Periodicals ID
        for p in list_of_periodical:
            list_of_ids.append(p.get_item_id())

    # sort list, as the values are string, I am using (key=int) to sort it as integers.
    list_of_ids.sort(key=int)

    # Return the last value of the list, which is the highest number.
    return list_of_ids[-1]


# Return a list with all ISBN in the Library
def get_isbns():
    list_isbn = []
    for b in list_of_book:
        list_isbn.append(b.get_isbn())

    return list_isbn


# Check if ISBN is already in use for another book, returns True/False
def check_isbn(list_isbn,  check_isbn):
    if check_isbn in list_isbn:
        return True
    return False

def check_book_available():
    search_book = input(f' Ckeck if the book is available to borrow:')
    rc = ['No', ' Book not in the system', -1]
    for b in list_of_book:
        if b.get_item_id() == search_book :

            if b.get_on_loan() != 'No':
                rc = ['No', ' Book Already Borrowed\n Try again', -1]
            else:
                rc = ['True', ' Book Available', list_of_book.index(b)]

    return rc

def get_user():
    #u = input('Enter user ID who wants to borrow a book:')
    # do A while loop ????
    search_user = input('Enter a user ID to borrow:')
    get_user_index = ''
    for u in list_users:
        if u.get_id() == search_user:
            get_user_index = list_users.index(u)

    return get_user_index


def add_comma(list):
    print(list)


def get_book_index(book_id):
    get_index = -1
    for b in list_of_book:
        if b.get_item_id() == book_id:
            get_index = list_of_book.index(b)

    return get_index
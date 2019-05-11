from Items import *


# Print the title of the pager where the user is navigating.
def get_page_title(page_title):
    print(' ' + page_title + '\n ' + len(page_title) * '=')


def get_book_last_id():
    # Getting all books ID

    if list_of_book:

        list_of_ids = []
        for b in list_of_book:
            list_of_ids.append(b.get_item_id())

            # sort list, as the values are string, I am using (key=int) to sort it as integers.
            list_of_ids.sort(key=int)

    else:
        list_of_ids = ['0']

    # Return the last value of the list, which is the highest number.
    return list_of_ids[-1]


def get_periodical_last_id():
    # Getting all Periodicals ID
    if list_of_periodical:
        list_of_ids = []
        for p in list_of_periodical:
            list_of_ids.append(p.get_item_id())

        # sort list, as the values are string, I am using (key=int) to sort it as integers.
        list_of_ids.sort(key=int)

    else:
        list_of_ids = ['0']

    # Return the last value of the list, which is the highest number.
    return list_of_ids[-1]


# Get the latest ID used
def get_user_last_id():

    if list_users:
        list_of_ids = []

        for u in list_users:
            list_of_ids.append(u.get_id())

        # sort list, as the values are string, I am using (key=int) to sort it as integers.
        list_of_ids.sort(key=int)
    else:
        list_of_ids = ['0']

    # Return the last value of the list, which is the highest number.
    return list_of_ids[-1]


# Return a list with all ISBN in the Library
def get_isbns():
    list_isbn = []
    for b in list_of_book:
        list_isbn.append(b.get_isbn())

    return list_isbn


# Check if ISBN is already in use for another book, returns True/False
def check_isbn(list_isbn, check_isbn):
    if check_isbn in list_isbn:
        return True
    return False


def check_book_available(search_book):
    rc = ['No', ' Book not in the system', '']
    for b in list_of_book:
        if b.get_item_id() == search_book:

            if b.get_on_loan() != 'No':
                rc = ['No', ' Book Already Borrowed\n Try again', '']
            else:
                rc = ['True', ' Book Available', list_of_book.index(b)]

    return rc


def get_user_index(user_id):
    get_user_index = ''
    for u in list_users:
        if u.get_id() == user_id:
            get_user_index = list_users.index(u)

    return get_user_index


def get_book_index(book_id):
    get_index = ''
    for b in list_of_book:
        if b.get_item_id() == book_id:
            get_index = list_of_book.index(b)

    return get_index


def get_periodical_index(periodical_id):
    get_index = ''
    for b in list_of_periodical:
        if b.get_item_id() == periodical_id:
            get_index = list_of_periodical.index(b)

    return get_index


def check_del_user(user_index):
    # If user has any book borrowed, we can not delete it.
    if list_users[user_index].get_book_on_loan():
        rc = False
        print(f' User can not be Deleted. User needs do bring back the following book: '
              f'{list_users[user_index].get_book_on_loan()}')
    else:
        rc = True
    return rc


def check_del_book(book_index):
    # If any book is borrowed, we can not delete it.
    print(f'   {list_of_book[book_index].get_on_loan()}\n====')
    if list_of_book[book_index].get_on_loan() != 'No':
        rc = False
        print(f' Book can not be Deleted.\n'
              f' The User {list_of_book[book_index].get_on_loan()} needs do bring it back before delete the'
              f' book from the system')
    else:
        rc = True
    return rc


def check_string(word, reg):
    import re
    r = re.compile(reg)
    return not r.match(word) is None
